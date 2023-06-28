from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import GnBu3, OrRd3
from bokeh.plotting import figure, show
import pandas as pd

# Gráfico de barras empilhadas 

output_file("coal_stacked.html")

# Lendo o arquivo csv
data = pd.read_csv("World Energy Consumption.csv")

# Filtrando a base de dados
coal_stacked_countries = data[data["year"] == 1995]
coal_stacked_countries = coal_stacked_countries[["country", "coal_electricity","coal_production","coal_consumption"]]

# Renomenando as colunas
coal_stacked_countries["Eletricidade"] = coal_stacked_countries["coal_electricity"]
coal_stacked_countries["Produção"] = coal_stacked_countries["coal_production"]
coal_stacked_countries["Consumo"] = coal_stacked_countries["coal_consumption"]

# Categoria de cada parte da barra empilhada
coal_products = ["Eletricidade","Produção","Consumo"]

# Países que vão estar no gráfico
countries = ["United States", "India", "Russia", "Germany", "Poland", "Japan", "Ukraine", "United Kingdom", "Canada", "South Korea", "Spain", "Brazil"]

# Colocando no dataframe só so países da lista acima
coal_stacked_countries.set_index("country", inplace = True)
coal_stacked_countries = coal_stacked_countries.loc[countries]
coal_stacked_countries.reset_index(inplace= True)

# Fazendo o gráfico de barras empilhadas horizontalmente

coal_stacked_cds = ColumnDataSource(coal_stacked_countries)
colors = ['#00ff00', '#009900', '#00cc99']

coal_stacked = figure(y_range = coal_stacked_countries["country"],
                     tools = "pan, wheel_zoom, reset, hover, save",
                     tooltips = "$name @country: @$name{1,11}")
coal_stacked.hbar_stack(coal_products,
                        y="country",
                        source=coal_stacked_cds,
                        color=colors,
                        height=0.5,
                        legend_label= coal_products)

# Tamanho do gráfico
coal_stacked.height = 550
coal_stacked.width = 1000 

# Título e legendas
coal_stacked.title = "Atividades a partir do carvão (em TWh)"
coal_stacked.title.text_font_size = "20px"
coal_stacked.title.align = "center"



coal_stacked.ygrid.grid_line_color = None
coal_stacked.legend.location = "top_right"
coal_stacked.legend.click_policy= "mute"
coal_stacked.axis.minor_tick_line_color = None
coal_stacked.outline_line_color = None
coal_stacked.legend.orientation = "horizontal"

show(coal_stacked)
