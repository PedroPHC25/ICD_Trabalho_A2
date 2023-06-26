from bokeh.plotting import figure
from bokeh.models import Range1d
from bokeh.io import output_file, save, show
import pandas as pd
from bokeh.models import ColumnDataSource

nuclear = pd.read_csv("World Energy Consumption.csv")

print(nuclear)

output_file("nuclear_rascunho.html")

data_pib_nuclear_share_elec = {"x": nuclear["gdp"], "y": nuclear["nuclear_share_elec"]}

data_source = ColumnDataSource(data=data_pib_nuclear_share_elec )

scatterplot_gdp_nuclear_share = figure()

scatterplot_gdp_nuclear_share.circle(x = "x", y = "y", source = data_source)

show(scatterplot_gdp_nuclear_share)


