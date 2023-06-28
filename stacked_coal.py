from bokeh.models import ColumnDataSource
from bokeh.palettes import GnBu3, OrRd3
from bokeh.plotting import figure, show

# Gráfico de barras empilhadas 

output_file("continents.html")

# Lendo o arquivo csv
data = pd.read_csv("World Energy Consumption.csv")

# Categoria de cada parte da barra empilhada
coal_products = ["coal_electricity","coal_production","coal_consumption"]

stacked_countries = data[data["year"] == 1965]

countries = ["Ukraine", "Vietnam", "United States", "United Kingdom", "Turkey", "Thailand", "Spain", "South Korea", "Russia", "Poland", "New Zealand", "Mexico", "Japan", "India", "Germany", "Canada", "Brazil"]

for country in countries:
    stacked_countries = data[data["countries"] == country]
