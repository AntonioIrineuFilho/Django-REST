from django.contrib import admin
from .models import Projeto, Coluna, Etiqueta, Tarefa, Comentario

admin.site.register(Projeto)
admin.site.register(Coluna)
admin.site.register(Etiqueta)
admin.site.register(Tarefa)
admin.site.register(Comentario)
