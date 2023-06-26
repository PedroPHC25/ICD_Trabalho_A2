import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource

# Geração de eletricidade por petróleo no mundo por ano (gráfico de linha)
# Relação entre renda per capita e produção de petróleo em 2019 (scatter)
# ???

data_oil = pd.read_csv("World Energy Consumption.csv")

data_oil_countries = data_oil.loc[data_oil["country"] != "World"].dropna(subset = ["iso_code"])
data_oil_countries["population"] = data_oil_countries["population"]/10000000


data_oil_world_year = ColumnDataSource(data_oil[data_oil["country"] == "World"])
data_oil_gdp_production = ColumnDataSource(data_oil_countries[data_oil_countries["year"] == 2019])

output_file("rascunho_pedro_1.html")

graph_world_year = figure()

graph_world_year.line(x = "year", y = "oil_production", source = data_oil_world_year, line_color = "green")
graph_world_year.line(x = "year", y = "oil_consumption", source = data_oil_world_year, line_color = "red")

save(graph_world_year)

output_file("rascunho_pedro_2.html")

graph_gdp_production = figure()

graph_gdp_production.circle(x = "oil_production", y = "oil_consumption", size = "population", source = data_oil_gdp_production)

show(graph_gdp_production)