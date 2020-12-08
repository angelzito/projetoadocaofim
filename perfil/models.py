from django.db import models

class Cadastro(models.Model):
    denuncia = models.CharField(max_length=100)
    hora = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    gravidade_alta_ou_muito_alta = models.CharField(max_length=100)
    porte = models.CharField(max_length=100)
    espécie = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    contato_do_denunciante = models.CharField(max_length=100)
    teste = models.CharField(max_length=100, null=True)
    teste_dois = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.gravidade_alta_ou_muito_alta