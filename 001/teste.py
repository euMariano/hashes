import requests
import os

response = requests.get("https://nekos.life/api/v2/img/hug")
json_url = response.json()
json_data = json_url.get('url')

def baixar_arquivo(url, endereco):
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print(f'download salvo em {endereco}')
    else:
        resposta.raise_for_status()

if __name__ == "__main__":
    for i in range(1, 21):
        BASE_URL = 'https://cdn.nekos.life/hug/hug_{i}.gif'
        OUTPUT_DIR = "img"
        try:
            numero_formatado = str(i).zfill(3)
            url_gif = BASE_URL.format(i=numero_formatado)
            nome_arquivo = os.path.join(OUTPUT_DIR, f'hug{i}.gif')
            if response.status_code == requests.codes.OK:
                baixar_arquivo(url_gif, nome_arquivo)
            else:
                print(f'erro ao realizar download do gif {i}. Código do status: {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f'erro ao baixar gif {i}. {e}')
    print("fim do download dos gifs")