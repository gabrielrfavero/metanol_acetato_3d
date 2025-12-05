import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from io import StringIO
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = "browser"

# ----------------------------------------
# 1) Ler o arquivo (vírgula decimal → ponto)
# ----------------------------------------
with open('dados_PTxy.txt', 'r', encoding='utf-8') as f:
    raw = f.read()

raw = raw.replace(',', '.')  # troca vírgula por ponto
df = pd.read_csv(StringIO(raw), sep=r'\s+')

# Colunas
P = df["P"].to_numpy()
T = df["T"].to_numpy()
x1 = df["x1"].to_numpy()
y1 = df["y1"].to_numpy()

# ----------------------------------------
# 2) Criar grades (X = composição, Y = T)
# ----------------------------------------
x_lin = np.linspace(0, 1, 80)
T_lin = np.linspace(T.min(), T.max(), 80)

X_grid, T_grid = np.meshgrid(x_lin, T_lin)

# ----------------------------------------
# 3) Interpolar P(x, T) para bolha e orvalho
# ----------------------------------------
# Bolha: usa x1
pts_liq = np.column_stack((x1, T))
P_liq_grid = griddata(pts_liq, P, (X_grid, T_grid), method='cubic')

# Orvalho: usa y1
pts_vap = np.column_stack((y1, T))
P_vap_grid = griddata(pts_vap, P, (X_grid, T_grid), method='cubic')

# ----------------------------------------
# 4) Montar figura 3D no Plotly
# ----------------------------------------
fig = go.Figure()

# Superfície de BOLHA (líquido) – azul
fig.add_surface(
    x=X_grid,
    y=T_grid,
    z=P_liq_grid,
    colorscale=[[0, 'rgb(0, 90, 255)'], [1, 'rgb(0, 90, 255)']],
    opacity=0.55,
    showscale=False,
    name="Bolha (x₁)",
    showlegend=True
)

# Superfície de ORVALHO (vapor) – vermelha
fig.add_surface(
    x=X_grid,
    y=T_grid,
    z=P_vap_grid,
    colorscale=[[0, 'rgb(230, 40, 40)'], [1, 'rgb(230, 40, 40)']],
    opacity=0.55,
    showscale=False,
    name="Orvalho (y₁)",
    showlegend=True
)

# ----------------------------------------
# 5) Pontos experimentais (opcional – bem suaves)
#    Se achar poluído, é só comentar esses dois blocos.
# ----------------------------------------
fig.add_trace(go.Scatter3d(
    x=x1,
    y=T,
    z=P,
    mode='markers',
    marker=dict(size=3, color='rgba(0,0,120,0.4)'),
    name='Dados – líquido'
))

fig.add_trace(go.Scatter3d(
    x=y1,
    y=T,
    z=P,
    mode='markers',
    marker=dict(size=3, color='rgba(150,0,0,0.4)', symbol='x'),
    name='Dados – vapor'
))

# ----------------------------------------
# 6) Layout: eixos, títulos, estilo
# ----------------------------------------
fig.update_layout(
    title="Envelope P–T–x/y – UNIQUAC",
    scene=dict(
        xaxis_title="Composição (x₁ / y₁)",
        yaxis_title="Temperatura (K)",
        zaxis_title="Pressão (atm)",
    ),
    legend=dict(
        x=0.02, y=0.98,
        bgcolor='rgba(255,255,255,0.7)'
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

fig.show()

fig.write_image("grafico_PTxy.png", scale=3)
fig.write_html("grafico_PTxy_interativo.html")

