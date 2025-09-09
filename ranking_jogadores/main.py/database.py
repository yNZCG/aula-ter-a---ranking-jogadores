import sqlite3
from datetime import datetime

def create_connection():
    return sqlite3.connect("ranking.db")

def setup_database():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rankings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            nivel INTEGER NOT NULL,
            pontuacao REAL NOT NULL,
            data_importacao TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_player(nome, nivel, pontuacao):
    conn = create_connection()
    cursor = conn.cursor()

    data_importacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute('''
        INSERT INTO rankings (nome, nivel, pontuacao, data_importacao)
        VALUES (?, ?, ?, ?)
    ''', (nome, nivel, pontuacao, data_importacao))

    conn.commit()
    conn.close()

def get_import_dates():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT DISTINCT data_importacao FROM rankings ORDER BY data_importacao DESC')
    datas = cursor.fetchall()
    conn.close()
    return [d[0] for d in datas]

def get_ranking_by_date(data_importacao):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT nome, nivel, pontuacao FROM rankings
        WHERE data_importacao = ?
        ORDER BY pontuacao DESC
    ''', (data_importacao,))

    ranking = cursor.fetchall()
    conn.close()
    return ranking
