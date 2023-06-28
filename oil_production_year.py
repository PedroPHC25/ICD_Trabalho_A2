# Importando as bibliotecas necessárias
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, Range1d, Label, PrintfTickFormatter, Div
from bokeh.layouts import gridplot, column
from bokeh.models.annotations import BoxAnnotation, Span

# Pegando os dados do arquivo gerador de CDS
from cds_generator import cds_oil_middle_east, cds_oil_north_america, cds_oil_africa, cds_oil_asia, cds_oil_south_and_central_america

# Este é um gráfico de linhas mostrando a evolução da produção de petróleo das 5 maiores regiões produtoras ao longo dos anos

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