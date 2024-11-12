from django.urls import path
from gestao.views import index, cadastrofornecedor, cadastroproduto, cadastrocliente, consultacliente, consultafornecedor, consultavenda, consultaproduto, cadastrocompra


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
]