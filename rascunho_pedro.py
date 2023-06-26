import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot

# Geração de eletricidade por petróleo no mundo por ano (gráfico de linha)
# Relação entre renda per capita e produção de petróleo em 2019 (scatter)
# ???

data_oil = pd.read_csv("World Energy Consumption.csv")

best_oil_countries = ["United States", "Russia", "Saudi Arabia"]

data_oil_countries = data_oil.loc[data_oil["country"] != "World"].dropna(subset = ["iso_code"])
data_oil_countries["population"] = data_oil_countries["population"]/10000000

cds_oil_world = ColumnDataSource(data_oil[data_oil["country"] == "World"])
cds_oil_2019 = ColumnDataSource(data_oil_countries[data_oil_countries["year"] == 2019])

cds_oil_best_countries = {}

for country in best_oil_countries:
    data_oil_country = data_oil_countries.loc[data_oil_countries["country"] == country]
    cds_oil_best_countries[country] = ColumnDataSource(data_oil_country)


output_file("rascunho_pedro_1.html")

graph_world_variation = figure()

graph_world_variation.vbar(x = "year", top = "oil_cons_change_twh", source = cds_oil_world, fill_color = "blue", fill_alpha = 1)

show(graph_world_variation)


output_file("rascunho_pedro_2.html")

graph_gdp_production = figure()

graph_gdp_production.circle(x = "oil_production", y = "oil_consumption", size = "population", source = cds_oil_2019)

show(graph_gdp_production)


output_file("rascunho_pedro_3.html")

graph_united_states = figure()
graph_united_states.line(x = "year", y = "oil_production", source = cds_oil_best_countries["United States"])

graph_russia = figure()
graph_russia.line(x = "year", y = "oil_production", source = cds_oil_best_countries["Russia"])

graph_saudi_arabia = figure()
graph_saudi_arabia.line(x = "year", y = "oil_production", source = cds_oil_best_countries["Saudi Arabia"])

grid = gridplot([[graph_united_states, graph_russia, graph_saudi_arabia]])

show(grid)