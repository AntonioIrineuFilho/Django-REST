from django.db import models

class Autores(models.Model):
    nome = models.CharField(max_length=64, blank=False, null=False)
    data_nascimento = models.DateField(null=False)
    nacionalidade = models.CharField(max_length=64, null=False)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ["nome"]
    
    def _str__(self):
        return self.nome
