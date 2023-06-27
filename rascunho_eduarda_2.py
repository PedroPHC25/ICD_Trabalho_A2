import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, ColorBar
from bokeh.transform import linear_cmap, log_cmap
from bokeh.palettes import Blues256
'''
#1
 
# Leitura do arquivo CSV
data = pd.read_csv("World Energy Consumption.csv")

x = data['population']  # Selecionar a coluna 'population'
y = data['gdp']  # Selecionar a coluna 'gdp'
source = ColumnDataSource(dict(x=x, y=y))

def make_plot(mapper, palette):
    cmap = log_cmap(field_name="x", palette=palette, low=min(x), high=max(x))
    axis_type = "log"  # Definir a escala logarítmica

    p = figure(title=f"{palette} with {mapper.__name__}", toolbar_location=None, tools="", x_axis_type=axis_type, y_axis_type=axis_type)

    r = p.scatter('x', 'y', alpha=0.8, source=source, color=cmap)

    color_bar = ColorBar(color_mapper=cmap['transform'], location=(0, 0))
    p.add_layout(color_bar, 'right')

    return p

# Configurar a saída para um arquivo HTML
output_file("grafico.html")

# Chamar a função make_plot com os parâmetros desejados
p = make_plot(log_cmap, Blues256)

# Exibir o gráfico
show(p)
'''

import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Whisker
from bokeh.palettes import Category10_10

# Leitura do arquivo CSV
data = pd.read_csv("World Energy Consumption.csv")

# Ordenar os países pelo GDP em ordem decrescente e selecionar os 10 países com maior GDP (exceto o primeiro lugar)
top_countries = data.nlargest(11, 'gdp')[1:11]
countries = top_countries['country'].tolist()

print(countries)
'''
# Filtrar os dados apenas para os países selecionados
filtered_data = data[data['country'].isin(countries)]

# Criar uma fonte de dados (ColumnDataSource)
source = ColumnDataSource(filtered_data)

# Configurar o gráfico
p = figure(x_range=countries, title="Variação do consumo de energia eólica (TWh) ao longo dos anos",
           x_axis_label="Países", y_axis_label="Variação do consumo de energia eólica (TWh)")

# Agrupar os dados por país e calcular os quartis (quantiles) para o gráfico de caixa
groups = filtered_data.groupby('country')
q1 = groups['wind_cons_change_twh'].quantile(0.25)
q2 = groups['wind_cons_change_twh'].quantile(0.5)
q3 = groups['wind_cons_change_twh'].quantile(0.75)

# Criar listas para os segmentos (Whisker)
top = []
bottom = []
x = []

# Preencher as listas com os valores dos segmentos
for country in countries:
    top.append(q3[country])
    bottom.append(q1[country])
    x.append(country)

# Configurar os segmentos (Whisker) no gráfico
p.segment(x, top, x, q3, line_width=2, line_color='black')
p.segment(x, bottom, x, q1, line_width=2, line_color='black')

# Criar listas para as caixas
top_box = []
bottom_box = []

# Preencher as listas com os valores das caixas
for country in countries:
    top_box.append(q2[country])
    bottom_box.append(q1[country])

# Configurar as caixas no gráfico
p.vbar(x, 0.7, top_box, bottom_box, fill_color=Category10_10[0], line_color='black')

# Exibir o gráfico
show(p)

'''

'''
import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_notebook

# Leitura do arquivo CSV
data = pd.read_csv("World Energy Consumption.csv")


# Calculando os quartis e limites para o gráfico de caixa e bigodes
q1 = np.percentile(dados, 25, axis=1)
q2 = np.percentile(dados, 50, axis=1)
q3 = np.percentile(dados, 75, axis=1)
iqr = q3 - q1
upper = q3 + 1.5 * iqr
lower = q1 - 1.5 * iqr

# Configurando a saída para o notebook (opcional)
output_notebook()

# Criando a figura
p = figure(plot_width=400, plot_height=400)

# Plotando as linhas verticais (bigodes)
for i, d in enumerate(dados):
    p.segment(i + 0.5, lower[i], i + 0.5, q1[i], line_color="black")
    p.segment(i + 0.5, upper[i], i + 0.5, q3[i], line_color="black")

# Plotando as caixas
p.vbar(x=np.arange(1, len(dados) + 1), top=q2, bottom=q3, width=0.7, fill_color="#E08E79", line_color="black")
p.vbar(x=np.arange(1, len(dados) + 1), top=q2, bottom=q1, width=0.7, fill_color="#3B8686", line_color="black")

# Mostrando o gráfico
show(p)
'''