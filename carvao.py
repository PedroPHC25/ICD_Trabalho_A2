import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

#Gráfico da produção de energia dos continentes ao longo do tempo

output_file("output.html")

# Lendo o arquivo csv
csv = pd.read_csv("World Energy Consumption.csv")

# Africa
africa_data = csv[csv["country"] == "Africa"]

source = ColumnDataSource(africa_data)

africa = figure()
africa.line(x= "year", y="coal_production", source=source)



plot = figure()
plot.line(x= "year", y="coal_production", source=source)

show(africa)