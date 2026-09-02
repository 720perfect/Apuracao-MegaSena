import csv
import random
import string
import sys

def gerar_id_alfanumerico():
    letras_numeros = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"AP-{letras_numeros}"

def validar_quantidade_numeros(numeros):
    return 6 <= len(numeros) <= 15

def gerar_apostas(quantidade, arquivo_saida="apostas.csv"):
    with open(arquivo_saida, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        linhas_geradas = 0
        while linhas_geradas < quantidade:
            id_aposta = gerar_id_alfanumerico()
            
            # Gera apostas validas (de 6 a 15 dezenas)
            qtd_dezenas = random.randint(6, 15)
            numeros = sorted(random.sample(range(1, 61), qtd_dezenas))
            
            if validar_quantidade_numeros(numeros):
                linha = [id_aposta] + numeros
                writer.writerow(linha)
                linhas_geradas += 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso correto: python gerador.py <quantidade_de_linhas>")
        sys.exit(1)
        
    try:
        qtd_linhas = int(sys.argv[1])
        if qtd_linhas <= 0:
            raise ValueError
    except ValueError:
        print("Erro: A quantidade de linhas deve ser um número inteiro positivo.")
        sys.exit(1)
        
    gerar_apostas(qtd_linhas)
    print(f"Sucesso: {qtd_linhas} linhas geradas no arquivo 'apostas.csv'.")