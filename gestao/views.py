from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from gestao.models import Fornecedor, Produto, Cliente, Compra, Venda, ItemCompra, ItemVenda
from .forms import ClienteForm, FornecedorForm, ProdutoForm, VendaForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

def consultavenda(request):
    venda = Venda.objects.all()
    return render(request, 'gestao/consulta_venda_compra.html', {'venda': venda})

def consultaproduto(request):
    produto = Produto.objects.all()
    return render(request, 'gestao/consulta_produto.html', {'produto': produto})

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

