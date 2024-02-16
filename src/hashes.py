from database import adicionar_hash, criar_tabela, hash_existe
import os
import hashlib

from utils.constantes import OUTPUT_DIR

def gerar_hash(arquivo):
    md5 = hashlib.md5()
    with open(arquivo, 'rb') as f:
        conteudo = f.read()
        md5.update(conteudo)
    return md5.hexdigest()

def imprimir_hash():
    criar_tabela()

    for nome_arquivo in os.listdir(OUTPUT_DIR):
        if nome_arquivo.endswith('.gif'):
            caminho_arquivo = os.path.join(OUTPUT_DIR, nome_arquivo)
            hash_valor = gerar_hash(caminho_arquivo)

            if not hash_existe(hash_valor):
                adicionar_hash(hash_valor)
                print(f'Arquivo: {nome_arquivo} | Hash: {hash_valor} - Adicionado a database')

            print(f'Arquivo: {nome_arquivo} | Hash: {hash_valor} - Já existente na database')

