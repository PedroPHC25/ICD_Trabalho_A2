from bokeh.plotting import figure
from cds_generator import best_countries_nuclear, data_america, data_europe, data_asia

# Gerando o gráfico de barras
bar_rank_nuclear = figure(x_range = best_countries_nuclear["country"], 
                          width= 800, 
                          height = 600, 
                          tools = "box_zoom, pan, reset, save, wheel_zoom",
                          tooltips = [("País", "@country"),
                                      ("Consumo de Energia nuclear", "@nuclear_consumption")])

bar_rank_nuclear.vbar(x="country", 
                      top="nuclear_consumption", 
                      legend_label = "Europa", 
                      fill_alpha = 0.9, 
                      color = "color", 
                      width=0.5, 
                      source = data_europe)
bar_rank_nuclear.vbar(x="country", 
                      top="nuclear_consumption", 
                      legend_label = "Ásia", 
                      fill_alpha = 0.8, 
                      color = "color", 
                      width=0.5, 
                      source = data_asia)
bar_rank_nuclear.vbar(x="country", 
                      top="nuclear_consumption", 
                      legend_label = "América do norte", 
                      fill_alpha = 0.8, 
                      color = "color", 
                      width=0.5, 
                      source = data_america)

# ferramnetas
bar_rank_nuclear.toolbar.logo = None #retira a logo
bar_rank_nuclear.toolbar.autohide = True #deixa o barra de ferramentas invisível
bar_rank_nuclear.toolbar_location = "below" #define a localização barra de ferramentas

# título
bar_rank_nuclear.title.text = "Os 10 países que mais consumiram energia nuclear em 2018"
bar_rank_nuclear.title.text_color = "#00075F"
bar_rank_nuclear.title.text_font = "Arial"
bar_rank_nuclear.title.text_font_size = "22px"
bar_rank_nuclear.title.align = "center"

# Eixos
bar_rank_nuclear.xaxis.axis_label = "País"  #título do eixo x
bar_rank_nuclear.xaxis.minor_tick_line_color = "black" 
bar_rank_nuclear.xaxis.minor_tick_in = 5
bar_rank_nuclear.axis.axis_label_text_font_style= "normal"
bar_rank_nuclear.xaxis.major_label_orientation = "horizontal"
bar_rank_nuclear.yaxis.axis_label = "Consumo de energia primária nuclear (TWh) "  #título do eixo y
bar_rank_nuclear.yaxis.minor_tick_line_color = "black"
bar_rank_nuclear.yaxis.minor_tick_in = 5
bar_rank_nuclear.yaxis.major_label_orientation = "horizontal"
bar_rank_nuclear.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo
bar_rank_nuclear.yaxis.axis_label_text_font ="Arial"
bar_rank_nuclear.yaxis.axis_label_text_color = '#00075F' #cor do título do eixo
bar_rank_nuclear.yaxis[0].ticker.num_minor_ticks = 0
bar_rank_nuclear.xaxis.axis_label_text_color = '#00075F'
bar_rank_nuclear.xaxis.axis_label_text_font_size = "20px" #Tamnho da fonte do título dos eixos
bar_rank_nuclear.yaxis.axis_label_text_font_size = "20px"

# Fundo
bar_rank_nuclear.background_fill_color = ("WhiteSmoke")

