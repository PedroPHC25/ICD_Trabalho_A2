import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

output_file("output.html")

csv = pd.read_csv("World Energy Consumption.csv")

source = ColumnDataSource(csv)

plot = figure()
plot.line(x= "year", y="coal_production", source=source)

show(plot)