from django.contrib import admin
from .models import SimuladoFormacao, SimuladoProfissionais, SimuladoFornecedor, Ocorrencia
# Register your models here.


class OcorrenciaAdmin(admin.ModelAdmin):
     list_display = ('id', 'fornecedor', 'status', 'componente', 'status')


admin.site.register(SimuladoFornecedor)
admin.site.register(SimuladoProfissionais)
admin.site.register(SimuladoFormacao)
admin.site.register(Ocorrencia, OcorrenciaAdmin)