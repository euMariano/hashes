import sqlite3
import os

DB_FILE = 'hashes.db'

def criar_tabela():
    conn =sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS imagens (id INTEGER PRIMARY KEY AUTOINCREMENT,hash TEXT)')
    conn.commit()
    conn.close()

def verificar_existencia_hash(hash):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM imagens WHERE hash = ?', (hash,))
    resultado = cursor.fetchone()

    conn.close
    return resultado is not None

def adicionar_hash(hash):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute('INSERT INTO imagens (hash) VALUES (?)', (hash,))
    conn.commit()
    conn.close()