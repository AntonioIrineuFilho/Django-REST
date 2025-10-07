from django.db import models

class Livros(models.Model):
    titulo = models.CharField(max_length=64, blank=False, null=False)
    autor = models.CharField(max_length=64, blank=False, null=False)
    ano_publicacao = models.IntegerField(blank=False, null=False)
    genero = models.CharField(max_length=64, blank=False, null=False)

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
        ordering = ["titulo"]
    
    def __str__(self):
        return self.titulo