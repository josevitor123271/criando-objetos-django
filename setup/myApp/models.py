from django.db import models

# Create your models here.

# Classe editora
class Loja(models.Model):
    nome = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2)
    website = models.URLField()

    # Retorna o nome da Loja
    def __str__(self):
        return self.nome

# Classe livro
class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.TextField()
    estoque = models.ForeignKey(Loja, on_delete=models.CASCADE)

    # Retorna o nome do produto
    def __str__(self):
        return self.nome
 