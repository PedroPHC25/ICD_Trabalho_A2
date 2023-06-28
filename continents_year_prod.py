import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Range1d, HoverTool
from bokeh.layouts import gridplot
from bokeh.models.annotations import BoxAnnotation

# Gráfico da produção de energia dos continentes ao longo do tempo

output_file("coal_continents.html")

# Lendo o arquivo csv
data = pd.read_csv("World Energy Consumption.csv")

# Especificando as ferramentas e anotações
hover = HoverTool(tooltips = [("Ano", "@year"),("Produção", "@coal_production{1,11}")])
box_annotation = BoxAnnotation(left=1964, right=1981, fill_color = "DeepPink", fill_alpha = 0.42)

# África
# Filtrando apenas os dados da África
africa_data = data[data["country"] == "Africa"]
# Convertendo o arquivo para CDS
africa_data = ColumnDataSource(africa_data)
africa = figure(tools = "")
africa.title="África"
africa.y_range = Range1d(start=0, end = 7500)
africa.add_tools(hover)
africa.add_layout(box_annotation)

# Linha do tempo com a produção anual de energia da África
africa.line(x= "year", 
            y="coal_production", 
            source=africa_data, 
            line_color = "green")


# Oriente Médio
# Filtrando os dados
sc_am_data = data[data["country"] == "South & Central America"]
# Convertendo o arquivo para CDS
source = ColumnDataSource(sc_am_data)
sc_am = figure(tools = "pan, wheel_zoom, reset, hover, save",
                 tooltips = [("Ano", "@year"),("Produção", "@coal_production{1,11}")],
                 y_range = (0,7500),
                 x_range = (1893, 2025))
sc_am.title = "América do Sul e Central"
sc_am.y_range = Range1d(start=0, end = 7500)
sc_am.x_range = Range1d(start=1893, end = 2025)

# Linha do tempo com a produção anual de energia do Oriente Médio
sc_am.line(x= "year", 
             y="coal_production", 
             source=source,
             line_color = "red")


# Europa 
# Filtrando os dados
europa_data = data[data["country"] == "Europe"]
# Convertendo o arquivo para CDS
source = ColumnDataSource(europa_data)
europa = figure(tools = "pan, wheel_zoom, reset, hover, save",
                tooltips = [("Ano", "@year"),("Produção", "@coal_production{1,11}")])
europa.y_range = Range1d(start=0, end = 7500)

# Títulos
europa.title = "Europa"
europa.yaxis.axis_label = "Produção de energia pelo carvão"
# Linha do tempo com a produção anual de energia da Europa
europa.line(x= "year", 
            y="coal_production", 
            source=source)

# América do norte
# Filtrando os dados 
am_norte_data = data[data["country"] == "North America"]
# Convertendo o arquivo para CDS
source = ColumnDataSource(am_norte_data)
am_norte = figure(tools = "pan, wheel_zoom, reset, hover, save",
                 tooltips = [("Ano", "@year"),("Produção", "@coal_production{1,11}")])
am_norte.y_range = Range1d(start=0, end = 7500)

# Títulos
am_norte.yaxis.axis_label = "Produção de energia pelo carvão"
am_norte.axis.axis_label_text_font_style = "normal"
am_norte.xaxis.axis_label_text_font = "georgia"
am_norte.title = "América do Norte"
# Linha do tempo com a produção anual de energia da América do Norte
am_norte.line(x= "year", 
              y="coal_production", 
              source=source,
              line_color = "gold")


# Grid 2x2, com todas as linhas do tempo
grid = gridplot([[europa, africa], [am_norte, sc_am]], width=500, height=300)

show(grid)