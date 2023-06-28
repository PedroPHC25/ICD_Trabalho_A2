from bokeh.plotting import figure, output_file, show, curdoc
import pandas as pd
from bokeh.models import ColumnDataSource, Slider
from bokeh.layouts import column

# Gráfico de barras com os maiores consumidores de energia vinda do carvão

output_file("rank_interativo.html")

# Lendo o arquivo csv
data = pd.read_csv("World Energy Consumption.csv")


# Filtrando os dados

#Retirando os continentes e organizações
data_country = data[~data["iso_code"].isnull()] 
data_country = data_country[data_country["country"] != "World"]

# Selecionando um ano
rank_data = data_country[data_country["year"] == 2015]

# Ordenando e selecionando as colunas desejadas
rank_data = rank_data.sort_values("coal_consumption", ascending= False)
rank_data = rank_data[["country", "year", "coal_consumption"]]
rank_data = rank_data.head(10)


# Gráfico de barras

# Dados dos eixos
source = ColumnDataSource(rank_data)

# Construção do gráfico de barras
rank = figure(x_range = rank_data["country"])
rank.width = 1000
rank.height = 550
rank.vbar(x="country", top="coal_consumption", width=0.5, source=source)

# Função de atualização do gráfico com base no valor do slider
def update_plot(attr, old, new):
    year = year_slider.value
    new_data = data_country[data_country["year"] == year]
    new_data = new_data.sort_values("coal_consumption", ascending=False)
    new_data = new_data[["country", "year", "coal_consumption"]]
    new_data = new_data.head(10)
    source.data = ColumnDataSource.from_df(new_data)
    rank.x_range.factors = list(new_data["country"])

# Criando o slider
initial_year = 1900
year_slider = Slider(title="ano", start=1965, end=2019, step=1, value=initial_year)
year_slider.on_change('value', update_plot)

# Combinando o gráfico e o slider em uma única figura
layout = column(year_slider, rank)

# Adicionando o layout à aplicação
curdoc().add_root(layout)

show(layout)
