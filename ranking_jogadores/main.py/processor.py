import csv
from database import setup_database, insert_player

def process_csv(path):
    setup_database()
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader, start=2):  # linha 2 em diante
            try:
                nome = row['nome']
                nivel = int(row['nivel'])
                pontuacao = float(row['pontuacao'])

                insert_player(nome, nivel, pontuacao)
            except Exception as e:
                with open('erros.log', 'a', encoding='utf-8') as log:
                    log.write(f"Linha {i}: {row} - Erro: {str(e)}\n")
