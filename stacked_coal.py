from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import GnBu3, OrRd3
from bokeh.plotting import figure, show
import pandas as pd

# Gráfico de barras empilhadas 

output_file("coal_stacked.html")

# Lendo o arquivo csv
data = pd.read_csv("World Energy Consumption.csv")

# Categoria de cada parte da barra empilhada

stacked_countries = data[data["year"] == 1995]
stacked_countries = stacked_countries[["country", "coal_electricity","coal_production","coal_consumption"]]

stacked_countries["Eletricidade"] = stacked_countries["coal_electricity"]
stacked_countries["Produção"] = stacked_countries["coal_production"]
stacked_countries["Consumo"] = stacked_countries["coal_consumption"]

coal_products = ["Eletricidade","Produção","Consumo"]

# Países que vão estar no gráfico
countries = ["Ukraine", "United States", "United Kingdom", "Spain", "South Korea", "Russia", "Poland", "Japan", "India", "Germany", "Canada", "Brazil"]

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
                     tooltips = "$name @country: @$name{1,11}")
coal_stacked.hbar_stack(coal_products,
                        y="country",
                        source=source,
                        color=cols,
                        height=0.5,
                        legend_label= coal_products)

coal_stacked.ygrid.grid_line_color = None
coal_stacked.legend.location = "top_right"
coal_stacked.legend.click_policy= "mute"
coal_stacked.axis.minor_tick_line_color = None
coal_stacked.outline_line_color = None
  
# Display Stack Graph
coal_stacked.legend.orientation = "horizontal"
show(coal_stacked)
