# Generar CSV mensuales de ventas para 2026
import pandas as pd
import numpy as np

# Cargar el dataset base de mayo
df_base = pd.read_csv("/workspaces/semana_tragica/data/ventas_mayo_2026.csv")

# Meses del año
meses = [
    ("enero", 1), ("febrero", 2), ("marzo", 3), ("abril", 4), ("mayo", 5),
    ("junio", 6), ("julio", 7), ("agosto", 8), ("septiembre", 9), ("octubre", 10),
    ("noviembre", 11), ("diciembre", 12)
]

# Función para variar los datos
def variar_datos(df, mes_num):
    df_var = df.copy()
    # Cambiar fecha al mes correspondiente (usar 2026)
    df_var['fecha'] = df_var['fecha'].str.replace(r'2025-\d{2}-', f'2026-{mes_num:02d}-', regex=True)
    # Variar importe con factor aleatorio
    factor = np.random.uniform(0.8, 1.2, size=len(df_var))
    df_var['importe'] = df_var['importe'] * factor
    # Recalcular unidades si es necesario, pero mantener simple
    return df_var

# Generar y guardar CSV para cada mes
for nombre_mes, mes_num in meses:
    df_mes = variar_datos(df_base, mes_num)
    filename = f"/workspaces/semana_tragica/data/ventas_{nombre_mes}_2026.csv"
    df_mes.to_csv(filename, index=False)
    print(f"Generado: {filename}")

print("Todos los CSV mensuales han sido generados.")