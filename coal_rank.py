from bokeh.plotting import figure, curdoc, output_file, show
from bokeh.models import ColumnDataSource, Slider, HoverTool, Range1d
from bokeh.layouts import column
from cds_generator import data_countries, coal_rank_data, cds_coal_rank_data

# Gráfico de barras interativo com os maiores consumidores de energia vinda do carvão

output_file("coal_bar_rank.html")
# Construção do gráfico de barras
rank = figure(x_range = coal_rank_data["country"], tools = "")

# Customizando as legendas e os eixos
rank.axis.axis_label_text_font_style = "bold"

rank.xaxis.axis_label = "Países"
rank.xaxis.axis_label_text_font_size = "20px"

rank.yaxis.axis_label = "Consumo (TWh)"
rank.yaxis.axis_label_text_font_size = "20px"
rank.y_range = Range1d(start=0, end = 24000)

# Colocando o hover
hover = HoverTool(tooltips = [("Consumo", "@coal_consumption{1,11}")])
rank.add_tools(hover)
rank.toolbar.logo = None

# Customização da proporção, grid e eixos
rank.height = 550
rank.width = 1000
rank.xgrid.grid_line_color = None
rank.ygrid.grid_line_color = None
rank.toolbar_location = None
rank.title = "Maiores consumidores da energia primária vinda do carvão"

# Gráfico de barras
verde = "#009900"
rank.vbar(x="country", top="coal_consumption", width=0.5, source=cds_coal_rank_data, color = verde )

# Função de atualização do gráfico com base no valor do slider
def update_plot(attr, old, new):
    year = year_slider.value
    new_data = data_countries[data_countries["year"] == year]
    new_data = new_data.sort_values("coal_consumption", ascending=False)
    new_data = new_data[["country", "year", "coal_consumption"]]
    new_data = new_data.head(10)
    cds_coal_rank_data.data = ColumnDataSource.from_df(new_data)
    rank.x_range.factors = list(new_data["country"])

# Criando o slider
initial_year = 1965
year_slider = Slider(title="Ano", start=1965, end=2019, step=1, value=initial_year)
year_slider.on_change('value', update_plot)

# Combinando o gráfico e o slider em uma única figura
layout = column(year_slider, rank)

# Adicionando o layout à aplicação
curdoc().add_root(layout)

show(layout)
