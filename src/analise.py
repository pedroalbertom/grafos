import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import powerlaw

# 1. Carregamento e Preparação dos Dados
df = pd.read_csv('../results/metricas_vertices.csv', sep=';')

# Cálculo do Grau Total (Soma de In e Out para análise de escala livre)
df['GrauTotal'] = df['GrauEntrada'] + df['GrauSaida']

# Filtramos graus zero para não enviesar a análise de Power Law
df_filtered = df[df['GrauTotal'] > 0]

# 2. Métricas Básicas (Confirmação dos dados do Java)
V = 2394385  # Valor oficial do SNAP
E = 5021410  # Valor oficial do SNAP
densidade = E / (V * (V - 1))
grau_medio = (2 * E) / V

print(f"Ordem |V|: {V}")
print(f"Tamanho |E|: {E}")
print(f"Densidade: {densidade:.10f}")
print(f"Grau Médio: {grau_medio:.2f}")

# 3. Visualização da Distribuição de Graus P(k)
fig, ax = plt.subplots(1, 2, figsize=(15, 6))

# Histograma Linear (P(k) em escala normal)
ax[0].hist(df_filtered['GrauTotal'], bins=100, color='royalblue', edgecolor='white', density=True)
ax[0].set_title('Distribuição de Graus P(k) - Escala Linear')
ax[0].set_xlabel('Grau (k)')
ax[0].set_ylabel('Frequência Normalizada')
ax[0].grid(axis='y', alpha=0.3)

# Gráfico Log-Log (Essencial para identificar Escala Livre)
# Calculamos a probabilidade empírica para cada k
counts = df_filtered['GrauTotal'].value_counts(normalize=True).sort_index()
x = counts.index
y = counts.values

ax[1].scatter(x, y, alpha=0.6, s=15, color='darkorange')
ax[1].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_title('Distribuição de Graus P(k) - Escala Log-Log')
ax[1].set_xlabel('Grau (k) - Log')
ax[1].set_ylabel('Frequência P(k) - Log')
ax[1].grid(which='both', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

# 4. Ajuste por Lei de Potência (Power Law Fit)
data = df_filtered['GrauTotal'].values
fit = powerlaw.Fit(data, xmin=1) # O xmin pode ser ajustado automaticamente pelo pacote

print("\n--- Resultados do Ajuste de Lei de Potência ---")
print(f"Gamma (Alpha): {fit.power_law.alpha:.4f}")
print(f"Xmin: {fit.power_law.xmin}")
print(f"Coeficiente D (KS test): {fit.power_law.D:.4f}")

# 5. Comparação de Distribuições (Análise Crítica)
R, p = fit.distribution_compare('power_law', 'lognormal')
print(f"\nComparação Power Law vs Lognormal:")
print(f"Razão de Verossimilhança (R): {R:.4f}")
print(f"p-value: {p:.4f}")

if R > 0 and p < 0.05:
    print("Conclusão: A Lei de Potência é estatisticamente mais provável que a Lognormal.")
else:
    print("Conclusão: Não há evidência forte para descartar a Lognormal frente à Lei de Potência.")