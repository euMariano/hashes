# importação
import sys
from baixar_gifs import baixar_gifs
from hashes import imprimir_hash


#chamada de função
if __name__ == "__main__":
    quantidade = int(sys.argv[-1])
    if quantidade == 1:
        quantidade += 1
    baixar_gifs(quantidade)
    imprimir_hash()
