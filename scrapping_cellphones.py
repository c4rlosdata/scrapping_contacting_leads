import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def buscar_telefones_guia_mais(url_base,setor ,num_paginas=5):
    contatos = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    }

    for pagina in range(0, num_paginas):
        # Construa a URL para cada página de resultados
        url = f"{url_base}{setor}&p={pagina}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar todos os elementos que contêm os números de telefone
        for div in soup.find_all('div', class_='col mr-md-2'):
            # Encontre o link com o telefone
            link = div.find('a', href=True, class_='btn btn-block btn-gray text-black mr-2')
            if link and 'tel:' in link['href']:
                telefone = link['href'].replace('tel:', '')
                contatos.append({'celular': '55'+telefone})
                print(f"Telefone encontrado: 55{telefone}")  # Para depuração

        # Pausa para evitar bloqueios do servidor
        time.sleep(2)

    # Salvar os dados em um arquivo Excel
    df = pd.DataFrame(contatos)
    df.to_excel("celulares_python.xlsx", index=False)
    print("Arquivo Excel 'celulares_python.xlsx' salvo com sucesso!")

# Uso da função
url_base = "https://www.guiamais.com.br/encontre?searchbox=true&what="
buscar_telefones_guia_mais(url_base,setor='alimentos', num_paginas=6)
