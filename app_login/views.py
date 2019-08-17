from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
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
    return render(request, 'app_login/inicial.html', {'html': data})
