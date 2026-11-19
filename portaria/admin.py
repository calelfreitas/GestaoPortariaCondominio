from django.contrib import admin
from .models import Morador, Funcionario, Entrega, Entrada, Ocorrencia

admin.site.register(Morador)
admin.site.register(Funcionario)
admin.site.register(Entrega)
admin.site.register(Entrada)
admin.site.register(Ocorrencia)
