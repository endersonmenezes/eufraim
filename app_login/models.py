from django.db import models

# Create your models here.


class SimuladoEndereco(models.Model):
    endereco_descricao = models.CharField(max_length=255)
    endereco_numero = models.PositiveIntegerField()
    endereco_cep = models.IntegerField()
    bairro = models.CharField(max_length=255)

    def __str__(self):
        return str(self.endereco_cep)

    class Meta:
        verbose_name_plural = '6 - Endereços Cadastrados'
        verbose_name = '6 - Endereços Cadastrados'


class SimuladoModalidade(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return str(self.descricao)

    class Meta:
        verbose_name_plural = '0 - Modalidades'
        verbose_name = '0 - Modalidades'


class SimuladoComponente(models.Model):
    origem_gov = models.CharField(max_length=50)
    origem_crea = models.ManyToManyField(SimuladoModalidade)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.nome)

    class Meta:
        verbose_name_plural = '1 - Componentes'
        verbose_name = '1 - Componentes'


class SimuladoFormacao(models.Model):
    descricao = models.CharField(max_length=50)
    componente_permissao = models.ManyToManyField(SimuladoComponente)

    def __str__(self):
        return str(self.descricao)

    class Meta:
        verbose_name_plural = '2 - Formação'
        verbose_name = '2 - Formação'


class SimuladoResponsaveisTecnicos(models.Model):
    nome = models.CharField(max_length=255)
    formacao = models.OneToOneField(SimuladoFormacao, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name_plural = '3 - Responsáveis Técnicos'
        verbose_name = '3 - Responsáveis Técnicos'


class SimuladoEmpresaCrea(models.Model):
    cnpj = models.CharField(max_length=14, primary_key=True, )
    nome = models.CharField(max_length=255)
    endereco = models.ForeignKey(SimuladoEndereco, on_delete=models.PROTECT)
    endereco_numero = models.PositiveIntegerField()
    endereco_complemento = models.CharField(max_length=50)
    profissionais = models.ManyToManyField(SimuladoResponsaveisTecnicos)
    situacao = models.BooleanField(default=True)

    def __str__(self):
        return str(self.cnpj)

    class Meta:
        verbose_name_plural = '4 - Empresas Cadastradas'
        verbose_name = '4 - Empresas Cadastradas'


class ObrasEmAndamento(models.Model):
    executor = models.CharField(max_length=50)
    fornecedor = models.ForeignKey(SimuladoEmpresaCrea, on_delete=models.PROTECT)
    contrato_numero = models.CharField(max_length=50)
    contrato_valor = models.FloatField()
    componente = models.ForeignKey(SimuladoComponente, on_delete=models.PROTECT)
    analisada = models.BooleanField(default=False)

    def __str__(self):
        return str(self.executor) + ' - ' + str(self.fornecedor)

    class Meta:
        verbose_name_plural = '5 - Obras em Andamento'
        verbose_name = '5 - Obras em Andamento'
