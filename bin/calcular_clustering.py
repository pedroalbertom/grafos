import pandas as pd
import networkx as nx
import random
import time

print("1. Lendo o dataset...")
df = pd.read_csv('data/WikiTalk.txt', sep='\t', comment='#', names=['FromNodeId', 'ToNodeId'])
print("2. Construindo o grafo direcionado...")
G = nx.from_pandas_edgelist(df, 'FromNodeId', 'ToNodeId', create_using=nx.DiGraph())
print(f"Grafo criado! Vértices: {G.number_of_nodes()} | Arestas: {G.number_of_edges()}")
tamanho_amostra = 10000
print(f"3. Sorteando {tamanho_amostra} vértices para amostragem...")
todos_os_nos = list(G.nodes())
nos_amostra = random.sample(todos_os_nos, tamanho_amostra)
print("4. Calculando o clustering médio (isso pode levar alguns segundos/minutos)...")
inicio = time.time()
clustering_medio = nx.average_clustering(G, nodes=nos_amostra)
fim = time.time()

print("-" * 40)
print(f"Coeficiente de Agrupamento Médio (Amostra): {clustering_medio:.6f}")
print(f"Tempo de execução: {(fim - inicio):.2f} segundos")
print("-" * 40)