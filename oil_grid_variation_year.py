# Importando todas as funções e métodos necessários
from bokeh.plotting import figure
from bokeh.models import Range1d, Label
from bokeh.layouts import gridplot
from bokeh.models.annotations import BoxAnnotation, Span

# Pegando os dados do arquivo gerador de CDS
from cds_generator import cds_oil_positive_united_states, cds_oil_negative_united_states, cds_oil_positive_russia, cds_oil_negative_russia, cds_oil_positive_saudi_arabia, cds_oil_negative_saudi_arabia

# Esta visualização é um gridplot com 3 gráficos de barras que indicam a variação da produção de petróleo nos 3 países mais produtores: Estados Unidos, Rússia e Arábia Saudita

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
                      tooltips = [("Ano", "@year"), 
                                  ("Variação", "@oil_prod_change_twh{1,11}")])
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
graph_united_states.title.text_font_size = "17px"

graph_russia.title.text = "Rússia"
graph_russia.title.text_font = "arial"
graph_russia.title.text_font_size = "17px"

graph_saudi_arabia.title.text = "Arábia Saudita"
graph_saudi_arabia.title.text_font = "arial"
graph_saudi_arabia.title.text_font_size = "17px"

# Configurando os títulos dos eixos
graph_saudi_arabia.xaxis.axis_label = "Ano"
graph_russia.yaxis.axis_label = "Variação anual da produção\nde petróleo (terawatts-hora)"
graph_saudi_arabia.axis.axis_label_text_font_style = "normal"
graph_russia.axis.axis_label_text_font_style = "normal"
graph_saudi_arabia.xaxis.axis_label_text_font = "arial"
graph_russia.yaxis.axis_label_text_font = "arial"
graph_saudi_arabia.axis.axis_label_text_font_size = "14px"
graph_russia.axis.axis_label_text_font_size = "14px"

# Ajustando o grid
graph_united_states.xgrid.grid_line_alpha = 0.4
graph_united_states.ygrid.grid_line_alpha = 0.4
graph_russia.xgrid.grid_line_alpha = 0.4
graph_russia.ygrid.grid_line_alpha = 0.4
graph_saudi_arabia.xgrid.grid_line_alpha = 0.4
graph_saudi_arabia.ygrid.grid_line_alpha = 0.4

# Criando uma anotação para destacar a linha y = 0
graph_united_states.add_layout(Span(location = 0,
                                    dimension = "width",
                                    line_color = "black",
                                    line_width = 0.5))
graph_russia.add_layout(Span(location = 0,
                             dimension = "width",
                             line_color = "black",
                             line_width = 0.5))
graph_saudi_arabia.add_layout(Span(location = 0,
                                   dimension = "width",
                                   line_color = "black",
                                   line_width = 0.5))

# Criando uma anotação no gráfico referente aos Estados Unidos
graph_united_states.add_layout(BoxAnnotation(left = 2008.5, 
                                             right = 2019.5,
                                             fill_color = "green",
                                             fill_alpha = 0.3))
graph_united_states.add_layout(Label(x = 2005, 
                                     y = -1750, 
                                     text = "Aumento na produção estadunidense devido\n ao desenvolvimento de tecnologias para\n extração e produção do petróleo de xisto", text_font_size = "11px",
                                     text_color = "green",
                                     text_alpha = 0.8,
                                     text_align = "right"))

# Criando uma anotação no gráfico referente à Rússia
graph_russia.add_layout(BoxAnnotation(left = 1987.5, 
                                      right = 1996.5, 
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
graph_saudi_arabia.add_layout(BoxAnnotation(left = 1980.5,
                                            right = 1985.5,
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
oil_grid = gridplot([[graph_united_states],
                     [graph_russia],
                     [graph_saudi_arabia]], 
                     toolbar_options = dict(autohide = True, logo = None), 
                     toolbar_location = "right")