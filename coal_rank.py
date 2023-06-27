import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Slider
from bokeh.layouts import column

# Gráfico de barras com os maiores consumidores de energia vinda do carvão

output_file("rank_interativo.html")

# Lendo o arquivo csv
data = pd.read_csv("World Energy Consumption.csv")


# Filtrando os dados

#Retirando os continentes e organizações
rank_data = data[~data["iso_code"].isnull()] 
rank_data = rank_data[rank_data["country"] != "World"]

# Selecionando um ano
rank_data = rank_data[rank_data["year"] == 2015]

# Ordenando e selecionando as colunas desejadas
rank_data = rank_data.sort_values("coal_consumption", ascending= False)
rank_data = rank_data[["country", "year", "coal_consumption"]]
rank_data = rank_data.head(10)


# Gráfico de barras

# Dados dos eixos
x = rank_data["country"]
y = rank_data["coal_consumption"]

# Construção do gráfico de barras
rank = figure(x_range = rank_data["country"])
rank.vbar(x=x, top=y, width=0.5)


# Construção de um slider sem interatividade
initial_year = 1900
year_slider = Slider(title="Year", start=1900, end=2019, step=1, value=initial_year)



layout = column(year_slider, rank)
show(layout)
