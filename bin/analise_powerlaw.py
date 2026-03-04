import pandas as pd
import powerlaw

df = pd.read_csv('results/metricas_vertices.csv', sep=';')

for tipo in ['GrauEntrada', 'GrauSaida']:
    dados = df[df[tipo] > 0][tipo].values
    fit = powerlaw.Fit(dados, discrete=True, verbose=False)
    
    print(f"\n--- ANÁLISE: {tipo} ---")
    print(f"Gamma (Alpha): {fit.power_law.alpha:.4f}")
    print(f"Xmin:          {fit.power_law.xmin}")
    print(f"KS (D):        {fit.power_law.D:.4f}")
    print(f"N na Cauda:    {len(fit.power_law.data)}")
    
    R, p = fit.distribution_compare('power_law', 'lognormal')
    print(f"p-value (vs Lognormal): {p:.4f}")