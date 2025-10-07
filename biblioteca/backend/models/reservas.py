from django.db import models
from django.utils import timezone

class Reservas(models.Model):
    id_usuario = models.IntegerField(blank=False, null=False)
    id_livro = models.IntegerField(blank=False, null=False)
    data_reserva = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["data_reserva"]
    
    def __str__(self):
        return str(self.data_reserva)