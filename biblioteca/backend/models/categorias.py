from django.db import models

class Categorias(models.Model):
    nome = models.CharField(max_length=64, blank=False, null=False)
    descricao = models.TextField(null=False)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nome"]
    
    def __str__(self):
        return self.nome