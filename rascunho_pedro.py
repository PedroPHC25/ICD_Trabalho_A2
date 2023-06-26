import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, Range1d
from bokeh.layouts import gridplot

# Geração de eletricidade por petróleo no mundo por ano (gráfico de linha)
# Relação entre renda per capita e produção de petróleo em 2019 (scatter)
# ???

data_oil = pd.read_csv("World Energy Consumption.csv")

data_oil_countries = data_oil.loc[data_oil["country"] != "World"].dropna(subset = ["iso_code"])
data_oil_countries["population"] = data_oil_countries["population"]/1000000

cds_oil_world = ColumnDataSource(data_oil[data_oil["country"] == "World"])
cds_oil_2019 = ColumnDataSource(data_oil_countries[data_oil_countries["year"] == 2019])

cds_oil_united_states = ColumnDataSource(data_oil[data_oil["country"] == "United States"])
cds_oil_russia = ColumnDataSource(data_oil[data_oil["country"] == "Russia"])
cds_oil_saudi_arabia = ColumnDataSource(data_oil[data_oil["country"] == "Saudi Arabia"])

cds_oil_africa = ColumnDataSource(data_oil[data_oil["country"] == "Africa"])
cds_oil_asia = ColumnDataSource(data_oil[data_oil["country"] == "Asia Pacific"])
cds_oil_middle_east = ColumnDataSource(data_oil[data_oil["country"] == "Middle East"])
cds_oil_north_america = ColumnDataSource(data_oil[data_oil["country"] == "North America"])
cds_oil_south_and_central_america = ColumnDataSource(data_oil[data_oil["country"] == "South & Central America"])


output_file("rascunho_pedro_1.html")

graph_best_regions = figure()

graph_best_regions.line(x = "year", y = "oil_production", source = cds_oil_africa)
graph_best_regions.line(x = "year", y = "oil_production", source = cds_oil_asia)
graph_best_regions.line(x = "year", y = "oil_production", source = cds_oil_middle_east)
graph_best_regions.line(x = "year", y = "oil_production", source = cds_oil_north_america)
graph_best_regions.line(x = "year", y = "oil_production", source = cds_oil_south_and_central_america)

show(graph_best_regions)


output_file("rascunho_pedro_2.html")

graph_pop_consumption = figure(x_axis_type = "log", y_axis_type = "log")

graph_pop_consumption.circle(x = "population", y = "oil_consumption", source = cds_oil_2019)

# show(graph_pop_consumption)


output_file("rascunho_pedro_3.html")

graph_united_states = figure(height = 200)
graph_united_states.line(x = "year", y = "oil_production", source = cds_oil_united_states)
graph_united_states.y_range = Range1d(start = 0, end = 9100)

graph_russia = figure(height = 200)
graph_russia.line(x = "year", y = "oil_production", source = cds_oil_russia)
graph_russia.y_range = Range1d(end = 9100)

graph_saudi_arabia = figure(height = 200)
graph_saudi_arabia.line(x = "year", y = "oil_production", source = cds_oil_saudi_arabia)
graph_saudi_arabia.x_range = Range1d(start = 1895, end = 2025)
graph_saudi_arabia.y_range = Range1d(end = 9100)

grid = gridplot([[graph_united_states],
                 [graph_russia],
                 [graph_saudi_arabia]])

# show(grid)