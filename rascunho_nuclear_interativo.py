from bokeh.plotting import figure
from bokeh.models import Range1d, Label, Div, Spinner, TextInput, Slider
from bokeh.io import output_file, save, show
import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot, layout
from bokeh.models.annotations import Span, BoxAnnotation


data = pd.read_csv("World Energy Consumption.csv")

# Cria um data frame com todos os países excluindo a soma dos continentes e do mundo ("world"), que estão no dado original.
data_countries = data.loc[data["country"] != "World"].dropna(subset = ["iso_code"])

# Seleciona os dados do ano 2000
data_nuclear_2000 = data_countries.loc[data_countries["year"]==2000]
data_nuclear_2000["gdp_in_bi"] = data_nuclear_2000["gdp"]/ 1000000000

output_file("nuclear_rascunho.html")

# Cria um dicionário que corresponde x, y e z com as colunas 'gdp_in_bi', 'nuclear_share_energy' e 'country', do dataframe 'data_nuclear_2000'.
# E gera o ColumnDataSource com esse dicionário.
data_gdp_nuclear = {"x": data_nuclear_2000["gdp_in_bi"], 
                    "y": data_nuclear_2000["nuclear_share_energy"], 
                    "z": data_nuclear_2000["country"]}

cds_nuclear_gdp_share_country = data_source = ColumnDataSource(data=data_gdp_nuclear)

# Gera o scatterplot
scatterplot_gdp_nuclear_share = figure(width= 700, height = 700,
                                        tools = "box_zoom, pan, reset, save, wheel_zoom, hover",
                                        tooltips = [("País", "@z"),
                                                    ("Energia nuclear", "@y"),
                                                    ("PIB", "@x")]) 

points = scatterplot_gdp_nuclear_share.circle(x = "x", y = "y",color = "DeepPink", alpha = 0.5,  size = "y", source = cds_nuclear_gdp_share_country) 



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
scatterplot_gdp_nuclear_share.add_layout(Label(x = 2700, y = 35,
                                       text = "França foi o país em que a energia nuclear \nteve maior participação no consumo de \neletricidade no ano 2000",
                                       text_font_size = "14px",
                                       text_color = "MidnightBlue", 
                                       text_alpha = 0.7))

# Fundo
scatterplot_gdp_nuclear_share.background_fill_color = ("WhiteSmoke")


#Interatividade
div = Div()
slider = Slider(start = 0, end =50,
                value= 5, step = 0.5,
                title="Tamanho dos círculos")
slider.js_link("value", points.glyph, "size")

textinput = TextInput(value = points.glyph.fill_color, width = 200)
textinput.js_link("value", points.glyph, "fill_color")

nuclear_interactive_chart= layout([[div, slider],[textinput],[scatterplot_gdp_nuclear_share] ])


# show(nuclear_interactive_chart)

