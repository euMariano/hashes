# baixar_gifs.py
import requests
import os

from utils.constantes import OUTPUT_DIR

def baixar_arquivo(url, endereco):
    resposta = requests.get(url)
    if not resposta.ok:
        resposta.raise_for_status()
        return

    with open(endereco, 'wb') as novo_arquivo:
        novo_arquivo.write(resposta.content)
    print(f'download salvo em {endereco}')

def baixar_gifs(quantidade):
    response = requests.get("https://nekos.life/api/v2/img/hug")

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    for i in range(1, quantidade):
        numero_formatado = str(i).zfill(3)
        url_gif = f'https://cdn.nekos.life/hug/hug_{numero_formatado}.gif'
        try:
            nome_arquivo = os.path.join(OUTPUT_DIR, f'hug{i}.gif')
            if not response.ok:
                print(f'erro ao realizar download do gif {i}. Código do status: {response.status_code}')
                continue

            baixar_arquivo(url_gif, nome_arquivo)
        except requests.exceptions.RequestException as e:
            print(f'erro ao baixar gif {i}. {e}')
    print("fim do download dos gifs\n")
