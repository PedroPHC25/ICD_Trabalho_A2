from bokeh.models import ColumnDataSource, HoverTool, Label
from bokeh.plotting import figure, output_file, show
import pandas as pd
from cds_generator import cds_coal_stacked, coal_stacked_countries


# Gráfico de barras empilhadas 

# # Categoria de cada parte da barra empilhada
coal_products = ["Produção","Consumo","Eletricidade"]

colors = ['#00ff00', '#009900', '#00cc99']

coal_bar_stacked = figure(y_range = coal_stacked_countries["country"], tools = "")
coal_bar_stacked.hbar_stack(coal_products,
                        y="country",
                        source=cds_coal_stacked,
                        color=colors,
                        height=0.5,
                        legend_label= coal_products)


# Tamanho do gráfico
coal_bar_stacked.height = 550
coal_bar_stacked.width = 1000 

# Título e legendas
coal_bar_stacked.title = "Atividades a partir do carvão em 1995 (em TWh)"
coal_bar_stacked.title.text_font_size = "20px"
coal_bar_stacked.title.align = "center"

# Customização das ferramentas
hover = HoverTool(tooltips = "$name @country: @$name{1,11}")
coal_bar_stacked.add_tools(hover)
coal_bar_stacked.legend.click_policy= "mute"
coal_bar_stacked.toolbar.logo = None

# Customização do grid e linhas de contorno
coal_bar_stacked.ygrid.grid_line_color = None
coal_bar_stacked.axis.minor_tick_line_color = None
coal_bar_stacked.outline_line_color = None
coal_bar_stacked.legend.location = "top_right"
coal_bar_stacked.legend.orientation = "horizontal"

# Adicionando uma anotaçã no gráfico
coal_bar_stacked.add_layout(Label(x = 11300, y = 10.7,
                              text = "Clique na legenda para\nocultar a categoria desejada",
                              text_align = "left",
                              text_font_size = "13px",
                              text_color = "black"))
