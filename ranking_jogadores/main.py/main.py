from processor import process_csv
from dashboard import show_dashboard

def main():
    print("=== Sistema de Ranking de Jogadores ===")
    process_csv('jogadores.csv')
    show_dashboard()

if __name__ == "__main__":
    main()
