# Importando todas as funções e métodos necessários
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, Range1d
from bokeh.layouts import gridplot



data = pd.read_csv("World Energy Consumption.csv")

# Gerando um dataframe apenas com os dados dos países, sem os continentes ou o mundo
data_countries = data.loc[data["country"] != "World"].dropna(subset = ["iso_code"])

# Gerando um CDS apenas com os dados do mundo e outro apenas com os dados de 2019
cds_oil_world = ColumnDataSource(data[data["country"] == "World"])
cds_oil_2019 = ColumnDataSource(data_countries[data_countries["year"] == 2019])

# Gerando CDSs apenas com os dados dos 3 maiores produtores de petróleo (Estados Unidos, Rússia e Arábia Saudita)
cds_oil_united_states = ColumnDataSource(data[data["country"] == "United States"])
cds_oil_russia = ColumnDataSource(data[data["country"] == "Russia"])
cds_oil_saudi_arabia = ColumnDataSource(data[data["country"] == "Saudi Arabia"])

# Gerando CDSs apenas com os dados das regiões mais produtoras de petróleo (África, Ásia, Oriente Médio, América do Norte e Américas Central e do Sul)
cds_oil_africa = ColumnDataSource(data[data["country"] == "Africa"])
cds_oil_asia = ColumnDataSource(data[data["country"] == "Asia Pacific"])
cds_oil_middle_east = ColumnDataSource(data[data["country"] == "Middle East"])
cds_oil_north_america = ColumnDataSource(data[data["country"] == "North America"])
cds_oil_south_and_central_america = ColumnDataSource(data[data["country"] == "South & Central America"])



# Meu primeiro gráfico é um gráfico de linhas mostrando a evolução da produção de petróleo das 5 maiores regiões produtoras ao longo dos anos
output_file("rascunho_pedro_1.html")

graph_best_regions = figure()

# Gerando as 5 linhas com base dos CDSs criados anteriormente, já com suas cores e legendas
graph_best_regions.line(x = "year", y = "oil_production", source = cds_oil_middle_east, line_color = "orange", line_width = 2, legend_label = "Oriente Médio")
graph_best_regions.line(x = "year", y = "oil_production", source = cds_oil_north_america, line_color = "blue", line_width = 2, legend_label = "América do Norte")
graph_best_regions.line(x = "year", y = "oil_production", source = cds_oil_africa, line_color = "red", line_width = 2, legend_label = "África")
graph_best_regions.line(x = "year", y = "oil_production", source = cds_oil_asia, line_color = "yellow", line_width = 2, legend_label = "Ásia")
graph_best_regions.line(x = "year", y = "oil_production", source = cds_oil_south_and_central_america, line_color = "green", line_width = 2, legend_label = "Américas Central e do Sul")

# Tirando os ticks secundários
graph_best_regions.xaxis.minor_tick_line_color = None
graph_best_regions.yaxis.minor_tick_line_color = None

# Ajustando a posição da legenda
graph_best_regions.legend.location = "top_left"

# Inserindo e personalizando o título
graph_best_regions.title.text = "Produção de petróleo das 5 maiores regiões produtoras (1900 - 2020)"
graph_best_regions.title.text_font = "arial"
graph_best_regions.title.text_font_size = "15px"
graph_best_regions.title.align = "center"

# Inserindo e ajustando os rótulos dos eixos
graph_best_regions.xaxis.axis_label = "Ano"
graph_best_regions.yaxis.axis_label = "Produção (em terawatts-hora)"
graph_best_regions.axis.axis_label_text_font_style = "normal"
graph_best_regions.xaxis.axis_label_text_font = "arial"
graph_best_regions.yaxis.axis_label_text_font = "arial"


save(graph_best_regions)


output_file("rascunho_pedro_2.html")

graph_pop_consumption = figure(x_axis_type = "log", y_axis_type = "log")

graph_pop_consumption.circle(x = "population", y = "oil_consumption", source = cds_oil_2019, size = 10)

# show(graph_pop_consumption)


output_file("rascunho_pedro_3.html")

graph_united_states = figure(height = 200)
graph_united_states.vbar(x = "year", top = "oil_prod_change_twh", source = cds_oil_united_states)
graph_united_states.x_range = Range1d(start = 1886, end = 2024)
graph_united_states.y_range = Range1d(start = -2000, end = 1200)

graph_russia = figure(height = 200)
graph_russia.vbar(x = "year", top = "oil_prod_change_twh", source = cds_oil_russia)
graph_russia.x_range = Range1d(start = 1886, end = 2024)
graph_russia.y_range = Range1d(start = -2000, end = 1200)

graph_saudi_arabia = figure(height = 200)
graph_saudi_arabia.vbar(x = "year", top = "oil_prod_change_twh", source = cds_oil_saudi_arabia)
graph_saudi_arabia.x_range = Range1d(start = 1886, end = 2024)
graph_saudi_arabia.y_range = Range1d(start = -2000, end = 1200)

grid = gridplot([[graph_united_states],
                 [graph_russia],
                 [graph_saudi_arabia]])

# show(grid)