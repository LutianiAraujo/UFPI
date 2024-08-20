import math
import random
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

k = 0
data = []


def randomico():
  global data
  x = [random.uniform(0, 1) for i in range(200)]
  y = [random.uniform(0, 1) for i in range(200)]
  data = list(zip(x, y))
  texto_final["text"] = "Dados gerados com sucesso!"
  return data


def ler():
  global k
  k = int(entry.get())
  while (k <= 0):
    texto_final[
      "text"] = "Quantidade invalida, digite um valor maior do que 0!"
    k = entry.get()
  texto_final["text"] = "Quantidade lida com sucesso!"
  return k


def divisao_euclidiana(x, y):
  return math.sqrt(sum([(a - b)**2 for a, b in zip(x, y)]))


def lerarqv():
  global data
  with open("input.txt", 'r') as arquivo:
    for line in arquivo:
      line = line.replace("\n", "").split(',')
      x = float(line[0])
      y = float(line[1])
      tupla = (x, y)
      data.append(tupla)


def gerar():
  global k
  global data

  try:
    centroides = random.sample(data, k)

    #vetor para cada ponto
    vetor = [0] * len(data)
    while (True):
      #atribuir cada ponto ao cluster mais próximo
      for j, point in enumerate(data):
        distancias = [
          divisao_euclidiana(point, centroide) for centroide in centroides
        ]
        cluster = distancias.index(min(distancias))
        vetor[j] = cluster

      #atualizar a posição
      #Criando uma lista dos pontos mais proximos para cada um dos centroides:
      old_centroids = centroides[:]
      clusters = [[] for _ in range(k)]
      for j, point in enumerate(data):
        clusters[vetor[j]].append(point)

      for c in range(k):
        if len(clusters[c]) != 0:
          centroides[c] = tuple(sum(x) / len(x) for x in zip(*clusters[c]))

      #verificar se houve mudanças
      if set(old_centroids) == set(centroides):
        break

    #Garantindo que as cores base aparecam primeiro/ 148 centroides possiveis:
    colors0 = list(mcolors.CSS4_COLORS)
    colors = [
      'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'black', 'pink'
    ]
    for iterab in colors:
      colors0.remove(iterab)
    for iterab in colors0:
      colors.append(iterab)

    #plotar os resultados
    for i, cluster in enumerate(clusters):
      x, y = zip(*cluster)
      plt.scatter(x, y, color=colors[i])
      plt.scatter(centroides[i][0],
                  centroides[i][1],
                  marker='*',
                  color='black',
                  s=100)

    plt.show()
    texto_final["text"] = ""
  except:
    texto_final["text"] = "Faltam dados!"


##Menu-------------------------------------------------------------------
root = Tk()
root.title("KMeans")
root.geometry("320x320")

texto_menu = Label(root, font=('', 15), text="Menu kmeans")
texto_menu.pack(pady=5)

texto_final = Label(root, text="")
texto_final.pack(pady=10)

botao = Button(root, text="Gerar dados aleatórios", command=randomico)
botao.pack()

##Read-------------------------------------------------------------------
#Arquivo
botao_arqv = Button(root,
                    text="          Ler arquivo          ",
                    command=lerarqv)
botao_arqv.pack(pady=15)

##Show-------------------------------------------------------------------
botao_mostrar = Button(root,
                       text="        Gerar gráfico        ",
                       command=gerar)
botao_mostrar.pack()

##Read-------------------------------------------------------------------
texto_ler = Label(root, text="Informe a quantidade de centróides: ")
texto_ler.pack(pady=9)

entry = Entry(root, bd=3, cursor="heart")
entry.pack()

botao_ler = Button(root, text="confirmar", command=ler)
botao_ler.pack(pady=9)

root.mainloop()