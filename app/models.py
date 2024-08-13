from django.db import models

# Create your models here.

class Usuario(models.Model):
    apelido = models.CharField(max_length=10, primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    idade = models.IntegerField()

    def __str__(self):
        return f'Apelido: {self.apelido} | Nome: {self.nome} | Email: {self.email} | Idade: {self.idade}'