from bokeh.plotting import figure
from bokeh.models import Range1d, Label
from bokeh.io import output_file, save, show
import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot
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

scatterplot_gdp_nuclear_share.circle(x = "x", y = "y", size = "y", color = "MidnightBlue", 
                                     alpha = 0.5, source = cds_nuclear_gdp_share_country)


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

show(scatterplot_gdp_nuclear_share)


output_file("nuclear_rascunho3.html")

"""EUA"""
cds_nuclear_eua = ColumnDataSource(data=data[data["country"]=="United States"]) #Cria o ColumnDataSource apenas com os EUA

#Gera o gráfico de linha
line_year_nuclear_EUA = figure(width= 400, height = 400, 
                               tools = "box_zoom, pan, reset, save, wheel_zoom",
                               tooltips = [("Ano", "@year"),
                                           ("Energia nuclear", "@nuclear_electricity")])

renderer = line_year_nuclear_EUA.line(x = "year", y = "nuclear_electricity", source = cds_nuclear_eua, color="RoyalBlue")

# título
line_year_nuclear_EUA.title.text = "Estados Unidos da América"
line_year_nuclear_EUA.title.text_color = "MidnightBlue"
line_year_nuclear_EUA.title.text_font = "Arial"
line_year_nuclear_EUA.title.text_font_size = "20px"
line_year_nuclear_EUA.title.align = "center"

# Eixos
line_year_nuclear_EUA.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_EUA.xaxis.minor_tick_in = 5
line_year_nuclear_EUA.xaxis.major_label_orientation = "horizontal"
line_year_nuclear_EUA.yaxis.axis_label = "Geração de energia nuclear (TWh)"  #título do eixo y
line_year_nuclear_EUA.axis.axis_label_text_font = "normal" #Retira o itálico
line_year_nuclear_EUA.yaxis.minor_tick_line_color = "black"
line_year_nuclear_EUA.yaxis.minor_tick_in = 5
line_year_nuclear_EUA.axis.axis_label_text_font_style = "normal"
line_year_nuclear_EUA.xaxis[0].ticker.num_minor_ticks = 0 #número de ticks menores eixo x
line_year_nuclear_EUA.yaxis[0].ticker.num_minor_ticks = 0 #número de ticks menores eixo y
line_year_nuclear_EUA.yaxis.major_label_orientation = "horizontal"
line_year_nuclear_EUA.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo x
line_year_nuclear_EUA.yaxis.axis_label_text_font ="Arial" #Fonte do título do eixo y
line_year_nuclear_EUA.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo x
line_year_nuclear_EUA.xaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo y
line_year_nuclear_EUA.xaxis.axis_label_text_font_size = "20px" #Tamnho da fonte do título do eixo x
line_year_nuclear_EUA.yaxis.axis_label_text_font_size = "20px" #Tamnho da fonte do título do eixo y
line_year_nuclear_EUA.y_range = Range1d(start = 0, end = 850)   #muda a escala do eixo y

#Glifo
glyph_renderer = renderer.glyph #pega o renderizador do glifo
glyph_renderer.line_width= 3.5 #Define o tamanho da linha

# Fundo
line_year_nuclear_EUA.background_fill_color = ("WhiteSmoke") #Cor de fundo

#Grid
line_year_nuclear_EUA.xgrid.grid_line_color = "LightGray" #Cor do grid
line_year_nuclear_EUA.xgrid.grid_line_alpha = 0.6  #transparencia do gride
line_year_nuclear_EUA.ygrid.grid_line_color = "LightGray" #Cor do grid
line_year_nuclear_EUA.ygrid.grid_line_alpha = 0.6  #transparencia do gride


"""France"""
cds_nuclear_france = ColumnDataSource(data= data[data["country"]=="France"])
line_year_nuclear_France = figure(width= 400, height = 400, 
                                  tools = "box_zoom, pan, reset, save, wheel_zoom",
                                  tooltips = [("Ano", "@year"),
                                              ("Energia nuclear", "@nuclear_electricity")])

renderer = line_year_nuclear_France.line(x = "year", y = "nuclear_electricity", source = cds_nuclear_france, color="RoyalBlue")

# título
line_year_nuclear_France.title.text = "França"
line_year_nuclear_France.title.text_color = "MidnightBlue"
line_year_nuclear_France.title.text_font = "Arial"
line_year_nuclear_France.title.text_font_size = "20px"
line_year_nuclear_France.title.align = "center"

# Eixos
line_year_nuclear_France.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_France.xaxis.minor_tick_in = 5
line_year_nuclear_France.xaxis[0].ticker.num_minor_ticks = 0 #número de ticks menores
line_year_nuclear_France.yaxis[0].ticker.num_minor_ticks = 0
line_year_nuclear_France.xaxis.major_label_orientation = "horizontal"
line_year_nuclear_France.axis.axis_label_text_font = "normal" #retira o itálico
line_year_nuclear_France.yaxis.minor_tick_line_color = "black"
line_year_nuclear_France.yaxis.minor_tick_in = 5
line_year_nuclear_France.yaxis.major_label_orientation = "horizontal"
line_year_nuclear_France.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo
line_year_nuclear_France.yaxis.axis_label_text_font ="Arial"
line_year_nuclear_France.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo
line_year_nuclear_France.xaxis.axis_label_text_color = 'MidnightBlue'
line_year_nuclear_France.xaxis.axis_label_text_font_size = "20px" #Tamnho da fonte do título dos eixos
line_year_nuclear_France.yaxis.axis_label_text_font_size = "20px"
line_year_nuclear_France.y_range = Range1d(start = 0, end = 850)

# Fundo
line_year_nuclear_France.background_fill_color = ("WhiteSmoke")

#Grid
line_year_nuclear_France.background_fill_color = ("WhiteSmoke")
line_year_nuclear_France.xgrid.grid_line_color = "LightGray"
line_year_nuclear_France.xgrid.grid_line_alpha = 0.6  #transparencia do gride
line_year_nuclear_France.ygrid.grid_line_color = "LightGray"
line_year_nuclear_France.ygrid.grid_line_alpha = 0.6  #transparencia do gride

#Glifo
glyph_renderer = renderer.glyph #pega o renderzador do glifo
glyph_renderer.line_width= 3.5

"""Japan"""
cds_nuclear_japan = ColumnDataSource(data= data[data["country"]=="Japan"])
line_year_nuclear_Japan = figure(width= 400, height = 400, 
                                 tools = "box_zoom, pan, reset, save, wheel_zoom",
                                 tooltips = [("Ano", "@year"),
                                             ("Energia nuclear", "@nuclear_electricity")])

renderer = line_year_nuclear_Japan.line(x = "year", y = "nuclear_electricity", source = cds_nuclear_japan, color="RoyalBlue")
# título
line_year_nuclear_Japan.title.text = "Japão"
line_year_nuclear_Japan.title.text_color = "MidnightBlue"
line_year_nuclear_Japan.title.text_font = "Arial"
line_year_nuclear_Japan.title.text_font_size = "20px"
line_year_nuclear_Japan.title.align = "center"

# Eixos
line_year_nuclear_Japan.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_Japan.xaxis.minor_tick_in = 5
line_year_nuclear_Japan.xaxis[0].ticker.num_minor_ticks = 0 #número de ticks menores
line_year_nuclear_Japan.yaxis[0].ticker.num_minor_ticks = 0
line_year_nuclear_Japan.xaxis.major_label_orientation = "horizontal"
line_year_nuclear_Japan.axis.axis_label_text_font_style = "normal"
line_year_nuclear_Japan.yaxis.minor_tick_line_color = "black"
line_year_nuclear_Japan.yaxis.minor_tick_in = 5
line_year_nuclear_Japan.yaxis.major_label_orientation = "horizontal"
line_year_nuclear_Japan.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo
line_year_nuclear_Japan.yaxis.axis_label_text_font ="Arial"
line_year_nuclear_Japan.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo
line_year_nuclear_Japan.xaxis.axis_label_text_color = 'MidnightBlue'
line_year_nuclear_Japan.xaxis.axis_label_text_font_size = "20px" #Tamnho da fonte do título dos eixos
line_year_nuclear_Japan.yaxis.axis_label_text_font_size = "20px"
line_year_nuclear_Japan.y_range = Range1d(start = 0, end = 850)

# Fundo
line_year_nuclear_Japan.background_fill_color = ("WhiteSmoke")

#Grid
line_year_nuclear_Japan.xgrid.grid_line_color = "LightGray"
line_year_nuclear_Japan.xgrid.grid_line_alpha = 0.6  #transparencia do gride
line_year_nuclear_Japan.ygrid.grid_line_color = "LightGray"
line_year_nuclear_Japan.ygrid.grid_line_alpha = 0.6  #transparencia do gride

#Glifo
glyph_renderer = renderer.glyph #pega o renderizador do glifo
glyph_renderer.line_width= 3.5

#Anotação
box_annotation = BoxAnnotation(left = 2010, right = 2017, fill_color = "red", fill_alpha = 0.2)
line_year_nuclear_Japan.add_layout(box_annotation)

line_year_nuclear_Japan.add_layout(Label(x = 2009, y = 500,
                                       text = "Em 2011 ocorre o acidente\n nuclear de Fukushima Daiichi",
                                       text_align = "right",
                                       text_font_size = "12px",
                                       text_color = "red", 
                                       text_alpha = 0.7))

"""Germany"""
cds_nuclear_germany = ColumnDataSource(data= data[data["country"]=="Germany"])
line_year_nuclear_Germany = figure(width= 400, height = 400, 
                                   tools = "box_zoom, pan, reset, save, wheel_zoom",
                                   tooltips = [("Ano", "@year"),
                                                      ("Energia nuclear", "@nuclear_electricity")])
renderer = line_year_nuclear_Germany.line(x = "year", y = "nuclear_electricity", source = cds_nuclear_germany, color="RoyalBlue")
# ferramnetas
line_year_nuclear_Germany.toolbar.logo = None #retira a logo
line_year_nuclear_Germany.toolbar.autohide = True #deixa o barra de ferramentas invisível
line_year_nuclear_Germany.toolbar_location = "below" #define a localização barra de ferramentas
# título
line_year_nuclear_Germany.title.text = "Alemanha"
line_year_nuclear_Germany.title.text_color = "MidnightBlue"
line_year_nuclear_Germany.title.text_font = "Arial"
line_year_nuclear_Germany.title.text_font_size = "20px"
line_year_nuclear_Germany.title.align = "center"
# Eixos
line_year_nuclear_Germany.xaxis.axis_label = "Ano"  #título do eixo x
line_year_nuclear_Germany.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_Germany.xaxis.minor_tick_in = 5
line_year_nuclear_Germany.xaxis[0].ticker.num_minor_ticks = 0 #número de ticks menores
line_year_nuclear_Germany.yaxis[0].ticker.num_minor_ticks = 0
line_year_nuclear_Germany.xaxis.major_label_orientation = "horizontal"
line_year_nuclear_Germany.yaxis.axis_label = "Geração de energia nuclear (TWh) "  #título do eixo y
line_year_nuclear_Germany.axis.axis_label_text_font_style = "normal"
line_year_nuclear_Germany.yaxis.minor_tick_line_color = "black"
line_year_nuclear_Germany.yaxis.minor_tick_in = 5
line_year_nuclear_Germany.yaxis.major_label_orientation = "horizontal"
line_year_nuclear_Germany.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo
line_year_nuclear_Germany.yaxis.axis_label_text_font ="Arial"
line_year_nuclear_Germany.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo
line_year_nuclear_Germany.xaxis.axis_label_text_color = 'MidnightBlue'
line_year_nuclear_Germany.xaxis.axis_label_text_font_size = "20px" #Tamnho da fonte do título dos eixos
line_year_nuclear_Germany.yaxis.axis_label_text_font_size = "20px"
line_year_nuclear_Germany.y_range = Range1d(start = 0, end = 850)

# Fundo
line_year_nuclear_Germany.background_fill_color = ("WhiteSmoke")

#Grid
line_year_nuclear_Germany.xgrid.grid_line_color = "LightGray"
line_year_nuclear_Germany.xgrid.grid_line_alpha = 0.6  #transparencia do gride
line_year_nuclear_Germany.ygrid.grid_line_color = "LightGray"
line_year_nuclear_Germany.ygrid.grid_line_alpha = 0.6  #transparencia do gride

#Glifo
glyph_renderer = renderer.glyph #pega o renderizador do glifo
glyph_renderer.line_width= 3.5

"""Russia"""
cds_nuclear_russia = ColumnDataSource(data= data[data["country"]=="Russia"])
line_year_nuclear_Russia = figure(width= 400, height = 400, 
                                  tools = "box_zoom, pan, reset, save, wheel_zoom",
                                  tooltips = [("Ano", "@year"),
                                              ("Energia nuclear", "@nuclear_electricity")])

renderer = line_year_nuclear_Russia.line(x = "year", y = "nuclear_electricity", source = cds_nuclear_russia, color="RoyalBlue")

# título
line_year_nuclear_Russia.title.text = "Rússia"
line_year_nuclear_Russia.title.text_color = "MidnightBlue"
line_year_nuclear_Russia.title.text_font = "Arial"
line_year_nuclear_Russia.title.text_font_size = "20px"
line_year_nuclear_Russia.title.align = "center"

# Eixos
line_year_nuclear_Russia.xaxis.axis_label = "Ano"  #título do eixo x
line_year_nuclear_Russia.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_Russia.xaxis.minor_tick_in = 5
line_year_nuclear_Russia.axis.axis_label_text_font_style = "normal"
line_year_nuclear_Russia.xaxis[0].ticker.num_minor_ticks = 0 #número de ticks menores
line_year_nuclear_Russia.yaxis[0].ticker.num_minor_ticks = 0
line_year_nuclear_Russia.xaxis.major_label_orientation = "horizontal"

# line_year_nuclear_Russia.yaxis.axis_label = "Geração de energia nuclear(TWh) "  #título do eixo y
line_year_nuclear_Russia.axis.axis_label_text_font = "normal"
line_year_nuclear_Russia.yaxis.minor_tick_line_color = "black"
line_year_nuclear_Russia.yaxis.minor_tick_in = 5
line_year_nuclear_Russia.yaxis.major_label_orientation = "horizontal"
line_year_nuclear_Russia.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo
line_year_nuclear_Russia.yaxis.axis_label_text_font ="Arial"
line_year_nuclear_Russia.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo
line_year_nuclear_Russia.xaxis.axis_label_text_color = 'MidnightBlue'
line_year_nuclear_Russia.xaxis.axis_label_text_font_size = "20px" #Tamnho da fonte do título dos eixos
line_year_nuclear_Russia.yaxis.axis_label_text_font_size = "20px"
line_year_nuclear_Russia.y_range = Range1d(start = 0, end = 850)

# Fundo
line_year_nuclear_Russia.background_fill_color = ("WhiteSmoke")

#Grid
line_year_nuclear_Russia.xgrid.grid_line_color = "LightGray"
line_year_nuclear_Russia.xgrid.grid_line_alpha = 0.6  #transparencia do gride
line_year_nuclear_Russia.ygrid.grid_line_color = "LightGray"
line_year_nuclear_Russia.ygrid.grid_line_alpha = 0.6  #transparencia do gride

#Glifo
glyph_renderer = renderer.glyph #pega o renderzador do glifo
glyph_renderer.line_width= 3.5

"""South Korea"""
cds_nuclear_korea = ColumnDataSource(data= data[data["country"]=="South Korea"])
line_year_nuclear_SouthKorea = figure(width= 400, height = 400, 
                                      tools = "box_zoom, pan, reset, save, wheel_zoom",
                                      tooltips = [("Ano", "@year"),
                                                  ("Energia nuclear", "@nuclear_electricity")])

renderer = line_year_nuclear_SouthKorea.line(x = "year", y = "nuclear_electricity", source = cds_nuclear_korea, color="RoyalBlue")

# título
line_year_nuclear_SouthKorea.title.text = "Coreia do Sul"
line_year_nuclear_SouthKorea.title.text_color = "MidnightBlue"
line_year_nuclear_SouthKorea.title.text_font = "Arial"
line_year_nuclear_SouthKorea.title.text_font_size = "20px"
line_year_nuclear_SouthKorea.title.align = "center"

# Eixos
line_year_nuclear_SouthKorea.xaxis.axis_label = "Ano"  #título do eixo x
line_year_nuclear_SouthKorea.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_SouthKorea.xaxis.minor_tick_in = 5
line_year_nuclear_SouthKorea.axis.axis_label_text_font_style = "normal"
line_year_nuclear_SouthKorea.xaxis[0].ticker.num_minor_ticks = 0 #número de ticks menores
line_year_nuclear_SouthKorea.yaxis[0].ticker.num_minor_ticks = 0
line_year_nuclear_SouthKorea.xaxis.major_label_orientation = "horizontal"
line_year_nuclear_SouthKorea.axis.axis_label_text_font = "normal"
line_year_nuclear_SouthKorea.yaxis.minor_tick_line_color = "black"
line_year_nuclear_SouthKorea.yaxis.minor_tick_in = 5
line_year_nuclear_SouthKorea.yaxis.major_label_orientation = "horizontal"
line_year_nuclear_SouthKorea.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo
line_year_nuclear_SouthKorea.yaxis.axis_label_text_font ="Arial"
line_year_nuclear_SouthKorea.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo
line_year_nuclear_SouthKorea.xaxis.axis_label_text_color = 'MidnightBlue'
line_year_nuclear_SouthKorea.xaxis.axis_label_text_font_size = "20px" #Tamnho da fonte do título dos eixos
line_year_nuclear_SouthKorea.yaxis.axis_label_text_font_size = "20px"
line_year_nuclear_SouthKorea.y_range = Range1d(start = 0, end = 850)

# Fundo
line_year_nuclear_SouthKorea.background_fill_color = ("WhiteSmoke")

#Grid
line_year_nuclear_SouthKorea.xgrid.grid_line_color = "LightGray"
line_year_nuclear_SouthKorea.xgrid.grid_line_alpha = 0.6  #transparencia do gride
line_year_nuclear_SouthKorea.ygrid.grid_line_color = "LightGray"
line_year_nuclear_SouthKorea.ygrid.grid_line_alpha = 0.6  #transparencia do gride

#Glifo
glyph_renderer = renderer.glyph #pega o renderzador do glifo
glyph_renderer.line_width= 3.5

#Junção dos gráficos
plot = gridplot([[line_year_nuclear_EUA, line_year_nuclear_France, line_year_nuclear_Japan],
                 [line_year_nuclear_Germany, line_year_nuclear_Russia, line_year_nuclear_SouthKorea]])

show(plot)


output_file("nuclear_rascunho4.html")


# Filtrando os dados

#Retirando os continentes e organizações
best_countries_nuclear = data[~data["iso_code"].isnull()] 
best_countries_nuclear = best_countries_nuclear[best_countries_nuclear["country"] != "World"]

# Selecionando um ano
best_countries_nuclear = best_countries_nuclear[best_countries_nuclear["year"] == 2018]

# Ordenando e selecionando as colunas desejadas
best_countries_nuclear = best_countries_nuclear.sort_values("nuclear_consumption", ascending= False)
best_countries_nuclear_nuclear = best_countries_nuclear[["country", "year", "nuclear_consumption"]]
best_countries_nuclear = best_countries_nuclear.head(10)

#Adicionando cada cor à um continente
best_countries_nuclear["continent"] = ["América do norte", "Europa", "Ásia", "Ásia", "Ásia", "América do norte", "Europa", "Europa", "Europa", "Europa"]

color_dict = {"América do norte":"Tomato", "Europa":"SteelBlue", "Ásia": "Khaki"}

colors = []

for each_element in best_countries_nuclear["continent"]:
    colors.append(color_dict[each_element])

best_countries_nuclear["color"] = colors

#Gera os ColumnDataSources 
data_europe = ColumnDataSource(best_countries_nuclear[best_countries_nuclear["continent"] == "Europa"])
data_asia = ColumnDataSource(best_countries_nuclear[best_countries_nuclear["continent"] == "Ásia"])
data_america = ColumnDataSource(best_countries_nuclear[best_countries_nuclear["continent"] == "América do norte"])

# Gerando o gráfico de barras
bar_rank_nuclear = figure(x_range = best_countries_nuclear["country"], 
                          width= 800, height = 600, 
                          tools = "box_zoom, pan, reset, save, wheel_zoom",
                          tooltips = [("País", "@country"),
                                      ("Consumo de Energia nuclear", "@nuclear_consumption")])

bar_rank_nuclear.vbar(x="country", top="nuclear_consumption", legend_label = "Europa", fill_alpha = 0.9, color = "color", width=0.5, source = data_europe)
bar_rank_nuclear.vbar(x="country", top="nuclear_consumption", legend_label = "Ásia", fill_alpha = 0.8, color = "color", width=0.5, source = data_asia)
bar_rank_nuclear.vbar(x="country", top="nuclear_consumption", legend_label = "América do norte", fill_alpha = 0.8, color = "color", width=0.5, source = data_america)

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

show(bar_rank_nuclear)
