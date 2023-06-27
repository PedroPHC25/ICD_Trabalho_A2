# Importando todas as funções e métodos necessários
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, Range1d, Label, PrintfTickFormatter, Div
from bokeh.layouts import gridplot, column
from bokeh.models.annotations import BoxAnnotation


data = pd.read_csv("World Energy Consumption.csv")

# Gerando um dataframe apenas com os dados dos países, sem os continentes ou o mundo
data_countries = data.loc[data["country"] != "World"].dropna(subset = ["iso_code"])

# Criando uma nova coluna com a média de consumo de petróleo em função da população
data_countries["oil_mean_consumption"] = data_countries["oil_consumption"]/data_countries["population"]

# Gerando dataframes cujos países possuem um consumo de petróleo acima e abaixo da média mundial em 2019, valor esse calculado a partir da divisão do consumo pela população
data_2019_high_consumption = data_countries.loc[data_countries["year"] == 2019].loc[data_countries["oil_mean_consumption"] > 53619.925/7713467904]
data_2019_low_consumption = data_countries.loc[data_countries["year"] == 2019].loc[data_countries["oil_mean_consumption"] < 53619.925/7713467904]

# Gerando tabelas filtradas referentes aos dados dos 3 maiores produtores de petróleo (Estados Unidos, Rússia e Arábia Saudita), separados por anos em que a variação na produção foi positiva e negativa
data_positive_united_states = data.loc[data["country"] == "United States"].loc[data["oil_prod_change_twh"] > 0]
data_positive_russia = data.loc[data["country"] == "Russia"].loc[data["oil_prod_change_twh"] > 0]
data_positive_saudi_arabia = data.loc[data["country"] == "Saudi Arabia"].loc[data["oil_prod_change_twh"] > 0]
data_negative_united_states = data.loc[data["country"] == "United States"].loc[data["oil_prod_change_twh"] < 0]
data_negative_russia = data.loc[data["country"] == "Russia"].loc[data["oil_prod_change_twh"] < 0]
data_negative_saudi_arabia = data.loc[data["country"] == "Saudi Arabia"].loc[data["oil_prod_change_twh"] < 0]

# Gerando um CDS apenas com os dados do mundo
cds_oil_world = ColumnDataSource(data[data["country"] == "World"])

# Gerando CDSs com os dados de 2019 separados com base no consumo de petróleo do país
cds_oil_2019_high_consumption = ColumnDataSource(data_2019_high_consumption)
cds_oil_2019_low_consumption = ColumnDataSource(data_2019_low_consumption)

# Gerando CDSs apenas com os dados dos 3 maiores produtores de petróleo (Estados Unidos, Rússia e Arábia Saudita), separados por anos em que a produção aumentou ou diminuiu
cds_oil_positive_united_states = ColumnDataSource(data_positive_united_states)
cds_oil_positive_russia = ColumnDataSource(data_positive_russia)
cds_oil_positive_saudi_arabia = ColumnDataSource(data_positive_saudi_arabia)
cds_oil_negative_united_states = ColumnDataSource(data_negative_united_states)
cds_oil_negative_russia = ColumnDataSource(data_negative_russia)
cds_oil_negative_saudi_arabia = ColumnDataSource(data_negative_saudi_arabia)

# Gerando CDSs apenas com os dados das regiões mais produtoras de petróleo (África, Ásia, Oriente Médio, América do Norte e Américas Central e do Sul)
cds_oil_africa = ColumnDataSource(data[data["country"] == "Africa"])
cds_oil_asia = ColumnDataSource(data[data["country"] == "Asia Pacific"])
cds_oil_middle_east = ColumnDataSource(data[data["country"] == "Middle East"])
cds_oil_north_america = ColumnDataSource(data[data["country"] == "North America"])
cds_oil_south_and_central_america = ColumnDataSource(data[data["country"] == "South & Central America"])


##############################################################################################################


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


##############################################################################################################


# Minha segunda visualização será um gráfico de dispersão mostrando a relação entre a população de cada país e o consumo de petróleo

output_file("rascunho_pedro_2.html")

# Criando o objeto figura com os eixos em escala logarítmica e com as ferramentas adequadas
graph_pop_consumption = figure(x_axis_type = "log", 
                               y_axis_type = "log", 
                               tools = "pan, wheel_zoom, reset, hover, save",
                               tooltips = [("País", "@country")])

# Gerando o gráfico de dispersão com os dados dos CDSs, agrupando os dados por cor (verde são os países com consumo abaixo da média mundial e vermelho são os com consumo acima)
graph_pop_consumption.circle(x = "population", 
                             y = "oil_consumption", 
                             source = cds_oil_2019_high_consumption, 
                             fill_color = "red",
                             line_color = "red",
                             size = 5,  
                             legend_label = "Acima da média mundial")
graph_pop_consumption.circle(x = "population", 
                             y = "oil_consumption", 
                             source = cds_oil_2019_low_consumption, 
                             fill_color = "lime",
                             line_color = "lime",
                             size = 5, 
                             legend_label = "Abaixo da média mundial")

# Excluindo os ticks secundários
graph_pop_consumption.xaxis.minor_tick_line_color = None
graph_pop_consumption.yaxis.minor_tick_line_color = None

# Ajustando os rótulos dos eixos
graph_pop_consumption.xaxis[0].formatter = PrintfTickFormatter(format="%5f")
graph_pop_consumption.yaxis[0].formatter = PrintfTickFormatter(format="%5f")
graph_pop_consumption.xaxis.major_label_overrides = {1000000: '1 milhão', 
                                                     10000000: '10 milhões', 
                                                     100000000: '100 milhões', 
                                                     1000000000: "1 bilhão"}

# Inserindo e customizando o título
graph_pop_consumption.title.text = "Consumo de petróleo x População em 2019"
graph_pop_consumption.title.text_font = "arial"
graph_pop_consumption.title.text_font_size = "15px"
graph_pop_consumption.title.align = "center"

# Adicionando os títulos dos eixos
graph_pop_consumption.xaxis.axis_label = "População"
graph_pop_consumption.yaxis.axis_label = "Consumo (em terawatts-hora)"
graph_pop_consumption.axis.axis_label_text_font_style = "normal"
graph_pop_consumption.xaxis.axis_label_text_font = "arial"
graph_pop_consumption.yaxis.axis_label_text_font = "arial"

# Gerando a legenda
graph_pop_consumption.legend.location = "top_left"

# Ajustando o grid
graph_pop_consumption.xgrid.grid_line_alpha = 0.4
graph_pop_consumption.ygrid.grid_line_alpha = 0.4

# Ajustando a barra de ferramentas
graph_pop_consumption.toolbar.autohide = True
graph_pop_consumption.toolbar.logo = None

# Adicionando uma anotação
graph_pop_consumption.add_layout(Label(x = 100000000,
                                       y = 15, 
                                       text = "Em geral, quanto maior \na população, maior \no consumo de petróleo",
                                       text_font_size = "12px",
                                       text_color = "darkslategray",
                                       text_alpha = 0.8))

# Salvando o gráfico
# save(graph_pop_consumption)


##############################################################################################################


# Minha terceira e última visualização é um gridplot com 3 gráficos de barras que indicam a variação da produção de petróleo nos 3 países mais produtores: Estados Unidos, Rússia e Arábia Saudita

output_file("rascunho_pedro_3.html")

# Gerando os 3 gráficos de barras, já com os ajustes de dimensões, com as cores verde para os dados positivos e vermelho para os dados negativos e com as ferramentas adequadas
graph_united_states = figure(height = 200, 
                             tools = "pan, wheel_zoom, reset, hover, save", 
                             tooltips = [("Ano", "@year"), ("Variação", "@oil_prod_change_twh{1,11}")])
graph_united_states.vbar(x = "year", 
                         top = "oil_prod_change_twh", 
                         source = cds_oil_positive_united_states, 
                         fill_color = "limegreen", 
                         line_color = "limegreen")
graph_united_states.vbar(x = "year", 
                         top = "oil_prod_change_twh", 
                         source = cds_oil_negative_united_states, 
                         fill_color = "red", 
                         line_color = "red")
graph_united_states.x_range = Range1d(start = 1886, end = 2024)
graph_united_states.y_range = Range1d(start = -2000, end = 1200)

graph_russia = figure(height = 200, 
                      tools = "pan, wheel_zoom, reset, hover, save",
                      tooltips = [("Ano", "@year"), ("Variação", "@oil_prod_change_twh{1,11}")])
graph_russia.vbar(x = "year", 
                  top = "oil_prod_change_twh", 
                  source = cds_oil_positive_russia, 
                  fill_color = "limegreen", 
                  line_color = "limegreen")
graph_russia.vbar(x = "year", 
                  top = "oil_prod_change_twh", 
                  source = cds_oil_negative_russia, 
                  fill_color = "red", 
                  line_color = "red")
graph_russia.x_range = Range1d(start = 1886, end = 2024)
graph_russia.y_range = Range1d(start = -2000, end = 1200)

graph_saudi_arabia = figure(height = 200, 
                            tools = "pan, wheel_zoom, reset, hover, save",
                            tooltips = [("Ano", "@year"), ("Variação", "@oil_prod_change_twh{1,11}")])
graph_saudi_arabia.vbar(x = "year", 
                        top = "oil_prod_change_twh", 
                        source = cds_oil_positive_saudi_arabia, 
                        fill_color = "limegreen", 
                        line_color = "limegreen")
graph_saudi_arabia.vbar(x = "year", 
                        top = "oil_prod_change_twh", 
                        source = cds_oil_negative_saudi_arabia, 
                        fill_color = "red", 
                        line_color = "red")
graph_saudi_arabia.x_range = Range1d(start = 1886, end = 2024)
graph_saudi_arabia.y_range = Range1d(start = -2000, end = 1200)

# Tirando os ticks secundários dos eixos
graph_united_states.xaxis.minor_tick_line_color = None
graph_united_states.yaxis.minor_tick_line_color = None
graph_russia.xaxis.minor_tick_line_color = None
graph_russia.yaxis.minor_tick_line_color = None
graph_saudi_arabia.xaxis.minor_tick_line_color = None
graph_saudi_arabia.yaxis.minor_tick_line_color = None

# Adicionando os títulos dos gráficos
graph_united_states.title.text = "Estados Unidos"
graph_united_states.title.text_font = "arial"
graph_united_states.title.text_font_size = "15px"

graph_russia.title.text = "Rússia"
graph_russia.title.text_font = "arial"
graph_russia.title.text_font_size = "15px"

graph_saudi_arabia.title.text = "Arábia Saudita"
graph_saudi_arabia.title.text_font = "arial"
graph_saudi_arabia.title.text_font_size = "15px"

# Configurando os títulos dos eixos
graph_saudi_arabia.xaxis.axis_label = "Ano"
graph_russia.yaxis.axis_label = "Variação anual da produção\nde petróleo (em terawatts-hora)"
graph_saudi_arabia.axis.axis_label_text_font_style = "normal"
graph_russia.axis.axis_label_text_font_style = "normal"
graph_saudi_arabia.xaxis.axis_label_text_font = "arial"
graph_russia.yaxis.axis_label_text_font = "arial"

# Ajustando o grid
graph_united_states.xgrid.grid_line_alpha = 0.4
graph_united_states.ygrid.grid_line_alpha = 0.4
graph_russia.xgrid.grid_line_alpha = 0.4
graph_russia.ygrid.grid_line_alpha = 0.4
graph_saudi_arabia.xgrid.grid_line_alpha = 0.4
graph_saudi_arabia.ygrid.grid_line_alpha = 0.4

# Criando uma anotação no gráfico referente aos Estados Unidos
graph_united_states.add_layout(BoxAnnotation(left = 2009, 
                                             right = 2019,
                                             fill_color = "green",
                                             fill_alpha = 0.3))
graph_united_states.add_layout(Label(x = 2005, 
                                     y = -1750, 
                                     text = "Aumento na produção estadunidense devido\n ao desenvolvimento de tecnologias para\n extração e produção do petróleo de xisto", text_font_size = "11px",
                                     text_color = "green",
                                     text_alpha = 0.8,
                                     text_align = "right"))

# Criando uma anotação no gráfico referente à Rússia
graph_russia.add_layout(BoxAnnotation(left = 1988, 
                                      right = 1996, 
                                      fill_color = "red", 
                                      fill_alpha = 0.3))
graph_russia.add_layout(Label(x = 1984, 
                              y = -1750, 
                              text = "Queda na produção russa provocada\n pela instabilidade ocasionada pela\n queda da União Soviética em 1991", 
                              text_font_size = "11px", 
                              text_color = "red", 
                              text_alpha = 0.8,
                              text_align = "right"))

# Criando uma anotação no gráfico referente à Árábia Saudita
graph_saudi_arabia.add_layout(BoxAnnotation(left = 1981,
                                            right = 1985,
                                            fill_color = "red",
                                            fill_alpha = 0.3))
graph_saudi_arabia.add_layout(Label(x = 1970,
                                    y = -1750,
                                    text = "Forte baixa na produção saudita gerada pela\n crise mundial desencadeada pela Revolução Iraniana\n de 1979 e pela Guerra Irã-Iraque de 1980",
                                    text_font_size = "11px",
                                    text_color = "red",
                                    text_alpha = 0.8,
                                    text_align = "right"))

# Gerando o gridplot com os 3 gráficos e configurando a toolbar
grid = gridplot([[graph_united_states],
                 [graph_russia],
                 [graph_saudi_arabia]], 
                 toolbar_options = dict(autohide = True, logo = None), 
                 toolbar_location = "right")

# Salvando a visualização
# save(grid)

output_file("petroleo.html")

text = Div(text = "")

show(column(text, graph_best_regions))