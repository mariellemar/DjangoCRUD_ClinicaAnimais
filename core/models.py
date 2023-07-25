from django.db import models

class Animal(models.Model):
    nome = models.CharField(max_length=50)

    CACHORRO = "Cachorro "
    GATO = "Gato "
    PASSARO = "Passaro "
    CAVALO = "Cavalo "

    ESPECIE_CHOICES = [
        (CACHORRO, "Cachorro"),
        (GATO, "Gato"),
        (PASSARO, "Passaro"),
        (CAVALO, "Cavalo")
    ]

    especie = models.CharField(
        max_length = 15,
        choices = ESPECIE_CHOICES,
    )

    nome_dono = models.CharField(max_length=50)
    telefone = models.CharField(max_length=12)

    def __str__(self):
        return self.nome
    

