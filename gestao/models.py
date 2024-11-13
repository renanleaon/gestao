from django.db import models

# Modelo de Fornecedor
class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    contato = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome

# Modelo de Produto
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    quantidade_minima = models.PositiveIntegerField(default=0)
    quantidade_maxima = models.PositiveIntegerField(default=100)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

    def atualizar_estoque(self, quantidade, tipo):
        if tipo == 'compra':
            self.estoque += quantidade
        elif tipo == 'venda':
            self.estoque -= quantidade
        self.save()

# Modelo de Cliente
class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, null=True)  # CPF como campo único
    contato = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome

# Modelo de Venda
class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_venda = models.DateField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venda {self.id} - Cliente: {self.cliente.nome}"

# Modelo de Compra
class Compra(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    data_compra = models.DateField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Compra {self.id} - Fornecedor: {self.fornecedor.nome}"

# Modelo de ItemVenda
class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens_venda')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.produto.atualizar_estoque(self.quantidade, 'venda')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Item {self.id} - Venda {self.venda.id} - Produto: {self.produto.nome}"

# Modelo de ItemCompra
class ItemCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itens_compra')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.produto.atualizar_estoque(self.quantidade, 'compra')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Item {self.id} - Compra {self.compra.id} - Produto: {self.produto.nome}"





# from django.db import models

# # Modelo de Fornecedor
# class Fornecedor(models.Model):
#     nome = models.CharField(max_length=255)
#     contato = models.CharField(max_length=255, blank=True, null=True)
#     telefone = models.CharField(max_length=20, blank=True, null=True)
#     email = models.EmailField(blank=True, null=True)
#     endereco = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return self.nome

# # Modelo de Produto
# class Produto(models.Model):
#     nome = models.CharField(max_length=255)
#     descricao = models.TextField(blank=True, null=True)
#     preco = models.DecimalField(max_digits=10, decimal_places=2)
#     estoque = models.PositiveIntegerField()
#     fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return self.nome

# # Modelo de Cliente
# class Cliente(models.Model):
#     nome = models.CharField(max_length=255)
#     cpf = models.CharField(max_length=14, null=True )  # CPF como campo único
#     contato = models.CharField(max_length=255, blank=True, null=True)
#     telefone = models.CharField(max_length=20, blank=True, null=True)
#     email = models.EmailField(blank=True, null=True)
#     endereco = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return self.nome

# # Modelo de Venda
# class Venda(models.Model):
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     data_venda = models.DateField(auto_now_add=True)
#     valor_total = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Venda {self.id} - Cliente: {self.cliente.nome}"

# # Modelo de Compra
# class Compra(models.Model):
#     fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
#     data_compra = models.DateField(auto_now_add=True)
#     valor_total = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Compra {self.id} - Fornecedor: {self.fornecedor.nome}"

# # Modelo de ItemVenda
# class ItemVenda(models.Model):
#     venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens_venda')
#     produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
#     quantidade = models.PositiveIntegerField()
#     preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Item {self.id} - Venda {self.venda.id} - Produto: {self.produto.nome}"

# # Modelo de ItemCompra
# class ItemCompra(models.Model):
#     compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itens_compra')
#     produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
#     quantidade = models.PositiveIntegerField()
#     preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Item {self.id} - Compra {self.compra.id} - Produto: {self.produto.nome}"
