from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Ocorrencia, SimuladoFornecedor
# Create your views here.


def inicial(request):
    data = []
    page = requests.get('http://200.195.150.93/dados_site_paranacidade/')
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table', attrs={'class': 'table table-striped'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

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
            tmp_contrato_projeto = int(licitacao[1])
            tmp_contrato_numero = str(licitacao[6])
            tmp_contrato_valor = str(licitacao[8])
            tmp_contrato_valor = tmp_contrato_valor.replace('.', '')
            tmp_contrato_valor = tmp_contrato_valor.replace(',', '.')
            tmp_contrato_valor = float(tmp_contrato_valor)
            tmp_componente = str(licitacao[9])
            tmp_fotos_url = str(licitacao[10])
            ocorrencia = Ocorrencia.objects.create(
                fornecedor=empresa,
                contrato_projeto=tmp_contrato_projeto,
                contrato_lote=tmp_contrato_lote,
                contrato_numero=tmp_contrato_numero,
                componente=tmp_componente,
                contrato_valor=tmp_contrato_valor,
                fotos=tmp_fotos_url,
            )
            ocorrencia.save()

    return render(request, 'app_login/inicial.html', {'html': data})
