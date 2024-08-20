import numpy as np
import random
import matplotlib.pyplot as plt
from tkinter import *

data = []
k = 0

def quantcentroides():
    global k
    k = int(entry.get())
    while (k <= 0):
        texto_centroides["text"] = "Quantidade inválida, digite um valor maior do que 0!"
        k = int(entry.get())
    texto_centroides["text"] = "Quantidade lida com sucesso!"
    return k


# função para gerar dados aleatorios
def geraraleatorio():
    global data
    data = np.random.rand(100, 2)
    return data


def kmeans(k):
    global data
    centroids = random.sample(list(data), k)
    
    while True:
        # Atribuição dos pontos aos centróides mais próximos
        clusters = [[] for _ in range(k)]
        for point in data:
            distances = [np.linalg.norm(point - c) for c in centroids]
            cluster_id = np.argmin(distances)
            clusters[cluster_id].append(point)
        
        # Cálculo dos novos centróides
        new_centroids = [np.mean(cluster, axis=0) for cluster in clusters]
        
        # Verificação de convergência
        if all((new_centroids[i] == centroids[i]).all() for i in range(k)):
            break
        else:
            centroids = new_centroids
    
    return clusters, centroids


data = geraraleatorio() # Gerando dados aleatórios

#menu 
root = Tk()
root.title("KMeans")
root.geometry("280x280")

texto_menu = Label(root, font=('', 15), text="Menu")
texto_menu.pack(pady=5)

texto_final = Label(root, text="")
texto_final.pack(pady=10)

#Informar a quantidade de centroides 
texto_centroides = Label(root, text="Informe a quantidade de centróides: ")
texto_centroides.pack(pady=9)

entry = Entry(root, bd=3, cursor="")
entry.pack()

botao_ler = Button(root, text="confirmar", command=lambda: kmeans(quantcentroides()))
botao_ler.pack(pady=9)

botao_ler = Button(root, text="grafico", command=lambda: kmeans(grafico()))
botao_ler.pack(pady=9)

colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'orange'] # Definindo cores

def grafico():
    global k
    clusters, centroids = kmeans(k) # Executando o algoritmo K-Means com k=x(max 7)
    fig, ax = plt.subplots()
    for i, cluster in enumerate(clusters):
        cluster = np.array(cluster)
        ax.scatter(cluster[:,0], cluster[:,1], c=colors[i], label='Cluster {}'.format(i+1))
    ax.scatter(np.array(centroids)[:,0], np.array(centroids)[:,1], c='k', marker='x', s=100, label='Centroids')
    ax.legend()
    plt.show()

root.mainloop()
