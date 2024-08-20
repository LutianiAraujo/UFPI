import matplotlib.pyplot as plt

def minha_funcao_hash(chave):
    return ord(chave[0].lower()) % 17

tabela_hash = [[] for _ in range(17)]

with open("alunosEd.txt", "r") as arquivo:
    for nome in arquivo:
        posicao = minha_funcao_hash(nome)
        tabela_hash[posicao].append(nome.strip())

ocorrencias = [len(tabela_hash[i]) for i in range(17)]

letras = [str(i) for i in range(17)]
plt.bar(letras, ocorrencias)
plt.title("Distribuição de nomes pelo início da primeira letra")
plt.xlabel("Posição na tabela hash")
plt.ylabel("Número de nomes")
plt.show()