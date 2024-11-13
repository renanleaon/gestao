from django.shortcuts import render
from gestao.models import Fornecedor, Produto, Cliente, Compra, Venda, ItemCompra, ItemVenda
from .forms import ClienteForm, FornecedorForm, ProdutoForm, VendaForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# def index(request):
#     books = Book.objects.all()
#     genre = Genre.objects.all()  # Pegando todos os gêneros
#     return render(request, 'gestao/index.html', {'cards': books, 'genres': genre})


def index(request):
    return render(request, 'gestao/index.html')

def cadastrofornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Fornecedor cadastrado com sucesso!")
            return render(request, 'gestao/cadastro_fornecedor.html')  # Redireciona para a página inicial ou outra página desejada
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
            return render(request, 'gestao/cadastro_produto.html')  # Redireciona para a página inicial ou outra página desejada
        else:
            messages.error(request, "Erro ao cadastrar produto. Verifique os dados informados.")
    else:
        form = ProdutoForm()    
        return render(request, 'gestao/cadastro_produto.html', {'form': form})


def cadastrocliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente cadastrado com sucesso!")
            return render(request, 'gestao/cadastro_cliente.html')  # Redireciona para a página inicial ou outra página desejada
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
    fornecedor = Fornecedor.objects.all()
    return render(request, 'gestao/consulta_fornecedor.html', {'fornecedor' : fornecedor})

def consultacliente(request):
    cliente = Cliente.objects.all()
    return render(request, 'gestao/consulta_cliente.html', {'clientes' : cliente})

def consultaproduto(request):
    produto = Produto.objects.all()
    return render(request, 'gestao/consulta_produto.html', {'produto': produto})

def consultavenda(request):
    venda = Venda.objects.all()
    return render(request, 'gestao/consulta_venda_compra.html', {'venda': venda})


@csrf_exempt  # Para fins de teste, remova em produção ou use o CSRF corretamente.
def editar_produto(request, id):
    if request.method == 'POST':
        try:
            # Recebe os dados enviados via AJAX
            nome = request.POST.get('nome')
            descricao = request.POST.get('descricao')
            preco = request.POST.get('preco')
            estoque = request.POST.get('estoque')
            fornecedor = request.POST.get('fornecedor')

            # Verifica se todos os campos estão preenchidos
            if not nome or not descricao or not preco or not estoque or not fornecedor:
                return JsonResponse({'status': 'error', 'message': 'Todos os campos devem ser preenchidos!'}, status=400)

            # Atualiza o produto no banco de dados
            produto = Produto.objects.get(id=id)
            produto.nome = nome
            produto.descricao = descricao
            produto.preco = preco
            produto.estoque = estoque
            produto.fornecedor = fornecedor
            produto.save()  # Salva as alterações no banco de dados

            return JsonResponse({'status': 'success', 'message': 'Produto atualizado com sucesso!'})
        
        except Produto.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Produto não encontrado!'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Método inválido!'}, status=405)


def excluir_produto(request, id):
    if request.method == 'POST':
        try:
            # Tenta encontrar o produto pelo ID e excluir
            produto = Produto.objects.get(id=id)
            produto.delete()

            # Retorna uma resposta JSON de sucesso
            return JsonResponse({'status': 'success', 'message': 'Produto excluído com sucesso!'})

        except Produto.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Produto não encontrado!'})

    return JsonResponse({'status': 'error', 'message': 'Método inválido!'})