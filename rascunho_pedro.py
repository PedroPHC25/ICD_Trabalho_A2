import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource

# Geração de eletricidade por petróleo no mundo por ano (gráfico de linha)
# Relação entre renda per capita e produção de petróleo em 2019 (scatter)
# ???

data_oil = pd.read_csv("World Energy Consumption.csv")

data_oil_world_year = ColumnDataSource(data_oil[data_oil["country"] == "World"])

output_file("rascunho_pedro.html")

graph_world_year = figure()

graph_world_year.line(x = "year", y = "oil_production", source = data_oil_world_year)

show(graph_world_year)