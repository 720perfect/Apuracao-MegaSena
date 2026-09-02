import csv
import random
import string

def gerar_id_alfanumerico():
    letras_numeros = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"AP-{letras_numeros}"

def gerar_apostas_base(quantidade=10, arquivo_saida="apostas.csv"):
    with open(arquivo_saida, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        for _ in range(quantidade):
            id_aposta = gerar_id_alfanumerico()
            numeros = sorted(random.sample(range(1, 61), 6))
            linha = [id_aposta] + numeros
            writer.writerow(linha)

if __name__ == "__main__":
    gerar_apostas_base()