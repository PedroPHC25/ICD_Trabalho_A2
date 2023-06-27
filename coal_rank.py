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

# Função de atualização do gráfico com base no valor do slider
def update_plot(attr, old, new):
    year = year_slider.value
    new_data = data[data["year"] == year]
    new_data = new_data.sort_values("coal_consumption", ascending=False)
    new_data = new_data[["country", "year", "coal_consumption"]]
    new_data = new_data.head(10)
    source.data = ColumnDataSource.from_df(new_data)
    rank.x_range.factors = list(new_data["country"])
    bars.data_source.data = source.data

# Criando o slider
initial_year = 1900
year_slider = Slider(title="Year", start=1900, end=2019, step=1, value=initial_year)
year_slider.on_change('value', update_plot)

# Combinando o gráfico e o slider em uma única figura
layout = column(year_slider, rank)

# Adicionando o layout à aplicação
curdoc().add_root(layout)

show(layout)