from bokeh.plotting import figure
from bokeh.models import Range1d, Label
from bokeh.io import output_file, save, show
import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot


data = pd.read_csv("World Energy Consumption.csv")

# Cria um data frame com todos os países excluindo a soma dos continentes e do mundo ("world"), que estão no dado original.
data_countries = data.loc[data["country"] != "World"].dropna(subset = ["iso_code"])
# Seleciona os dados a partir do ano 2000
data_2000 = data_countries.loc[data_countries["year"]==2000]
data_2000["gdp_em_bi"] = data_2000["gdp"]/ 1000000000

output_file("nuclear_rascunho.html")
print(data_2000)
# Cria um dicionário que corresponde x e y com as colunas 'population' e 'nuclear_share_energy', do dataframe 'data_2000'.
# E gera o ColumnDataSource com esse dicionário.
data_pib_nuclear = {"x": data_2000["gdp_em_bi"], "y": data_2000["nuclear_share_energy"], "z": data_2000["country"]}
data_source = ColumnDataSource(data=data_pib_nuclear)

# Gera o scatterplot
scatterplot_gdp_nuclear_share = figure(width= 700, height = 700,
                                        tools = "box_zoom, pan, reset, save, wheel_zoom, hover",
                                          tooltips = [("País", "@z"),
                                                      ("Energia nuclear", "@y"),
                                                      ("PIB", "@x")])
scatterplot_gdp_nuclear_share.circle(x = "x", y = "y", size = "y", color = "MidnightBlue", 
                                     alpha = 0.5, source = data_source)


# Ferramentas pretendidas
scatterplot_gdp_nuclear_share.toolbar.logo = None #retira a logo
scatterplot_gdp_nuclear_share.toolbar.autohide = True #deixa a barra de ferramentas invisível
scatterplot_gdp_nuclear_share.toolbar_location = "right" #define a localização barra de ferramentas

# título
scatterplot_gdp_nuclear_share.title.text = "Energia nuclear por PIB"
scatterplot_gdp_nuclear_share.title.text_color = "MidnightBlue"
scatterplot_gdp_nuclear_share.title.text_font = "Arial"
scatterplot_gdp_nuclear_share.title.text_font_size = "25px"
scatterplot_gdp_nuclear_share.title.align = "center"

# Eixos
scatterplot_gdp_nuclear_share.xaxis.axis_label = "Produto interno bruto em bilhões"  #título do eixo x
scatterplot_gdp_nuclear_share.xaxis.minor_tick_line_color = "black" 
scatterplot_gdp_nuclear_share.xaxis.minor_tick_in = 5
scatterplot_gdp_nuclear_share.xaxis.major_label_orientation = "horizontal"

scatterplot_gdp_nuclear_share.yaxis.axis_label = "Participação da energia nuclear no consumo de eletricidade "  #título do eixo y
scatterplot_gdp_nuclear_share.yaxis.minor_tick_line_color = "black"
scatterplot_gdp_nuclear_share.yaxis.minor_tick_in = 5
scatterplot_gdp_nuclear_share.yaxis.major_label_orientation = "vertical"

scatterplot_gdp_nuclear_share.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo
scatterplot_gdp_nuclear_share.yaxis.axis_label_text_font ="Arial"
scatterplot_gdp_nuclear_share.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo
scatterplot_gdp_nuclear_share.xaxis.axis_label_text_color = 'MidnightBlue'

scatterplot_gdp_nuclear_share.xaxis.axis_label_text_font_size = "20px" #Tamanho da fonte do título dos eixos
scatterplot_gdp_nuclear_share.yaxis.axis_label_text_font_size = "20px"

# Anotação
scatterplot_gdp_nuclear_share.add_layout(Label(x = 2700, y = 35,
                                       text = "França foi o país que a energia nuclear \nteve mais participação no consumo de \neletricidade no ano 2000.",
                                       text_font_size = "14px",
                                       text_color = "Black", 
                                       text_alpha = 0.7))

scatterplot_gdp_nuclear_share.xaxis[0].formatter.use_scientific = False # Retirar o modo de escala em notação científica


# Fundo
scatterplot_gdp_nuclear_share.background_fill_color = ("WhiteSmoke")
# scatterplot_gdp_nuclear_share.background_fill_alpha = 0.9

# show(scatterplot_gdp_nuclear_share)


output_file("nuclear_rascunho3.html")

"""EUA"""
data_source = ColumnDataSource(data=data[data["country"]=="United States"]) #Cria o ColumnDataSource
line_year_nuclear_EUA = figure(width= 650, height = 600, tools = "box_zoom, pan, reset, save, wheel_zoom")
renderer = line_year_nuclear_EUA.line(x = "year", y = "nuclear_electricity", source = data_source, color="RoyalBlue")
# ferramnetas
line_year_nuclear_EUA.toolbar.logo = None #retira a logo
line_year_nuclear_EUA.toolbar.autohide = True #deixa o barra de ferramentas invisível
line_year_nuclear_EUA.toolbar_location = "below" #define a localização barra de ferramentas
# título
line_year_nuclear_EUA.title.text = "Geração de energia nuclear nos Estados Unidos"
line_year_nuclear_EUA.title.text_color = "MidnightBlue"
line_year_nuclear_EUA.title.text_font = "Arial"
line_year_nuclear_EUA.title.text_font_size = "25px"
line_year_nuclear_EUA.title.align = "center"
# Eixos
line_year_nuclear_EUA.xaxis.axis_label = "anos"  #título do eixo x
line_year_nuclear_EUA.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_EUA.xaxis.minor_tick_in = 5
line_year_nuclear_EUA.xaxis.major_label_orientation = "horizontal"
line_year_nuclear_EUA.yaxis.axis_label = "Geração de energia nuclear(terawatts-hora) "  #título do eixo y
line_year_nuclear_EUA.yaxis.minor_tick_line_color = "black"
line_year_nuclear_EUA.yaxis.minor_tick_in = 5
line_year_nuclear_EUA.yaxis.major_label_orientation = "horizontal"

line_year_nuclear_EUA.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo
line_year_nuclear_EUA.yaxis.axis_label_text_font ="Arial"
line_year_nuclear_EUA.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo
line_year_nuclear_EUA.xaxis.axis_label_text_color = 'MidnightBlue'

line_year_nuclear_EUA.xaxis.axis_label_text_font_size = "25px" #Tamnho da fonte do título dos eixos
line_year_nuclear_EUA.yaxis.axis_label_text_font_size = "25px"

# line_year_nuclear_EUA.x_range = Range1d(start = 0, end=10)  #muda a escala dos eixos
line_year_nuclear_EUA.y_range = Range1d(start = 0, end = 850)

#Glifo
glyph_renderer = renderer.glyph #pega o renderzador do glifo
glyph_renderer.line_width= 3.5


# Fundo
line_year_nuclear_EUA.background_fill_color = ("WhiteSmoke")

#Grid
line_year_nuclear_EUA.xgrid.grid_line_color = "LightGray"
line_year_nuclear_EUA.xgrid.grid_line_alpha = 0.6  #transparencia do gride

line_year_nuclear_EUA.ygrid.grid_line_color = "LightGray"
line_year_nuclear_EUA.ygrid.grid_line_alpha = 0.6  #transparencia do gride

# line_year_nuclear_EUA.grid.grid_line_dash = [1, 42] #pontilhamento, quanros traços para quantos espaços



"""France"""
data_source = ColumnDataSource(data= data[data["country"]=="France"])
line_year_nuclear_France = figure(width= 650, height = 600, tools = "box_zoom, pan, reset, save, wheel_zoom")
renderer = line_year_nuclear_France.line(x = "year", y = "nuclear_electricity", source = data_source, color="RoyalBlue")
# ferramnetas
line_year_nuclear_France.toolbar.logo = None #retira a logo
line_year_nuclear_France.toolbar.autohide = True #deixa o barra de ferramentas invisível
line_year_nuclear_France.toolbar_location = "below" #define a localização barra de ferramentas
# título
line_year_nuclear_France.title.text = "Geração de energia nuclear na França"
line_year_nuclear_France.title.text_color = "MidnightBlue"
line_year_nuclear_France.title.text_font = "Arial"
line_year_nuclear_France.title.text_font_size = "25px"
line_year_nuclear_France.title.align = "center"
# Eixos
line_year_nuclear_France.xaxis.axis_label = "anos"  #título do eixo x
line_year_nuclear_France.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_France.xaxis.minor_tick_in = 5
line_year_nuclear_France.xaxis.major_label_orientation = "horizontal"
line_year_nuclear_France.yaxis.axis_label = "Geração de energia nuclear(terawatts-hora) "  #título do eixo y
line_year_nuclear_France.yaxis.minor_tick_line_color = "black"
line_year_nuclear_France.yaxis.minor_tick_in = 5
line_year_nuclear_France.yaxis.major_label_orientation = "horizontal"

line_year_nuclear_France.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo
line_year_nuclear_France.yaxis.axis_label_text_font ="Arial"
line_year_nuclear_France.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo
line_year_nuclear_France.xaxis.axis_label_text_color = 'MidnightBlue'

line_year_nuclear_France.xaxis.axis_label_text_font_size = "25px" #Tamnho da fonte do título dos eixos
line_year_nuclear_France.yaxis.axis_label_text_font_size = "25px"

line_year_nuclear_France.y_range = Range1d(start = 0, end = 850)

# Fundo
line_year_nuclear_France.background_fill_color = ("WhiteSmoke")

#Grid
line_year_nuclear_France.background_fill_color = ("WhiteSmoke")
line_year_nuclear_France.xgrid.grid_line_color = "LightGray"
line_year_nuclear_France.xgrid.grid_line_alpha = 0.6  #transparencia do gride

line_year_nuclear_France.ygrid.grid_line_color = "LightGray"
line_year_nuclear_France.ygrid.grid_line_alpha = 0.6  #transparencia do gride

# line_year_nuclear_EUA.grid.grid_line_dash = [1, 42] #pontilhamento, quanros traços para quantos espaços

#Glifo
glyph_renderer = renderer.glyph #pega o renderzador do glifo
glyph_renderer.line_width= 3.5

"""Japan"""
data_source = ColumnDataSource(data= data[data["country"]=="Japan"])
line_year_nuclear_Japan = figure(width= 650, height = 600, tools = "box_zoom, pan, reset, save, wheel_zoom")
renderer = line_year_nuclear_Japan.line(x = "year", y = "nuclear_electricity", source = data_source, color="RoyalBlue")
# ferramnetas
line_year_nuclear_Japan.toolbar.logo = None #retira a logo
line_year_nuclear_Japan.toolbar.autohide = True #deixa o barra de ferramentas invisível
line_year_nuclear_Japan.toolbar_location = "below" #define a localização barra de ferramentas
# título
line_year_nuclear_Japan.title.text = "Geração de energia nuclear no Japão"
line_year_nuclear_Japan.title.text_color = "MidnightBlue"
line_year_nuclear_Japan.title.text_font = "Arial"
line_year_nuclear_Japan.title.text_font_size = "25px"
line_year_nuclear_Japan.title.align = "center"
# Eixos
line_year_nuclear_Japan.xaxis.axis_label = "anos"  #título do eixo x
line_year_nuclear_Japan.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_Japan.xaxis.minor_tick_in = 5
line_year_nuclear_Japan.xaxis.major_label_orientation = "horizontal"
line_year_nuclear_Japan.yaxis.axis_label = "Geração de energia nuclear(terawatts-hora) "  #título do eixo y
line_year_nuclear_Japan.yaxis.minor_tick_line_color = "black"
line_year_nuclear_Japan.yaxis.minor_tick_in = 5
line_year_nuclear_Japan.yaxis.major_label_orientation = "horizontal"

line_year_nuclear_Japan.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo
line_year_nuclear_Japan.yaxis.axis_label_text_font ="Arial"
line_year_nuclear_Japan.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo
line_year_nuclear_Japan.xaxis.axis_label_text_color = 'MidnightBlue'

line_year_nuclear_Japan.xaxis.axis_label_text_font_size = "25px" #Tamnho da fonte do título dos eixos
line_year_nuclear_Japan.yaxis.axis_label_text_font_size = "25px"

line_year_nuclear_Japan.y_range = Range1d(start = 0, end = 850)


# Fundo
line_year_nuclear_Japan.background_fill_color = ("WhiteSmoke")

#Grid
line_year_nuclear_Japan.xgrid.grid_line_color = "LightGray"
line_year_nuclear_Japan.xgrid.grid_line_alpha = 0.6  #transparencia do gride

line_year_nuclear_Japan.ygrid.grid_line_color = "LightGray"
line_year_nuclear_Japan.ygrid.grid_line_alpha = 0.6  #transparencia do gride

#Glifo
glyph_renderer = renderer.glyph #pega o renderzador do glifo
glyph_renderer.line_width= 3.5

"""Germany"""
data_source = ColumnDataSource(data= data[data["country"]=="Germany"])
line_year_nuclear_Germany = figure(width= 650, height = 600, tools = "box_zoom, pan, reset, save, wheel_zoom")
renderer = line_year_nuclear_Germany.line(x = "year", y = "nuclear_electricity", source = data_source, color="RoyalBlue")
# ferramnetas
line_year_nuclear_Germany.toolbar.logo = None #retira a logo
line_year_nuclear_Germany.toolbar.autohide = True #deixa o barra de ferramentas invisível
line_year_nuclear_Germany.toolbar_location = "below" #define a localização barra de ferramentas
# título
line_year_nuclear_Germany.title.text = "Geração de energia nuclear na Alemanha"
line_year_nuclear_Germany.title.text_color = "MidnightBlue"
line_year_nuclear_Germany.title.text_font = "Arial"
line_year_nuclear_Germany.title.text_font_size = "25px"
line_year_nuclear_Germany.title.align = "center"
# Eixos
line_year_nuclear_Germany.xaxis.axis_label = "anos"  #título do eixo x
line_year_nuclear_Germany.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_Germany.xaxis.minor_tick_in = 5
line_year_nuclear_Germany.xaxis.major_label_orientation = "horizontal"
line_year_nuclear_Germany.yaxis.axis_label = "Geração de energia nuclear(terawatts-hora) "  #título do eixo y
line_year_nuclear_Germany.yaxis.minor_tick_line_color = "black"
line_year_nuclear_Germany.yaxis.minor_tick_in = 5
line_year_nuclear_Germany.yaxis.major_label_orientation = "horizontal"

line_year_nuclear_Germany.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo
line_year_nuclear_Germany.yaxis.axis_label_text_font ="Arial"
line_year_nuclear_Germany.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo
line_year_nuclear_Germany.xaxis.axis_label_text_color = 'MidnightBlue'

line_year_nuclear_Germany.xaxis.axis_label_text_font_size = "25px" #Tamnho da fonte do título dos eixos
line_year_nuclear_Germany.yaxis.axis_label_text_font_size = "25px"

line_year_nuclear_Germany.y_range = Range1d(start = 0, end = 850)


# Fundo
line_year_nuclear_Germany.background_fill_color = ("WhiteSmoke")

#Grid
line_year_nuclear_Germany.xgrid.grid_line_color = "LightGray"
line_year_nuclear_Germany.xgrid.grid_line_alpha = 0.6  #transparencia do gride

line_year_nuclear_Germany.ygrid.grid_line_color = "LightGray"
line_year_nuclear_Germany.ygrid.grid_line_alpha = 0.6  #transparencia do gride

#Glifo
glyph_renderer = renderer.glyph #pega o renderzador do glifo
glyph_renderer.line_width= 3.5

"""Russia"""
data_source = ColumnDataSource(data= data[data["country"]=="Russia"])
line_year_nuclear_Russia = figure(width= 650, height = 600, tools = "box_zoom, pan, reset, save, wheel_zoom")
renderer = line_year_nuclear_Russia.line(x = "year", y = "nuclear_electricity", source = data_source, color="RoyalBlue")
# ferramnetas
line_year_nuclear_Russia.toolbar.logo = None #retira a logo
line_year_nuclear_Russia.toolbar.autohide = True #deixa o barra de ferramentas invisível
line_year_nuclear_Russia.toolbar_location = "below" #define a localização barra de ferramentas
# título
line_year_nuclear_Russia.title.text = "Geração de energia nuclear na Russia"
line_year_nuclear_Russia.title.text_color = "MidnightBlue"
line_year_nuclear_Russia.title.text_font = "Arial"
line_year_nuclear_Russia.title.text_font_size = "25px"
line_year_nuclear_Russia.title.align = "center"
# Eixos
line_year_nuclear_Russia.xaxis.axis_label = "anos"  #título do eixo x
line_year_nuclear_Russia.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_Russia.xaxis.minor_tick_in = 5
line_year_nuclear_Russia.xaxis.major_label_orientation = "horizontal"
line_year_nuclear_Russia.yaxis.axis_label = "Geração de energia nuclear(terawatts-hora) "  #título do eixo y
line_year_nuclear_Russia.yaxis.minor_tick_line_color = "black"
line_year_nuclear_Russia.yaxis.minor_tick_in = 5
line_year_nuclear_Russia.yaxis.major_label_orientation = "horizontal"

line_year_nuclear_Russia.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo
line_year_nuclear_Russia.yaxis.axis_label_text_font ="Arial"
line_year_nuclear_Russia.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo
line_year_nuclear_Russia.xaxis.axis_label_text_color = 'MidnightBlue'

line_year_nuclear_Russia.xaxis.axis_label_text_font_size = "25px" #Tamnho da fonte do título dos eixos
line_year_nuclear_Russia.yaxis.axis_label_text_font_size = "25px"

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
data_source = ColumnDataSource(data= data[data["country"]=="South Korea"])
line_year_nuclear_SouthKorea = figure(width= 650, height = 600, tools = "box_zoom, pan, reset, save, wheel_zoom")
renderer = line_year_nuclear_SouthKorea.line(x = "year", y = "nuclear_electricity", source = data_source, color="RoyalBlue")
# ferramnetas
line_year_nuclear_SouthKorea.toolbar.logo = None #retira a logo
line_year_nuclear_SouthKorea.toolbar.autohide = True #deixa o barra de ferramentas invisível
line_year_nuclear_SouthKorea.toolbar_location = "below" #define a localização barra de ferramentas
# título
line_year_nuclear_SouthKorea.title.text = "Geração de energia nuclear na Koreia do Sul"
line_year_nuclear_SouthKorea.title.text_color = "MidnightBlue"
line_year_nuclear_SouthKorea.title.text_font = "Arial"
line_year_nuclear_SouthKorea.title.text_font_size = "25px"
line_year_nuclear_SouthKorea.title.align = "center"
# Eixos
line_year_nuclear_SouthKorea.xaxis.axis_label = "anos"  #título do eixo x
line_year_nuclear_SouthKorea.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_SouthKorea.xaxis.minor_tick_in = 5
line_year_nuclear_SouthKorea.xaxis.major_label_orientation = "horizontal"
line_year_nuclear_SouthKorea.yaxis.axis_label = "Geração de energia nuclear(terawatts-hora) "  #título do eixo y
line_year_nuclear_SouthKorea.yaxis.minor_tick_line_color = "black"
line_year_nuclear_SouthKorea.yaxis.minor_tick_in = 5
line_year_nuclear_SouthKorea.yaxis.major_label_orientation = "horizontal"

line_year_nuclear_SouthKorea.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo
line_year_nuclear_SouthKorea.yaxis.axis_label_text_font ="Arial"
line_year_nuclear_SouthKorea.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo
line_year_nuclear_SouthKorea.xaxis.axis_label_text_color = 'MidnightBlue'

line_year_nuclear_SouthKorea.xaxis.axis_label_text_font_size = "25px" #Tamnho da fonte do título dos eixos
line_year_nuclear_SouthKorea.yaxis.axis_label_text_font_size = "25px"

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

plot = gridplot([[line_year_nuclear_EUA, line_year_nuclear_France, line_year_nuclear_Japan],
                  [line_year_nuclear_Germany, line_year_nuclear_Russia, line_year_nuclear_SouthKorea]])

show(plot)

output_file("nuclear_rascunho4.html")

# Filtrando os dados

#Retirando os continentes e organizações
cinco_países = data[~data["iso_code"].isnull()] 
cinco_países = cinco_países[cinco_países["country"] != "World"]

# Selecionando um ano
cinco_países = cinco_países[cinco_países["year"] == 2018]

# Ordenando e selecionando as colunas desejadas
cinco_países = cinco_países.sort_values("nuclear_consumption", ascending= False)
cinco_países = cinco_países[["country", "year", "nuclear_consumption"]]
cinco_países = cinco_países.head(10)


# Gráfico de barras
bar_rank_nuclear = figure(x_range = cinco_países["country"], width= 650, height = 600, tools = "box_zoom, pan, reset, save, wheel_zoom")
pais = cinco_países["country"]
y = cinco_países["nuclear_consumption"]
bar_rank_nuclear.vbar(x=pais, top=y, width=0.5)

# ferramnetas
bar_rank_nuclear.toolbar.logo = None #retira a logo
bar_rank_nuclear.toolbar.autohide = True #deixa o barra de ferramentas invisível
bar_rank_nuclear.toolbar_location = "below" #define a localização barra de ferramentas
# título
bar_rank_nuclear.title.text = "Geração de energia nuclear na Koreia do Sul"
bar_rank_nuclear.title.text_color = "MidnightBlue"
bar_rank_nuclear.title.text_font = "Arial"
bar_rank_nuclear.title.text_font_size = "20px"
bar_rank_nuclear.title.align = "center"
# Eixos
bar_rank_nuclear.xaxis.axis_label = "anos"  #título do eixo x
bar_rank_nuclear.xaxis.minor_tick_line_color = "black" 
bar_rank_nuclear.xaxis.minor_tick_in = 5
bar_rank_nuclear.xaxis.major_label_orientation = "horizontal"
bar_rank_nuclear.yaxis.axis_label = "Geração de energia nuclear(terawatts-hora) "  #título do eixo y
bar_rank_nuclear.yaxis.minor_tick_line_color = "black"
bar_rank_nuclear.yaxis.minor_tick_in = 5
bar_rank_nuclear.yaxis.major_label_orientation = "vertical"

bar_rank_nuclear.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo
bar_rank_nuclear.yaxis.axis_label_text_font ="Arial"
bar_rank_nuclear.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo
bar_rank_nuclear.xaxis.axis_label_text_color = 'MidnightBlue'

bar_rank_nuclear.xaxis.axis_label_text_font_size = "15px" #Tamnho da fonte do título dos eixos
bar_rank_nuclear.yaxis.axis_label_text_font_size = "20px"



# Fundo
bar_rank_nuclear.background_fill_color = ("WhiteSmoke")


# print(top)
# show(bar_rank_nuclear)
