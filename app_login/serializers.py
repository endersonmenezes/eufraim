from rest_framework import serializers
from .models import Ocorrencia


class OcorrenciaSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField()
    profissionais = serializers.SerializerMethodField()

    def get_status(self, obj):
        return obj.get_status_display()

    def get_profissionais(self, obj):
        data_array_tmp = []
        for profissional in obj.fornecedor.profissionais.all():
            data_tmp = {}
            data_tmp['nome'] = profissional.nome
            data_tmp['titulo'] = [str(titulo) for titulo in profissional.titulos.all()]
            data_array_tmp.append(data_tmp)
        return data_array_tmp

    class Meta:
        model = Ocorrencia
        fields = '__all__'
