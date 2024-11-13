from django import forms
from .models import Cliente, Fornecedor, Produto, Venda

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'telefone', 'email',]

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'contato', 'telefone', 'email', 'endereco',]

class ProdutoForm(forms.ModelForm):
    fornecedor = forms.ModelChoiceField(queryset=Fornecedor.objects.all(), required=True)

    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'estoque', 'fornecedor']


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'valor_total', ]


        
