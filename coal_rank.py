import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

# Gráfico de barras com os maiores consumidores de energia vinda do carvão

output_file("rank_interativo.html")

# Lendo o arquivo csv
data = pd.read_csv("World Energy Consumption.csv")


# Filtrando os dados

#Retirando os continentes e organizações
rank_data = data[~data["iso_code"].isnull()] 
rank_data = rank_data[rank_data["country"] != "World"]

# Selecionando um ano
rank_data = rank_data[rank_data["year"] == 1978]

# Ordenando e selecionando as colunas desejadas
rank_data = rank_data.sort_values("coal_consumption", ascending= False)
rank_data = rank_data[["country", "year", "coal_consumption"]]
rank_data = rank_data.head(10)


# Gráfico de barras

rank = figure(x_range = rank_data["country"])
pais = rank_data["country"]
y = rank_data["coal_consumption"]
rank.vbar(x=pais, top=y, width=0.5)

# print(top)
show(rank)
"""

from bokeh.plotting import figure, output_file, show
  
# file to save the model
output_file("gfg.html")
      
# instantiating the figure object
graph = figure(title = "Bokeh Vertical Bar Graph")
 
# name of the x-axis
graph.xaxis.axis_label = "x-axis"
      
# name of the y-axis
graph.yaxis.axis_label = "y-axis"
  
# x-coordinates to be plotted
x = [1, 2, 3, 4, 5]
  
# x-coordinates of the top edges
top = [1, 2, 3, 4, 5]
  
# width / thickness of the bars
width = [0.3]
 
# color values of the bars
fill_color = ["yellow", "pink", "blue", "green", "purple"]
  
# plotting the graph
graph.vbar(x,
           top = top,
           width = width,
           fill_color = fill_color)
  
# displaying the model
show(graph)
"""