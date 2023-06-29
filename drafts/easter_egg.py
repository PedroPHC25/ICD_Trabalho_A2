import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.plotting import show, save
from bokeh.models import Range1d, Label

easter_egg_data = pd.read_csv("dino.csv")

cds_easter_egg = ColumnDataSource(easter_egg_data)

graph_ds = figure(width = 800)

graph_ds.star(x = "x", 
              y = "y", 
              source = cds_easter_egg, 
              size = 13, 
              fill_color = "DeepPink")

graph_ds.toolbar.logo = None
graph_ds.toolbar.autohide = True

graph_ds.xgrid.grid_line_alpha = 0
graph_ds.ygrid.grid_line_alpha = 0
graph_ds.outline_line_color = None

graph_ds.xaxis.minor_tick_line_color = None
graph_ds.yaxis.minor_tick_line_color = None
graph_ds.xaxis.major_tick_line_color = None
graph_ds.yaxis.major_tick_line_color = None

graph_ds.axis.major_label_text_color = None
graph_ds.axis.axis_line_color = None

graph_ds.x_range = Range1d(start = -20, end = 100)

graph_ds.add_layout(Label(x = 0,
                          y = 30,
                          text = "Eu adoro\na EMAp",
                          text_font_size = "40px",
                          text_color = "DeepPink",
                          text_align = "center",
                          text_font = "fantasy"))

graph_ds.add_layout(Label(x = 10,
                          y = 0,
                          text = "Dos seus Pinholovers",
                          text_font_size = "15px",
                          text_color = "DeepPink",
                          text_align = "center",
                          text_font = "fantasy"))

save(graph_ds)