from django.urls import path
from gestao.views import index, cadastrofornecedor, cadastroproduto, cadastrocliente, consultacliente, consultafornecedor, consultavenda, consultaproduto, cadastrocompra, editar_produto, excluir_produto


urlpatterns = [
    path('', index, name='index'),
    path('cadastrofornecedor/', cadastrofornecedor, name='cadastrofornecedor'),
    path('cadastroproduto/', cadastroproduto, name='cadastroproduto'),
    path('cadastrocliente/', cadastrocliente, name='cadastrocliente'),
    path('cadastrocompra/', cadastrocompra, name='cadastrocompra'),
    path('consultaproduto/', consultaproduto, name='consultaproduto'),
    path('consultacliente/', consultacliente, name='consultacliente'),    
    path('consultafornecedor/', consultafornecedor, name='consultafornecedor'),    
    path('consultavenda/', consultavenda, name='consultavenda'),    

    path('editar_produto/<int:id>/', editar_produto, name='editar_produto'),
    path('excluir_produto/<int:id>/', excluir_produto, name='excluir_produto'),
]