from django.contrib import admin
from .models import SimuladoFormacao, SimuladoProfissionais, SimuladoFornecedor, Ocorrencia
# Register your models here.


class OcorrenciaAdmin(admin.ModelAdmin):
     list_display = ('id', 'fornecedor', 'status', 'componente', 'status', )


class FornecedoresAdmin(admin.ModelAdmin):
     list_display = ('cnpj', 'nome',)


class ProfissionaisAdmin(admin.ModelAdmin):
     list_display = ('cpf', 'nome',)


admin.site.register(SimuladoFornecedor, FornecedoresAdmin)
admin.site.register(SimuladoProfissionais, ProfissionaisAdmin)
admin.site.register(SimuladoFormacao)
admin.site.register(Ocorrencia, OcorrenciaAdmin)