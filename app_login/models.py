from django.db import models

# Create your models here.


class SimuladoFormacao(models.Model):
    nome = models.CharField(max_length=60, blank=True, null=True)
    descricao = models.TextField()

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name_plural = '1 - Lista de Formações'
        verbose_name = '1 - Lista de Formações'


class SimuladoProfissionais(models.Model):
    nome = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11)
    titulos = models.ManyToManyField(SimuladoFormacao)

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name_plural = '2 - Lista de Profissionais'
        verbose_name = '2 - Lista de Profissionais'


class SimuladoFornecedor(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(primary_key=True, max_length=14)
    profissionais = models.ManyToManyField(SimuladoProfissionais)

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name_plural = '3 - Lista de Fornecedores'
        verbose_name = '3 - Lista de Fornecedores'


class Ocorrencia(models.Model):
    STATUS_CHOICES = (
        (0, 'Fila de Análise'),
        (1, 'É uma ocorrencia'),
        (2, 'Não é uma ocorrencia'),
    )
    fornecedor = models.ForeignKey(SimuladoFornecedor, on_delete=models.PROTECT)
    contrato_numero = models.CharField(max_length=255)
    contrato_projeto = models.IntegerField(null=True, blank=True)
    contrato_lote = models.IntegerField(null=True, blank=True)
    componente = models.CharField(max_length=60)
    contrato_valor = models.FloatField(null=True, blank=True)
    fotos = models.URLField(null=True, blank=True)
    executor = models.CharField(max_length=50, null=True, blank=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = '4 - Lista de Ocorrências'
        verbose_name = '4 - Lista de Ocorrências'
        unique_together = ('fornecedor', 'contrato_numero', 'contrato_projeto', 'contrato_lote')
