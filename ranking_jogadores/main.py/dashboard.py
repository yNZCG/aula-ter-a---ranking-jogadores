from database import get_import_dates, get_ranking_by_date

def show_dashboard():
    datas = get_import_dates()

    if not datas:
        print("Nenhum dado importado ainda.")
        return

    print("\n=== Listas Disponíveis ===")
    for idx, data in enumerate(datas):
        print(f"{idx + 1}. {data}")

    try:
        opcao = int(input("\nEscolha uma lista para exibir (número): "))
        if opcao < 1 or opcao > len(datas):
            raise ValueError("Opção inválida.")
    except Exception as e:
        print("Entrada inválida.")
        return

    data_escolhida = datas[opcao - 1]
    ranking = get_ranking_by_date(data_escolhida)

    print(f"\n=== Ranking - {data_escolhida} ===")
    for idx, (nome, nivel, pontuacao) in enumerate(ranking, start=1):
        destaque = ""
        if idx == 1:
            destaque = "🥇"
        elif idx == 2:
            destaque = "🥈"
        elif idx == 3:
            destaque = "🥉"

        print(f"{idx}. {nome} - Nível: {nivel} - Pontuação: {pontuacao} {destaque}")
