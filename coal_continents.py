from bokeh.plotting import figure
from bokeh.models import Range1d, HoverTool
from bokeh.layouts import gridplot
from bokeh.models.annotations import BoxAnnotation
from cds_generator import coal_africa_data, coal_sc_am_data, coal_europa_data, coal_am_norte_data

# Gráfico da produção de energia dos continentes ao longo do tempo

# Especificando as ferramentas e anotações
hover = HoverTool(tooltips = [("Ano", "@year"),("Produção", "@coal_production{1,11}")])
box_annotation = BoxAnnotation(left=1964, right=1981, fill_color = "silver", fill_alpha = 0.45)

# África
# Criando e customizando o plot
coal_africa = figure(tools = "")
coal_africa.title="África"
coal_africa.y_range = Range1d(start=0, end = 7500)
coal_africa.add_tools(hover)
coal_africa.add_layout(box_annotation)

# Linha do tempo com a produção anual de energia da África
coal_africa.line(x= "year", 
                 y="coal_production", 
                 source=coal_africa_data, 
                 line_color = "green", 
                 line_width=2,
                 legend_label = "África")


# Oriente Médio
# Criando e customizando o plot
coal_sc_am = figure(tools = "")
coal_sc_am.y_range = Range1d(start=0, end = 7500)
coal_sc_am.x_range = Range1d(start=1893, end = 2025)
coal_sc_am.add_tools(hover)
coal_sc_am.add_layout(box_annotation)

# Título do eixo x
coal_sc_am.title = "América do Sul e Central"
coal_sc_am.xaxis.axis_label = "Ano"
coal_sc_am.axis.axis_label_text_font_style = "bold"
coal_sc_am.xaxis.axis_label_text_font_size = "20px"

# Linha do tempo com a produção anual de energia do Oriente Médio
coal_sc_am.line(x= "year", 
                y="coal_production", 
                source=coal_sc_am_data,
                line_color = "red", 
                line_width=2,
                legend_label = "América do Sul e Central")


# Europa 

coal_europa = figure(tools = "")
coal_europa.y_range = Range1d(start=0, end = 7500)
coal_europa.add_tools(hover)
coal_europa.add_layout(box_annotation)

# Título eixo y
coal_europa.title = "Europa"
coal_europa.yaxis.axis_label = "Produção de energia a partir do carvão"
coal_europa.axis.axis_label_text_font_style = "bold"
coal_europa.yaxis.axis_label_text_font_size = "13px"

# Linha do tempo com a produção anual de energia da Europa
coal_europa.line(x= "year",
                 y="coal_production", 
                 source=coal_europa_data, 
                 line_width=2,
                 legend_label = "Europa")

# América do norte
coal_am_norte = figure(tools = "")
coal_am_norte.y_range = Range1d(start=0, end = 7500)
coal_am_norte.add_tools(hover)
coal_am_norte.add_layout(box_annotation)

# Título do eixo x
coal_am_norte.xaxis.axis_label = "Ano"
coal_am_norte.axis.axis_label_text_font_style = "bold"
coal_am_norte.xaxis.axis_label_text_font_size = "20px"
coal_am_norte.title = "América do Norte"

# Título do eixo y
coal_am_norte.yaxis.axis_label = "Produção de energia a partir do carvão"
coal_am_norte.axis.axis_label_text_font_style = "bold"
coal_am_norte.yaxis.axis_label_text_font_size = "13px"

# Linha do tempo com a produção anual de energia da América do Norte
coal_am_norte.line(x= "year", 
                   y="coal_production", 
                   source=coal_am_norte_data,
                   line_color = "gold", 
                   line_width=2,
                   legend_label = "América do Norte")

coal_am_norte.legend.location = "top_left"


# Grid 2x2, com todas as linhas do tempo
coal_grid = gridplot([[coal_europa, coal_africa], [coal_am_norte, coal_sc_am]], width=500, height=300)

coal_grid.toolbar.logo = None
