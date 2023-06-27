from bokeh.plotting import figure
from bokeh.models import Range1d
from bokeh.io import output_file, save, show
import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot


data = pd.read_csv("World Energy Consumption.csv")

data_countries = data.loc[data["country"] != "World"].dropna(subset = ["iso_code"])

data_2000 = data_countries.loc[data_countries["year"]>=2000]
output_file("nuclear_rascunho.html")

data_pib_nuclear_share_elec = {"x": data_2000["population"], "y": data_2000["nuclear_share_energy"]}
data_source = ColumnDataSource(data=data_pib_nuclear_share_elec )

 #configura o tamanho e as ferramentas pretendidas
scatterplot_gdp_nuclear_share = figure(width= 640, height = 480, tools = "box_zoom, pan, reset, save, wheel_zoom")

scatterplot_gdp_nuclear_share.circle(x = "x", y = "y", source = data_source)


scatterplot_gdp_nuclear_share.toolbar.logo = None #retira a logo
scatterplot_gdp_nuclear_share.toolbar.autohide = True #deixa o barra de ferramentas invisível
scatterplot_gdp_nuclear_share.toolbar_location = "below" #define a localização barra de ferramentas


# título
scatterplot_gdp_nuclear_share.title.text = "Participação do consumo de eletricidade proveniente da energia nuclear por PIB"
scatterplot_gdp_nuclear_share.title.text_color = "DarkBlue"
scatterplot_gdp_nuclear_share.title.text_font = "Arial"
scatterplot_gdp_nuclear_share.title.text_font_size = "13px"
scatterplot_gdp_nuclear_share.title.align = "center"

# Eixos
scatterplot_gdp_nuclear_share.xaxis.axis_label = "PIB"  #título do eixo x
scatterplot_gdp_nuclear_share.xaxis.minor_tick_line_color = "black" 
scatterplot_gdp_nuclear_share.xaxis.minor_tick_in = 5
scatterplot_gdp_nuclear_share.xaxis.major_label_orientation = "vertical"

scatterplot_gdp_nuclear_share.yaxis.axis_label = "Participação da energia nuclear no consumo de eletricidade "  #título do eixo y
scatterplot_gdp_nuclear_share.yaxis.minor_tick_line_color = "black"
scatterplot_gdp_nuclear_share.yaxis.minor_tick_in = 5
scatterplot_gdp_nuclear_share.yaxis.major_label_orientation = "vertical"

show(scatterplot_gdp_nuclear_share)



output_file("nuclear_rascunho2.html")

data_pib_nuclear_elec = {"x": data["gdp"], "y": data["nuclear_electricity"]}

data_source = ColumnDataSource(data=data_pib_nuclear_elec )

 #configura o tamanho e as ferramentas pretendidas
scatterplot_gdp_nuclear = figure( tools = "box_zoom, pan, reset, save, wheel_zoom")

scatterplot_gdp_nuclear.circle(x = "x", y = "y", source = data_source)

scatterplot_gdp_nuclear.xaxis[0].formatter.use_scientific=False

# show(scatterplot_gdp_nuclear)



output_file("nuclear_rascunho3.html")
"""EUA"""
data_source = ColumnDataSource(data=data[data["country"]=="United States"]) #Cria o ColumnDataSource
line_year_nuclear_EUA = figure(width= 650, height = 600, tools = "box_zoom, pan, reset, save, wheel_zoom")
line_year_nuclear_EUA.line(x = "year", y = "nuclear_electricity", source = data_source)
# ferramnetas
line_year_nuclear_EUA.toolbar.logo = None #retira a logo
line_year_nuclear_EUA.toolbar.autohide = True #deixa o barra de ferramentas invisível
line_year_nuclear_EUA.toolbar_location = "below" #define a localização barra de ferramentas
# título
line_year_nuclear_EUA.title.text = "Geração de energia nuclear nos Estados Unidos"
line_year_nuclear_EUA.title.text_color = "DarkBlue"
line_year_nuclear_EUA.title.text_font = "Arial"
line_year_nuclear_EUA.title.text_font_size = "20px"
line_year_nuclear_EUA.title.align = "center"
# Eixos
line_year_nuclear_EUA.xaxis.axis_label = "anos"  #título do eixo x
line_year_nuclear_EUA.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_EUA.xaxis.minor_tick_in = 5
line_year_nuclear_EUA.xaxis.major_label_orientation = "vertical"
line_year_nuclear_EUA.yaxis.axis_label = "Geração de energia nuclear(terawatts-hora) "  #título do eixo y
line_year_nuclear_EUA.yaxis.minor_tick_line_color = "black"
line_year_nuclear_EUA.yaxis.minor_tick_in = 5
line_year_nuclear_EUA.yaxis.major_label_orientation = "vertical"


"""France"""
data_source = ColumnDataSource(data= data[data["country"]=="France"])
line_year_nuclear_France = figure(width= 650, height = 600, tools = "box_zoom, pan, reset, save, wheel_zoom")
line_year_nuclear_France.line(x = "year", y = "nuclear_electricity", source = data_source)
# ferramnetas
line_year_nuclear_France.toolbar.logo = None #retira a logo
line_year_nuclear_France.toolbar.autohide = True #deixa o barra de ferramentas invisível
line_year_nuclear_France.toolbar_location = "below" #define a localização barra de ferramentas
# título
line_year_nuclear_France.title.text = "Geração de energia nuclear na França"
line_year_nuclear_France.title.text_color = "DarkBlue"
line_year_nuclear_France.title.text_font = "Arial"
line_year_nuclear_France.title.text_font_size = "20px"
line_year_nuclear_France.title.align = "center"
# Eixos
line_year_nuclear_France.xaxis.axis_label = "anos"  #título do eixo x
line_year_nuclear_France.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_France.xaxis.minor_tick_in = 5
line_year_nuclear_France.xaxis.major_label_orientation = "vertical"
line_year_nuclear_France.yaxis.axis_label = "Geração de energia nuclear(terawatts-hora) "  #título do eixo y
line_year_nuclear_France.yaxis.minor_tick_line_color = "black"
line_year_nuclear_France.yaxis.minor_tick_in = 5
line_year_nuclear_France.yaxis.major_label_orientation = "vertical"

"""Japan"""
data_source = ColumnDataSource(data= data[data["country"]=="Japan"])
line_year_nuclear_Japan = figure(width= 650, height = 600, tools = "box_zoom, pan, reset, save, wheel_zoom")
line_year_nuclear_Japan.line(x = "year", y = "nuclear_electricity", source = data_source)
# ferramnetas
line_year_nuclear_Japan.toolbar.logo = None #retira a logo
line_year_nuclear_Japan.toolbar.autohide = True #deixa o barra de ferramentas invisível
line_year_nuclear_Japan.toolbar_location = "below" #define a localização barra de ferramentas
# título
line_year_nuclear_Japan.title.text = "Geração de energia nuclear no Japão"
line_year_nuclear_Japan.title.text_color = "DarkBlue"
line_year_nuclear_Japan.title.text_font = "Arial"
line_year_nuclear_Japan.title.text_font_size = "20px"
line_year_nuclear_Japan.title.align = "center"
# Eixos
line_year_nuclear_Japan.xaxis.axis_label = "anos"  #título do eixo x
line_year_nuclear_Japan.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_Japan.xaxis.minor_tick_in = 5
line_year_nuclear_Japan.xaxis.major_label_orientation = "vertical"
line_year_nuclear_Japan.yaxis.axis_label = "Geração de energia nuclear(terawatts-hora) "  #título do eixo y
line_year_nuclear_Japan.yaxis.minor_tick_line_color = "black"
line_year_nuclear_Japan.yaxis.minor_tick_in = 5
line_year_nuclear_Japan.yaxis.major_label_orientation = "vertical"


"""Germany"""
data_source = ColumnDataSource(data= data[data["country"]=="Germany"])
line_year_nuclear_Germany = figure(width= 650, height = 600, tools = "box_zoom, pan, reset, save, wheel_zoom")
line_year_nuclear_Germany.line(x = "year", y = "nuclear_electricity", source = data_source)
# ferramnetas
line_year_nuclear_Germany.toolbar.logo = None #retira a logo
line_year_nuclear_Germany.toolbar.autohide = True #deixa o barra de ferramentas invisível
line_year_nuclear_Germany.toolbar_location = "below" #define a localização barra de ferramentas
# título
line_year_nuclear_Germany.title.text = "Geração de energia nuclear na Alemanha"
line_year_nuclear_Germany.title.text_color = "DarkBlue"
line_year_nuclear_Germany.title.text_font = "Arial"
line_year_nuclear_Germany.title.text_font_size = "20px"
line_year_nuclear_Germany.title.align = "center"
# Eixos
line_year_nuclear_Germany.xaxis.axis_label = "anos"  #título do eixo x
line_year_nuclear_Germany.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_Germany.xaxis.minor_tick_in = 5
line_year_nuclear_Germany.xaxis.major_label_orientation = "vertical"
line_year_nuclear_Germany.yaxis.axis_label = "Geração de energia nuclear(terawatts-hora) "  #título do eixo y
line_year_nuclear_Germany.yaxis.minor_tick_line_color = "black"
line_year_nuclear_Germany.yaxis.minor_tick_in = 5
line_year_nuclear_Germany.yaxis.major_label_orientation = "vertical"

"""Russia"""
data_source = ColumnDataSource(data= data[data["country"]=="Russia"])
line_year_nuclear_Russia = figure(width= 650, height = 600, tools = "box_zoom, pan, reset, save, wheel_zoom")
line_year_nuclear_Russia.line(x = "year", y = "nuclear_electricity", source = data_source)
# ferramnetas
line_year_nuclear_Russia.toolbar.logo = None #retira a logo
line_year_nuclear_Russia.toolbar.autohide = True #deixa o barra de ferramentas invisível
line_year_nuclear_Russia.toolbar_location = "below" #define a localização barra de ferramentas
# título
line_year_nuclear_Russia.title.text = "Geração de energia nuclear na Russia"
line_year_nuclear_Russia.title.text_color = "DarkBlue"
line_year_nuclear_Russia.title.text_font = "Arial"
line_year_nuclear_Russia.title.text_font_size = "20px"
line_year_nuclear_Russia.title.align = "center"
# Eixos
line_year_nuclear_Russia.xaxis.axis_label = "anos"  #título do eixo x
line_year_nuclear_Russia.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_Russia.xaxis.minor_tick_in = 5
line_year_nuclear_Russia.xaxis.major_label_orientation = "vertical"
line_year_nuclear_Russia.yaxis.axis_label = "Geração de energia nuclear(terawatts-hora) "  #título do eixo y
line_year_nuclear_Russia.yaxis.minor_tick_line_color = "black"
line_year_nuclear_Russia.yaxis.minor_tick_in = 5
line_year_nuclear_Russia.yaxis.major_label_orientation = "vertical"

"""South Korea"""
data_source = ColumnDataSource(data= data[data["country"]=="South Korea"])
line_year_nuclear_SouthKorea = figure(width= 650, height = 600, tools = "box_zoom, pan, reset, save, wheel_zoom")
line_year_nuclear_SouthKorea.line(x = "year", y = "nuclear_electricity", source = data_source)
# ferramnetas
line_year_nuclear_SouthKorea.toolbar.logo = None #retira a logo
line_year_nuclear_SouthKorea.toolbar.autohide = True #deixa o barra de ferramentas invisível
line_year_nuclear_SouthKorea.toolbar_location = "below" #define a localização barra de ferramentas
# título
line_year_nuclear_SouthKorea.title.text = "Geração de energia nuclear na Koreia do Sul"
line_year_nuclear_SouthKorea.title.text_color = "DarkBlue"
line_year_nuclear_SouthKorea.title.text_font = "Arial"
line_year_nuclear_SouthKorea.title.text_font_size = "20px"
line_year_nuclear_SouthKorea.title.align = "center"
# Eixos
line_year_nuclear_SouthKorea.xaxis.axis_label = "anos"  #título do eixo x
line_year_nuclear_SouthKorea.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_SouthKorea.xaxis.minor_tick_in = 5
line_year_nuclear_SouthKorea.xaxis.major_label_orientation = "vertical"
line_year_nuclear_SouthKorea.yaxis.axis_label = "Geração de energia nuclear(terawatts-hora) "  #título do eixo y
line_year_nuclear_SouthKorea.yaxis.minor_tick_line_color = "black"
line_year_nuclear_SouthKorea.yaxis.minor_tick_in = 5
line_year_nuclear_SouthKorea.yaxis.major_label_orientation = "vertical"

plot = gridplot([[line_year_nuclear_EUA, line_year_nuclear_France, line_year_nuclear_Japan],
                  [line_year_nuclear_Germany, line_year_nuclear_Russia, line_year_nuclear_SouthKorea]])

# show(plot)

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

bar_rank_nuclear = figure(x_range = cinco_países["country"])
pais = cinco_países["country"]
y = cinco_países["nuclear_consumption"]
bar_rank_nuclear.vbar(x=pais, top=y, width=0.5)

# print(top)
# show(bar_rank_nuclear)
