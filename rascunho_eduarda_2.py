import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, ColorBar
from bokeh.transform import linear_cmap
from bokeh.palettes import Blues256

import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, ColorBar
from bokeh.transform import log_cmap
from bokeh.palettes import Blues256

# Leitura do arquivo CSV
data = pd.read_csv("World Energy Consumption.csv")

x = data['population']  # Selecionar a coluna 'population'
y = data['gdp']  # Selecionar a coluna 'gdp'
source = ColumnDataSource(dict(x=x, y=y))

def make_plot(mapper, palette):
    cmap = log_cmap(field_name="x", palette=palette, low=min(x), high=max(x))
    axis_type = "log"  # Definir a escala logarítmica

    p = figure(title=f"{palette} with {mapper.__name__}", toolbar_location=None, tools="", x_axis_type=axis_type, y_axis_type=axis_type)

    r = p.scatter('x', 'y', alpha=0.8, source=source, color=cmap)

    color_bar = ColorBar(color_mapper=cmap['transform'], location=(0, 0))
    p.add_layout(color_bar, 'right')

    return p

# Configurar a saída para um arquivo HTML
output_file("grafico.html")

# Chamar a função make_plot com os parâmetros desejados
p = make_plot(log_cmap, Blues256)

# Exibir o gráfico
show(p)



