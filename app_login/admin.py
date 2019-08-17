from django.contrib import admin
from .models import SimuladoFormacao, SimuladoComponente, SimuladoEndereco, SimuladoResponsaveisTecnicos, \
    SimuladoEmpresaCrea, ObrasEmAndamento, SimuladoModalidade
# Register your models here.

admin.site.register(SimuladoFormacao)
admin.site.register(SimuladoComponente)
admin.site.register(SimuladoEndereco)
admin.site.register(SimuladoResponsaveisTecnicos)
admin.site.register(SimuladoEmpresaCrea)
admin.site.register(ObrasEmAndamento)
admin.site.register(SimuladoModalidade)