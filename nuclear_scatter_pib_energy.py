from bokeh.plotting import figure
from bokeh.models import Label
from cds_generator import cds_nuclear_gdp_share_country
from nuclear_scatter_interactive import nuclear_interactive_chart
from bokeh.layouts import gridplot



# Gera o scatterplot

scatterplot_gdp_nuclear_share = figure(width= 600, height = 600,
                                        tools = "box_zoom, pan, reset, save, wheel_zoom, hover",
                                        tooltips = [("País", "@z"),
                                                    ("Energia nuclear", "@y"),
                                                    ("PIB", "@x")]) 

scatterplot_gdp_nuclear_share.circle(x = "x", 
                                     y = "y", 
                                     size = "y", 
                                     color = "MidnightBlue", 
                                     alpha = 0.5, 
                                     source = cds_nuclear_gdp_share_country)


# Ferramentas pretendidas
scatterplot_gdp_nuclear_share.toolbar.logo = None #retira a logo
scatterplot_gdp_nuclear_share.toolbar.autohide = True #deixa a barra de ferramentas invisível
scatterplot_gdp_nuclear_share.toolbar_location = "right" #define a localização barra de ferramentas

# título
scatterplot_gdp_nuclear_share.title.text = "Energia nuclear por PIB em 2000"
scatterplot_gdp_nuclear_share.title.text_color = "MidnightBlue"
scatterplot_gdp_nuclear_share.title.text_font = "Arial"
scatterplot_gdp_nuclear_share.title.text_font_size = "25px"
scatterplot_gdp_nuclear_share.title.align = "center"

# Eixos
scatterplot_gdp_nuclear_share.xaxis.axis_label = "Produto Interno Bruto em bilhões"  #título do eixo x
scatterplot_gdp_nuclear_share.xaxis.minor_tick_line_color = "black" 
scatterplot_gdp_nuclear_share.xaxis.minor_tick_in = 5
scatterplot_gdp_nuclear_share.xaxis[0].ticker.num_minor_ticks = 0
scatterplot_gdp_nuclear_share.xaxis.major_label_orientation = "horizontal"

scatterplot_gdp_nuclear_share.yaxis.axis_label = "Participação da energia nuclear no consumo de eletricidade (%)"  #título do eixo y
scatterplot_gdp_nuclear_share.yaxis.minor_tick_line_color = "black"
scatterplot_gdp_nuclear_share.yaxis.minor_tick_in = 5
scatterplot_gdp_nuclear_share.yaxis[0].ticker.num_minor_ticks = 0
scatterplot_gdp_nuclear_share.yaxis.major_label_orientation = "horizontal"

scatterplot_gdp_nuclear_share.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo x
scatterplot_gdp_nuclear_share.yaxis.axis_label_text_font ="Arial" #Fonte do título do eixo y
scatterplot_gdp_nuclear_share.axis.axis_label_text_font_style= "normal" #Retira o itálico
scatterplot_gdp_nuclear_share.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo x
scatterplot_gdp_nuclear_share.xaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo y
scatterplot_gdp_nuclear_share.xaxis.axis_label_text_font_size = "20px" #Tamanho da fonte do título dos eixo x
scatterplot_gdp_nuclear_share.yaxis.axis_label_text_font_size = "20px" #Tamanho da fonte do título dos eixo y
scatterplot_gdp_nuclear_share.xaxis[0].formatter.use_scientific = False #Retirar o modo de escala em notação científica

# Anotação
scatterplot_gdp_nuclear_share.add_layout(Label(x = 2700, 
                                               y = 35,
                                               text = "França foi o país em que a energia nuclear \nteve maior participação no consumo de \neletricidade no ano 2000",
                                               text_font_size = "14px",
                                               text_color = "MidnightBlue", 
                                               text_alpha = 0.7))

# Fundo
scatterplot_gdp_nuclear_share.background_fill_color = ("WhiteSmoke")

grid_scatter_gdp_nuclear_share = gridplot([[scatterplot_gdp_nuclear_share, nuclear_interactive_chart]])



