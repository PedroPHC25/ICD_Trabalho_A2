from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import GnBu3, OrRd3
from bokeh.plotting import figure, show
import pandas as pd

# Gráfico de barras empilhadas 

output_file("continents.html")

# Lendo o arquivo csv
data = pd.read_csv("World Energy Consumption.csv")

# Categoria de cada parte da barra empilhada
coal_products = ["coal_electricity","coal_production","coal_consumption"]

stacked_countries = data[data["year"] == 1995]
stacked_countries = stacked_countries[["country", "coal_electricity","coal_production","coal_consumption"]]

# Países que vão estar no gráfico
countries = ["Ukraine","Vietnam", "United States", "United Kingdom", "Turkey", "Thailand", "Spain", "South Korea", "Russia", "Poland", "New Zealand", "Mexico", "Japan", "India", "Germany", "Canada", "Brazil"]

# Colocando no dataframe só so países da lista acima
stacked_countries.set_index("country", inplace = True)
stacked_countries = stacked_countries.loc[countries]
stacked_countries.reset_index(inplace= True)

# Fazendo o gráfico de barras empilhadas horizontalmente

source = ColumnDataSource(stacked_countries)
cols = ['#00ff00', '#009900', '#00cc99']

coal_stacked = figure(y_range = stacked_countries["country"] ,
             height=500,
             tools = "pan, wheel_zoom, reset, hover, save",
             tooltips = [("Geração de eletricidade (TWh)", "@coal_electricity{1,11}"),
                         ("Produção de energia(TWh)", "@coal_production{1,11}"),
                         ("Consumo de energia (TWh)", "@coal_consumption{1,11}")])
coal_stacked.hbar_stack(coal_products,
               y="country",
               source=source,
               color=cols,
               height=0.5,
               legend_label=coal_products)

coal_stacked.ygrid.grid_line_color = None
coal_stacked.legend.location = "top_right"
coal_stacked.axis.minor_tick_line_color = None
coal_stacked.outline_line_color = None
  
# Display Stack Graph
coal_stacked.legend.orientation = "horizontal"
coal_stacked.legend.location = "bottom"
show(coal_stacked)
