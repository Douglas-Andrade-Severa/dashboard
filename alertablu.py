import requests
from bs4 import BeautifulSoup #pip install beautifulsoup
from io import StringIO
import pandas as pd

url = 'https://alertablu.blumenau.sc.gov.br/d/'
colunas = ['Estação','Hora da leitura','24h','168h']
arquivo = 'alertablu.cvs'

def main():
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()

        soup  = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')
        table = StringIO(str(table))

        df = pd.read_html(table, thousands='.', decimal=',')[0]
        df = df[colunas]

        df.to_csv(arquivo, header=False, index=False, mode='a')

    except Exception as e:
        print(f'Erro: {e}')

if __name__ == '__main__':
    main()
