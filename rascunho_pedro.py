# Importando todas as funções e métodos necessários
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, Range1d, Label, PrintfTickFormatter
from bokeh.layouts import gridplot
from bokeh.models.annotations import BoxAnnotation



data = pd.read_csv("World Energy Consumption.csv")

# Gerando um dataframe apenas com os dados dos países, sem os continentes ou o mundo
data_countries = data.loc[data["country"] != "World"].dropna(subset = ["iso_code"])
data_2019_high_consumption = data_countries.loc[data_countries["year"] == 2019].loc[data_countries["oil_consumption"]/data["population"] > 53619.925/7713467904]
data_2019_low_consumption = data_countries.loc[data_countries["year"] == 2019].loc[data_countries["oil_consumption"]/data["population"] < 53619.925/7713467904]

# Gerando um CDS apenas com os dados do mundo e outro apenas com os dados de 2019
cds_oil_world = ColumnDataSource(data[data["country"] == "World"])
cds_oil_2019_high_consumption = ColumnDataSource(data_2019_high_consumption)
cds_oil_2019_low_consumption = ColumnDataSource(data_2019_low_consumption)

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

# Criando o objeto figure com as ferramentas desejadas
graph_best_regions = figure(tools = "pan, wheel_zoom, reset, save")

# Gerando as 5 linhas com base dos CDSs criados anteriormente, já com suas cores e legendas
graph_best_regions.line(x = "year", 
                        y = "oil_production", 
                        source = cds_oil_middle_east, 
                        line_color = "orange", 
                        line_width = 2, 
                        legend_label = "Oriente Médio")
graph_best_regions.line(x = "year", 
                        y = "oil_production", 
                        source = cds_oil_north_america, 
                        line_color = "blue", 
                        line_width = 2, 
                        legend_label = "América do Norte")
graph_best_regions.line(x = "year", 
                        y = "oil_production", 
                        source = cds_oil_africa, 
                        line_color = "red", 
                        line_width = 2, 
                        legend_label = "África")
graph_best_regions.line(x = "year", 
                        y = "oil_production", 
                        source = cds_oil_asia, 
                        line_color = "yellow", 
                        line_width = 2, 
                        legend_label = "Ásia")
graph_best_regions.line(x = "year", 
                        y = "oil_production", 
                        source = cds_oil_south_and_central_america, 
                        line_color = "green", 
                        line_width = 2, 
                        legend_label = "Américas Central e do Sul")

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

# Ajustando o grid
graph_best_regions.xgrid.grid_line_alpha = 0.4
graph_best_regions.ygrid.grid_line_alpha = 0.4

# Configurando as ferramentas
graph_best_regions.toolbar.autohide = True
graph_best_regions.toolbar.logo = None

# Adicionando anotações
graph_best_regions.add_layout(BoxAnnotation(left = 1980, 
                                            right = 1990, 
                                            fill_color = "red", 
                                            fill_alpha = 0.1))
graph_best_regions.add_layout(Label(x = 1992, 
                                    y = 50, 
                                    text = "Crise do petróleo \ncausada pela invasão \niraquiana do Irã", 
                                    text_font_size = "12px", 
                                    text_color = "red", 
                                    text_alpha = 0.7))

# Salvando o gráfico
# save(graph_best_regions)



# Minha segunda visualização será um gráfico de dispersão mostrando a relação entre a população de cada país e o consumo de petróleo
output_file("rascunho_pedro_2.html")

# Criando o objeto figura com os eixos em escala logarítmica e com as ferramentas adequadas
graph_pop_consumption = figure(x_axis_type = "log", 
                               y_axis_type = "log", 
                               tools = "pan, wheel_zoom, reset, hover, save")

# Gerando o gráfico de dispersão com os dados do CDS
graph_pop_consumption.circle(x = "population", y = "oil_consumption", source = cds_oil_2019_high_consumption, size = 5, fill_color = "red", line_color = "red")
graph_pop_consumption.circle(x = "population", y = "oil_consumption", source = cds_oil_2019_low_consumption, size = 5, fill_color = "lime", line_color = "lime")

# Excluindo os ticks secundários
graph_pop_consumption.xaxis.minor_tick_line_color = None
graph_pop_consumption.yaxis.minor_tick_line_color = None

graph_pop_consumption.xaxis[0].formatter = PrintfTickFormatter(format="%5f")
graph_pop_consumption.yaxis[0].formatter = PrintfTickFormatter(format="%5f")
graph_pop_consumption.xaxis.major_label_overrides = {1000000: '1 milhão', 10000000: '10 milhões', 100000000: '100 milhões'}

save(graph_pop_consumption)


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