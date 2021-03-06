# Generated by Django 2.2.4 on 2019-08-17 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SimuladoComponente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origem_gov', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '1 - Componentes',
                'verbose_name_plural': '1 - Componentes',
            },
        ),
        migrations.CreateModel(
            name='SimuladoEndereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco_descricao', models.CharField(max_length=255)),
                ('endereco_numero', models.PositiveIntegerField()),
                ('endereco_cep', models.IntegerField()),
                ('bairro', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': '6 - Endereços Cadastrados',
                'verbose_name_plural': '6 - Endereços Cadastrados',
            },
        ),
        migrations.CreateModel(
            name='SimuladoFormacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('componente_permissao', models.ManyToManyField(to='app_login.SimuladoComponente')),
            ],
            options={
                'verbose_name': '2 - Formação',
                'verbose_name_plural': '2 - Formação',
            },
        ),
        migrations.CreateModel(
            name='SimuladoModalidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': '0 - Modalidades',
                'verbose_name_plural': '0 - Modalidades',
            },
        ),
        migrations.CreateModel(
            name='SimuladoResponsaveisTecnicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('formacao', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='app_login.SimuladoFormacao')),
            ],
            options={
                'verbose_name': '3 - Responsáveis Técnicos',
                'verbose_name_plural': '3 - Responsáveis Técnicos',
            },
        ),
        migrations.CreateModel(
            name='SimuladoEmpresaCrea',
            fields=[
                ('cnpj', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('endereco_numero', models.PositiveIntegerField()),
                ('endereco_complemento', models.CharField(max_length=50)),
                ('situacao', models.BooleanField(default=True)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_login.SimuladoEndereco')),
                ('profissionais', models.ManyToManyField(to='app_login.SimuladoResponsaveisTecnicos')),
            ],
            options={
                'verbose_name': '4 - Empresas Cadastradas',
                'verbose_name_plural': '4 - Empresas Cadastradas',
            },
        ),
        migrations.AddField(
            model_name='simuladocomponente',
            name='origem_crea',
            field=models.ManyToManyField(to='app_login.SimuladoModalidade'),
        ),
        migrations.CreateModel(
            name='ObrasEmAndamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('executor', models.CharField(max_length=50)),
                ('contrato_numero', models.CharField(max_length=50)),
                ('contrato_valor', models.FloatField()),
                ('analisada', models.BooleanField(default=False)),
                ('componente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_login.SimuladoComponente')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_login.SimuladoEmpresaCrea')),
            ],
            options={
                'verbose_name': '5 - Obras em Andamento',
                'verbose_name_plural': '5 - Obras em Andamento',
            },
        ),
    ]
