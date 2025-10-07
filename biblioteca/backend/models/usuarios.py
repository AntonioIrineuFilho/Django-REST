from django.db import models
from django.utils import timezone

class Usuarios(models.Model):
    nome = models.CharField(max_length=64, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    data_registro = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["nome"]

    def __str__(self):
        return self.nome