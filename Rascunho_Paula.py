from bokeh.plotting import figure
from bokeh.models import Range1d
from bokeh.io import output_file, save, show
import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot


nuclear = pd.read_csv("World Energy Consumption.csv")

print(nuclear)

output_file("nuclear_rascunho.html")

data_pib_nuclear_share_elec = {"x": nuclear["gdp"], "y": nuclear["nuclear_share_elec"]}

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

#show(scatterplot_gdp_nuclear_share)



output_file("nuclear_rascunho2.html")

data_pib_nuclear_elec = {"x": nuclear["gdp"], "y": nuclear["nuclear_electricity"]}

data_source = ColumnDataSource(data=data_pib_nuclear_elec )

 #configura o tamanho e as ferramentas pretendidas
scatterplot_gdp_nuclear = figure( tools = "box_zoom, pan, reset, save, wheel_zoom")

scatterplot_gdp_nuclear.circle(x = "x", y = "y", source = data_source)

scatterplot_gdp_nuclear.xaxis[0].formatter.use_scientific=False

#show(scatterplot_gdp_nuclear)



output_file("nuclear_rascunho3.html")

data_source = ColumnDataSource(data= nuclear[nuclear["country"]=="United States"])
scatterplot_year_nuclear_EUA = figure(width= 650, height = 600, tools = "box_zoom, pan, reset, save, wheel_zoom")
scatterplot_year_nuclear_EUA.line(x = "year", y = "nuclear_electricity", source = data_source)

data_source = ColumnDataSource(data= nuclear[nuclear["country"]=="France"])
scatterplot_year_nuclear_France = figure(width= 650, height = 600, tools = "box_zoom, pan, reset, save, wheel_zoom")
scatterplot_year_nuclear_France.line(x = "year", y = "nuclear_electricity", source = data_source)

data_source = ColumnDataSource(data= nuclear[nuclear["country"]=="Japan"])
scatterplot_year_nuclear_Japan = figure(width= 650, height = 600, tools = "box_zoom, pan, reset, save, wheel_zoom")
scatterplot_year_nuclear_Japan.line(x = "year", y = "nuclear_electricity", source = data_source)

data_source = ColumnDataSource(data= nuclear[nuclear["country"]=="Germany"])
scatterplot_year_nuclear_Germany = figure(width= 650, height = 600, tools = "box_zoom, pan, reset, save, wheel_zoom")
scatterplot_year_nuclear_Germany.line(x = "year", y = "nuclear_electricity", source = data_source)

data_source = ColumnDataSource(data= nuclear[nuclear["country"]=="Russia"])
scatterplot_year_nuclear_Russia = figure(width= 650, height = 600, tools = "box_zoom, pan, reset, save, wheel_zoom")
scatterplot_year_nuclear_Russia.line(x = "year", y = "nuclear_electricity", source = data_source)

data_source = ColumnDataSource(data= nuclear[nuclear["country"]=="South Korea"])
scatterplot_year_nuclear_SouthKorea = figure(width= 650, height = 600, tools = "box_zoom, pan, reset, save, wheel_zoom")
scatterplot_year_nuclear_SouthKorea.line(x = "year", y = "nuclear_electricity", source = data_source)

plot = gridplot([[scatterplot_year_nuclear_EUA, scatterplot_year_nuclear_France, scatterplot_year_nuclear_Japan],
                  [scatterplot_year_nuclear_Germany, scatterplot_year_nuclear_Russia, scatterplot_year_nuclear_SouthKorea]])

show(plot)





