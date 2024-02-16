from database import adicionar_hash, criar_tabela, verificar_existencia_hash
import os
import hashlib

def gerar_hash(arquivo):
    md5 = hashlib.md5()
    with open(arquivo, 'rb') as f:
        conteudo = f.read()
        md5.update(conteudo)
    return md5.hexdigest()

def imprimir_hash():

    criar_tabela()


    OUTPUT_DIR = 'img'
    for nome_arquivo in os.listdir(OUTPUT_DIR):
        if nome_arquivo.endswith('.gif'):
            caminho_arquivo = os.path.join(OUTPUT_DIR, nome_arquivo)
            hash_valor = gerar_hash(caminho_arquivo)

            if verificar_existencia_hash(hash_valor):
                print(f'Arquivo: {nome_arquivo} | Hash: {hash_valor} - Já existente na database')
            else:
                adicionar_hash(hash_valor)
                print(f'Arquivo: {nome_arquivo} | Hash: {hash_valor} - Adicionado a database')

