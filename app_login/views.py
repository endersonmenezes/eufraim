import requests
from bs4 import BeautifulSoup
from .models import Ocorrencia, SimuladoFornecedor
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def inicial(request):
    contadores = {
        'total': Ocorrencia.objects.filter(status=0).count(),
        'ocorrencia': Ocorrencia.objects.filter(status=1).count(),
        'naoocorrencia': Ocorrencia.objects.filter(status=2).count()
    }
    return render(request, 'app_login/inicial.html', {'contadores': contadores})


def ocorrencias(request):
    if request.GET:
        try:
            id = int(request.GET['id'])
        except:
            messages.error(request, 'Não foi possível concluir sua solicitação, pois não encontramos '
                                    'nenhuma ocorrencia!')
            return render(request, 'app_login/ocorrencias_ficha.html', )
        ocorrencia = Ocorrencia.objects.filter(id=int(request.GET['id']))
        if not ocorrencia:
            messages.error(request, 'Não foi possível concluir sua solicitação, pois não encontramos '
                                    'nenhuma ocorrencia com esse ID!')
            return render(request, 'app_login/ocorrencias_ficha.html', )
        ocorrencia = Ocorrencia.objects.get(id=int(request.GET['id']))
        ## TENTAR PEGAR CONTRATO
        # if ocorrencia.executor == 'Apucarana':
        #     dados = ocorrencia.contrato_numero.split('/')
        #     url = 'http://portal.apucarana.pr.gov.br/pronimtb/index.asp?acao=1&item=1&visao=2&contrato='+\
        #           str(dados[0])+'&anocontrato='+str(dados[1])+'&dsTipoContrato=Contrato'
        #     page = requests.get(url)
        #     soup = BeautifulSoup(page.text, 'html.parser')
        #     conteudo = soup.find('div', {'id': 'conteudo'})
        #     print(soup)
        ## TENTAR PEGAR CONTRATO
        return render(request, 'app_login/ocorrencias_ficha.html', {'ocorrencia': ocorrencia,})
    return render(request, 'app_login/ocorrencias.html',)


def ativador_spiders(request):
    data = []
    url = 'http://200.195.150.93/dados_site_paranacidade/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table', attrs={'class': 'table table-striped'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        foto = row.find_all('a')
        linkfoto = str(foto)
        linkfoto = linkfoto.split('"')
        cols = [ele.text.strip() for ele in cols]
        array = [ele for ele in cols if ele]
        array.append(url + linkfoto[1])
        data.append(array)

    for licitacao in data:
        ocorrencia = Ocorrencia.objects.filter(fornecedor__cnpj=str(licitacao[3]),
                                               contrato_numero=str(licitacao[6]))
        if not ocorrencia:
            empresa = SimuladoFornecedor.objects.filter(cnpj=str(licitacao[3]))
            if not empresa:
                empresa = SimuladoFornecedor.objects.create(
                    cnpj=str(licitacao[3]),
                    nome=str(licitacao[4]),
                )
                empresa.save()
            else:
                empresa = SimuladoFornecedor.objects.get(cnpj=str(licitacao[3]))
            tmp_contrato_lote = int(licitacao[2])
            tmp_executor = str(licitacao[0])
            tmp_url = str(licitacao[-1])
            tmp_url = tmp_url.replace('amp;', '')
            tmp_contrato_projeto = int(licitacao[1])
            tmp_contrato_numero = str(licitacao[6])
            tmp_contrato_valor = str(licitacao[8])
            tmp_contrato_valor = tmp_contrato_valor.replace('.', '')
            tmp_contrato_valor = tmp_contrato_valor.replace(',', '.')
            tmp_contrato_valor = float(tmp_contrato_valor)
            tmp_componente = str(licitacao[9])
            ocorrencia = Ocorrencia.objects.create(
                fornecedor=empresa,
                executor=tmp_executor,
                contrato_projeto=tmp_contrato_projeto,
                contrato_lote=tmp_contrato_lote,
                contrato_numero=tmp_contrato_numero,
                componente=tmp_componente,
                contrato_valor=tmp_contrato_valor,
                fotos=tmp_url,
            )
            ocorrencia.save()

    return JsonResponse({'response': 200})
