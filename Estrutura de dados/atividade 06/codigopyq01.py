import matplotlib.pyplot as plt

# Inicializa a tabela hash com listas vazias
tabela_hash = {}
for letra in "abcdefghijklmnopqrstuvwxyz":
    tabela_hash[letra] = []

# Lê o arquivo de nomes e adiciona cada nome à lista correspondente na tabela hash
with open("alunosED.txt", "r") as arquivo:
    for nome in arquivo:
        primeira_letra = nome[0].lower()
        tabela_hash[primeira_letra].append(nome.strip())

# Conta o número de nomes começando com cada letra do alfabeto
ocorrencias = []
for letra in "abcdefghijklmnopqrstuvwxyz":
    ocorrencias.append(len(tabela_hash[letra]))

# Plota o histograma
letras = [letra.upper() for letra in "abcdefghijklmnopqrstuvwxyz"]
plt.bar(letras, ocorrencias)
plt.title("Distribuição de nomes pelo início da primeira letra")
plt.xlabel("Letra")
plt.ylabel("Número de nomes")
plt.show()