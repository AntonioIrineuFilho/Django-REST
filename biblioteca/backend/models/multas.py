from django.db import models

class Multas(models.Model):
    id_usuario = models.IntegerField(blank=False, null=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    data_pagamento = models.DateField()

    class Meta:
        verbose_name = "Multa"
        verbose_name_plural = "Multas"
        ordering = ["data_pagamento"]

    def __str__(self):
        return str(self.valor)