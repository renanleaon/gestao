from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from gestao.models import Fornecedor, Produto, Cliente, Compra, Venda, ItemCompra, ItemVenda
from .forms import ClienteForm, FornecedorForm, ProdutoForm, VendaForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import os
from django.conf import settings

def index(request):
    return render(request, 'gestao/index.html')


def cadastrofornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Fornecedor cadastrado com sucesso!")
        else:
            messages.error(request, "Erro ao cadastrar fornecedor. Verifique os dados informados.")
    else:
        form = FornecedorForm()
    return render(request, 'gestao/cadastro_fornecedor.html', {'form': form})

   

def cadastroproduto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto cadastrado com sucesso!")
            return render(request, 'gestao/cadastro_produto.html',{'form': form, 'fornecedores': Fornecedor.objects.all()})  # Redireciona para a página inicial ou outra página desejada
        else:
            messages.error(request, "Erro ao cadastrar produto. Verifique os dados informados.")
    else:
        form = ProdutoForm()    
        return render(request, 'gestao/cadastro_produto.html', {'form': form, 'fornecedores': Fornecedor.objects.all()})


def cadastrocliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente cadastrado com sucesso!")
        else:
            messages.error(request, "Erro ao cadastrar cliente. Verifique os dados informados.")
    else:
        form = ClienteForm()
    return render(request, 'gestao/cadastro_cliente.html', {'form': form})


def cadastrocompra(request):
    clientes = Cliente.objects.all()
    fornecedores = Fornecedor.objects.all()

    if request.method == 'POST':
        if 'cliente' in request.POST:
            # Lógica para cadastrar uma venda
            cliente = Cliente.objects.get(id=request.POST['cliente'])
            valor_total = request.POST['valor_total']
            Venda.objects.create(cliente=cliente, valor_total=valor_total)                  
        elif 'fornecedor' in request.POST:
            # Lógica para cadastrar uma compra
            fornecedor = Fornecedor.objects.get(id=request.POST['fornecedor'])
            valor_total = request.POST['valor_total']
            Compra.objects.create(fornecedor=fornecedor, valor_total=valor_total)
        messages.success(request, "Cadastrado com sucesso!")
    return render(request, 'gestao/cadastro_venda_compra.html', {'clientes': clientes,'fornecedores': fornecedores
    })
    

def consultafornecedor(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'gestao/consulta_fornecedor.html', {'fornecedores': fornecedores})

def editar_fornecedor(request, id):
    if request.method == 'POST':
        fornecedor = get_object_or_404(Fornecedor, id=id)
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Invalid request method'})

def excluir_fornecedor(request, id):
    if request.method == 'POST':
        fornecedor = get_object_or_404(Fornecedor, id=id)
        fornecedor.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': 'Invalid request method'})



def consultacliente(request):
    cliente = Cliente.objects.all()
    return render(request, 'gestao/consulta_cliente.html', {'clientes' : cliente})


def consultaproduto(request):
    produto = Produto.objects.all()
    return render(request, 'gestao/consulta_produto.html', {'produto': produto})


# Excluir ou alterar dados PRODUTOS

def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False})

def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# Excluir ou alterar dados CLIENTES

def consultacliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'gestao/consulta_cliente.html', {'clientes': clientes})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False})

def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})





def consultas_vendas_compras(request):
    vendas = Venda.objects.all()
    compras = Compra.objects.all()
    return render(request, 'gestao/consulta_venda_compra.html', {'vendas': vendas, 'compras': compras})

def editar_venda(request, id):
    if request.method == 'POST':
        venda = get_object_or_404(Venda, id=id)
        form = VendaForm(request.POST, instance=venda)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Invalid request method'})

def excluir_venda(request, id):
    if request.method == 'POST':
        venda = get_object_or_404(Venda, id=id)
        venda.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': 'Invalid request method'})

def editar_compra(request, id):
    if request.method == 'POST':
        compra = get_object_or_404(Compra, id=id)
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Invalid request method'})

def excluir_compra(request, id):
    if request.method == 'POST':
        compra = get_object_or_404(Compra, id=id)
        compra.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': 'Invalid request method'})

def consulta_github(request):
    # Define valor padrão se não for enviado nenhum usuário
    github_user = request.GET.get('usuario', 'octocat') 
    url = f'https://api.github.com/users/{github_user}'
    
    try:
        #Faz requisição para a api do GitHub de acordo com o github_user
        response = requests.get(url)

        #Se houver sucesso retorna os dados
        if response.status_code == 200:
            dados = response.json()

        #Senão, retorna erro
        else:
            dados = {'erro': 'Usuário não encontrado ou erro na API.'}

    #Se houver falhar na requisição retorna erro
    except requests.RequestException:
        dados = {'erro': 'Erro ao se conectar com o GitHub.'}

    #Havendo sucesso retornará os dados prontos para consumo
    return render(request, 'gestao/consulta_github.html', {'dados': dados, 'usuario': github_user})

def consulta_google_maps(request):
    #Caso a consulta seja por endereço recebe o valor enviado para consulta
    endereco = request.GET.get('endereco')

    #Caso a consulta seja por coordenadas recebe o valor enviado para consulta
    lat = request.GET.get("lat")
    lng = request.GET.get("lng")
    resultado = {}
    endereco_formatado = None

    #Recebe a chave da API do Google Maps configurada no .env
    api_key = os.environ.get("GOOGLE_MAPS_API_KEY", "")

    #Valida se existe a chave no .env
    if not api_key:
        return JsonResponse({'erro': 'Chave da API do Google não configurada.'})

    try:
        #Se a consulta for por endereço
        if endereco:
            url = "https://maps.googleapis.com/maps/api/geocode/json"
            params = {'address': endereco, 'key': api_key}

        #Se a consulta for por coordenadas
        elif lat and lng:
            url = "https://maps.googleapis.com/maps/api/geocode/json"
            params = {'latlng': f"{lat},{lng}", 'key': api_key}

        #Senão houverem valores corretos para consultar retornará erro
        else:
            return render(request, 'gestao/consulta_google_maps.html', {
                'erro': 'É necessário informar um endereço ou coordenadas.'
            })

        #Armazena retorno da requisição
        response = requests.get(url, params=params)

        #Se houver sucesso na consulta
        if response.status_code == 200:

            #Retorna o resultado formatado
            resultado = response.json()

            #Consigura validação e formatação para os dados de retorno
            if 'results' in resultado and resultado['results']:
                endereco_formatado = resultado['results'][0]['formatted_address']
                location = resultado['results'][0]['geometry']['location']

                #Formata coordenadas
                coordenadas_formatada = format_location(location)

            #Se não houverem dados encontrados no retorno da requisição
            else:
                resultado = {'erro': 'Nenhum dado encontrado para as coordenadas informadas.'}

        #Se houver falha ao tentar consultar
        else:
            resultado = {'erro': 'Erro ao consultar a API do Google Maps.'}

    #Retorna erro quando houver problemas com conexão
    except requests.RequestException as e:
        resultado = {'erro': f'Erro de conexão: {str(e)}'}

    #Havendo sucesso retorna os dados para serem consumidos
    return render(request, 'gestao/consulta_google_maps.html', {
        'resultado': resultado,
        'coordenadas': coordenadas_formatada,
        'endereco_formatado': endereco_formatado,
        'lat': lat,
        'lng': lng,
        'endereco': endereco,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
})

# Função responsável por formatar os campos de latitude e longitude
def format_location(location):
    return {
        'lat': f"{location['lat']:.6f}".replace(",", "."),
        'lng': f"{location['lng']:.6f}".replace(",", ".")
    }

