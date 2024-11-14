from django.urls import path
from gestao.views import index, cadastrofornecedor, cadastroproduto, cadastrocliente, consultacliente, consultafornecedor, consultaproduto, cadastrocompra, editar_produto, excluir_produto, editar_cliente, excluir_cliente, editar_fornecedor, excluir_fornecedor, consultas_vendas_compras, editar_compra, editar_venda, excluir_compra, excluir_venda


urlpatterns = [
    path('', index, name='index'),
    path('cadastrofornecedor/', cadastrofornecedor, name='cadastrofornecedor'),
    path('cadastroproduto/', cadastroproduto, name='cadastroproduto'),
    path('cadastrocliente/', cadastrocliente, name='cadastrocliente'),
    path('cadastrocompra/', cadastrocompra, name='cadastrocompra'),
    path('consultaproduto/', consultaproduto, name='consultaproduto'),
    path('consultacliente/', consultacliente, name='consultacliente'),    
    path('consultafornecedor/', consultafornecedor, name='consultafornecedor'),    
   

    path('editar_produto/<int:id>/', editar_produto, name='editar_produto'),
    path('excluir_produto/<int:id>/', excluir_produto, name='excluir_produto'),
    path('editar_cliente/<int:id>/', editar_cliente, name='editar_cliente'),
    path('excluir_cliente/<int:id>/', excluir_cliente, name='excluir_cliente'),
    path('editar_fornecedor/<int:id>/', editar_fornecedor, name='editar_fornecedor'),
    path('excluir_fornecedor/<int:id>/', excluir_fornecedor, name='excluir_fornecedor'),
   
    path('consultas_vendas_compras/', consultas_vendas_compras, name='consultas_vendas_compras'),
    path('editar_venda/<int:id>/', editar_venda, name='editar_venda'),
    path('excluir_venda/<int:id>/', excluir_venda, name='excluir_venda'),
    path('editar_compra/<int:id>/', editar_compra, name='editar_compra'),
    path('excluir_compra/<int:id>/', excluir_compra, name='excluir_compra'),




]