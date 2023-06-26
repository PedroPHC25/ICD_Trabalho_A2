import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot

# Geração de eletricidade por petróleo no mundo por ano (gráfico de linha)
# Relação entre renda per capita e produção de petróleo em 2019 (scatter)
# ???

data_oil = pd.read_csv("World Energy Consumption.csv")

best_oil_countries = ["United States", "Russia", "Saudi Arabia", "Canada", "Iraq", "China", "Iran", "Brazil", "United Arab Emirates"]

data_oil_countries = data_oil.loc[data_oil["country"] != "World"].dropna(subset = ["iso_code"])
data_oil_countries["population"] = data_oil_countries["population"]/10000000

cds_oil_world = ColumnDataSource(data_oil[data_oil["country"] == "World"])
cds_oil_2019 = ColumnDataSource(data_oil_countries[data_oil_countries["year"] == 2019])

cds_oil_best_countries = {}

for country in best_oil_countries:
    data_oil_country = data_oil_countries.loc[data_oil_countries["country"] == country]
    cds_oil_best_countries[country] = ColumnDataSource(data_oil_country)


output_file("rascunho_pedro_1.html")

graph_world_year = figure()

graph_world_year.line(x = "year", y = "oil_production", source = cds_oil_world, line_color = "green")
graph_world_year.line(x = "year", y = "oil_consumption", source = cds_oil_world, line_color = "red")

# save(graph_world_year)


output_file("rascunho_pedro_2.html")

graph_gdp_production = figure()

graph_gdp_production.circle(x = "oil_production", y = "oil_consumption", size = "population", source = cds_oil_2019)

# save(graph_gdp_production)


output_file("rascunho_pedro_3.html")

graph_united_states = figure()
graph_united_states.vbar(x = "year", top = "oil_prod_change_twh", source = cds_oil_best_countries["United States"])

graph_russia = figure()
graph_russia.vbar(x = "year", top = "oil_prod_change_twh", source = cds_oil_best_countries["Russia"])

graph_saudi_arabia = figure()
graph_saudi_arabia.vbar(x = "year", top = "oil_prod_change_twh", source = cds_oil_best_countries["Saudi Arabia"])

graph_canada = figure()
graph_canada.vbar(x = "year", top = "oil_prod_change_twh", source = cds_oil_best_countries["Canada"])

graph_iraq = figure()
graph_iraq.vbar(x = "year", top = "oil_prod_change_twh", source = cds_oil_best_countries["Iraq"])

graph_china = figure()
graph_china.vbar(x = "year", top = "oil_prod_change_twh", source = cds_oil_best_countries["China"])

graph_iran = figure()
graph_iran.vbar(x = "year", top = "oil_prod_change_twh", source = cds_oil_best_countries["Iran"])

graph_brazil = figure()
graph_brazil.vbar(x = "year", top = "oil_prod_change_twh", source = cds_oil_best_countries["Brazil"])

graph_united_arab_emirates = figure()
graph_united_arab_emirates.vbar(x = "year", top = "oil_prod_change_twh", source = cds_oil_best_countries["United Arab Emirates"])

grid = gridplot([[graph_united_states, graph_russia, graph_saudi_arabia],
                 [graph_canada, graph_iraq, graph_china],
                 [graph_iran, graph_brazil, graph_united_arab_emirates]])

show(grid)