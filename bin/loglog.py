import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import powerlaw

df = pd.read_csv('results/metricas_vertices.csv', sep=';')

fig, ax = plt.subplots(1, 2, figsize=(15, 6))

for i, tipo in enumerate(['GrauEntrada', 'GrauSaida']):
    dados = df[df[tipo] > 0][tipo].values
    
    # Ajuste para pegar Gamma e Xmin
    fit = powerlaw.Fit(dados, discrete=True, xmin=1, verbose=False)
    gamma = fit.power_law.alpha
    
    # Cálculo manual da reta
    bins, counts = np.unique(dados, return_counts=True)
    pk = counts / counts.sum()
    C = pk[0] / (bins[0]**-gamma)
    reta_teorica = C * (bins**-gamma)
    
    # Plotagem
    ax[i].scatter(bins, pk, color='darkorange', alpha=0.6, s=10, label='Dados Reais')
    ax[i].plot(bins, reta_teorica, color='red', linestyle='--', label=f'Ajuste ($\gamma = {gamma:.2f}$)')
    
    ax[i].set_xscale('log')
    ax[i].set_yscale('log')
    ax[i].set_title(f'Log-Log: {tipo}')
    ax[i].set_xlabel('k (Log)')
    ax[i].set_ylabel('P(k) (Log)')
    ax[i].legend()

plt.tight_layout()
plt.show()