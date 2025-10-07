from django.db import models
from django.utils import timezone

class Emprestimos(models.Model):
    id_livro = models.IntegerField(blank=False, null=False)
    id_usuario = models.IntegerField(blank=False, null=False)
    data_emprestimo = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"
        ordering = ["data_emprestimo"]

    def __str__(self):
        return str(self.data_emprestimo)