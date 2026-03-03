import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('results/metricas_vertices.csv', sep=';')
limite_k = 40

fig, ax = plt.subplots(1, 2, figsize=(15, 6))

# Histogramas para In e Out
for i, tipo in enumerate(['GrauEntrada', 'GrauSaida']):
    dados_focados = df[(df[tipo] > 0) & (df[tipo] < limite_k)][tipo]
    
    ax[i].hist(dados_focados, bins=limite_k, color='royalblue', edgecolor='black', alpha=0.7)
    ax[i].axvline(dados_focados.mean(), color='red', linestyle='dashed', label=f'Média: {dados_focados.mean():.2f}')
    
    ax[i].set_title(f'Distribuição de {tipo} (k < {limite_k})')
    ax[i].set_xlabel('Grau (k)')
    ax[i].set_ylabel('Frequência')
    ax[i].legend()

plt.tight_layout()
plt.show()