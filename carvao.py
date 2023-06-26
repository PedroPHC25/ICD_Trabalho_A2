import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

#Gráfico da produção de energia dos continentes ao longo do tempo

output_file("output.html")

# Lendo o arquivo csv
csv = pd.read_csv("World Energy Consumption.csv")

# África
africa_data = csv[csv["country"] == "Africa"]

source = ColumnDataSource(africa_data)

africa = figure()
africa.line(x= "year", y="coal_production", source=source)

# Oriente Médio
om_data = csv[csv["country"] == "Middle East"]

source = ColumnDataSource(om_data)

oriente = figure()
oriente.line(x= "year", y="coal_production", source=source)

# Europa 
europa_data = csv[csv["country"] == "Europe"]

source = ColumnDataSource(europa_data)

europa = figure()
europa.line(x= "year", y="coal_production", source=source)

# América do norte
am_norte_data = csv[csv["country"] == "North America"]

source = ColumnDataSource(am_norte_data)

am_norte = figure()
am_norte.line(x= "year", y="coal_production", source=source)


plot = figure()
plot.line(x= "year", y="coal_production", source=source)

show(am_norte)