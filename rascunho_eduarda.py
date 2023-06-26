from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
import pandas as pd

# Leitura do arquivo CSV
data = pd.read_csv("World Energy Consumption.csv")

# Filtrar os dados para o ano de 2020
df_filtered = data[data['year'] == 2020]

# Ordenar os valores da coluna 'wind_electricity' em ordem decrescente
df_sorted = df_filtered.sort_values('wind_electricity', ascending=False)

# Selecionar os 10 maiores valores da coluna 'wind_electricity'
df_top_10 = df_sorted.head(10)

# Selecionar apenas as colunas desejadas ('country' e 'wind_electricity')
df_top_10_filtered = df_top_10[['country', 'wind_electricity']]

# Criar um ColumnDataSource com os dados organizados
data_organized = ColumnDataSource(df_top_10_filtered)

# Configurar a saída para um arquivo HTML
output_file("bar_chart.html")

# Criar uma figura
p = figure(title="Países que mais geraram energia a partir do vento em 2020", x_axis_label='País', y_axis_label='Geração de eletricidade a partir do vento em terawatt-hora')

# Plotar o gráfico de barras
p.vbar(x='country', top='wind_electricity', width=0.5, source=data_organized)

# Mostrar o gráfico
show(p)
