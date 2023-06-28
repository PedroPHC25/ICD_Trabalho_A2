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

stacked_countries = data[data["year"] == 2005]
stacked_countries = stacked_countries[["country", "coal_electricity","coal_production","coal_consumption"]]

# Países que vão estar no gráfico
countries = ["Ukraine","Vietnam", "United States", "United Kingdom", "Turkey", "Thailand", "Spain", "South Korea", "Russia", "Poland", "New Zealand", "Mexico", "Japan", "India", "Germany", "Canada", "Brazil"]

stacked_countries.set_index("country", inplace = True)
stacked_countries = stacked_countries.loc[countries]

print(stacked_countries)
