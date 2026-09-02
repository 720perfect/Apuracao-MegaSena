import csv
import random
import string

def gerar_id_alfanumerico():
    letras_numeros = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"AP-{letras_numeros}"

def validar_quantidade_numeros(numeros):
    """Valida se a aposta contem entre 6 e 15 numeros."""
    return 6 <= len(numeros) <= 15

def gerar_apostas_com_validacao(quantidade=10, arquivo_saida="apostas.csv"):
    with open(arquivo_saida, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        linhas_geradas = 0
        while linhas_geradas < quantidade:
            id_aposta = gerar_id_alfanumerico()
            
            # Gera aleatoriamente uma quantidade de dezenas (pode incluir invalidas para teste)
            qtd_dezenas = random.randint(5, 16) 
            numeros = sorted(random.sample(range(1, 61), qtd_dezenas))
            
            # Aplica a regra de validacao da Mega-Sena
            if validar_quantidade_numeros(numeros):
                linha = [id_aposta] + numeros
                writer.writerow(linha)
                linhas_geradas += 1
            else:
                print(f"Linha descartada por violar as regras: {numeros}")

if __name__ == "__main__":
    gerar_apostas_com_validacao()