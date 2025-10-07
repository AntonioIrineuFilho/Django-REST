from django.db import models

class Editoras(models.Model):
    nome = models.CharField(max_length=64, blank=False, null=False)
    endereco = models.TextField(null=False)

    class Meta:
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"
        ordering = ["nome"]
    
    def __str__(self):
        return self.nome