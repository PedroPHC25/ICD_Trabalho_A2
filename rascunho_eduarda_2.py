import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource
from bokeh.transform import linear_cmap
from bokeh.palettes import Blues256

import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, ColorBar
from bokeh.transform import linear_cmap
from bokeh.palettes import Blues256

# Leitura do arquivo CSV
data = pd.read_csv("World Energy Consumption.csv")

x = data['population']  # Selecionar a coluna 'population'
y = data['gdp']  # Selecionar a coluna 'gdp'
source = ColumnDataSource(dict(x=x, y=y))

def make_plot(mapper, palette):
    cmap = linear_cmap(field_name="x", palette=palette, low=min(x), high=max(x))
    axis_type = mapper.__name__.split("_")[0]  # linear or log

    p = figure(x_range=(min(x), max(x)), title=f"{palette} with {mapper.__name__}",
               toolbar_location=None, tools="", x_axis_type=axis_type)

    r = p.scatter('x', 'y', alpha=0.8, source=source, color=cmap)

    color_bar = ColorBar(color_mapper=cmap['transform'], location=(0, 0))
    p.add_layout(color_bar, 'right')

    return p

# Configurar a saída para um arquivo HTML
output_file("grafico.html")

# Chamar a função make_plot com os parâmetros desejados
p = make_plot(linear_cmap, Blues256)

# Exibir o gráfico
show(p)

