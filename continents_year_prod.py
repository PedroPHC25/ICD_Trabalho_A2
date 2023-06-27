import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot

# Gráfico da produção de energia dos continentes ao longo do tempo

output_file("continents.html")

# Lendo o arquivo csv
data = pd.read_csv("World Energy Consumption.csv")

# África
# Filtrando apenas os dados da África
africa_data = data[data["country"] == "Africa"]
# Convertendo o arquivo para CDS
source = ColumnDataSource(africa_data)
africa = figure(title="África", 
                x_axis_label="Ano", 
                y_axis_label="Produção de energia pelo carvão",
                )

# Linha do tempo com a produção anual de energia da África
africa.line(x= "year", 
            y="coal_production", 
            source=source, 
            line_color = "green")


# Oriente Médio
# Filtrando os dados
oriente_data = data[data["country"] == "Middle East"]
# Convertendo o arquivo para CDS
source = ColumnDataSource(oriente_data)
oriente = figure(title="Oriente Médio", 
                x_axis_label="Ano", 
                y_axis_label="Produção de energia pelo carvão",
                )
# Linha do tempo com a produção anual de energia do Oriente Médio
oriente.line(x= "year", 
             y="coal_production", 
             source=source,
             line_color = "red")


# Europa 
# Filtrando os dados
europa_data = data[data["country"] == "Europe"]
# Convertendo o arquivo para CDS
source = ColumnDataSource(europa_data)
europa = figure()
# Linha do tempo com a produção anual de energia da Europa
europa.line(x= "year", y="coal_production", source=source)

# América do norte
# Filtrando os dados 
am_norte_data = data[data["country"] == "North America"]
# Convertendo o arquivo para CDS
source = ColumnDataSource(am_norte_data)
am_norte = figure()
# Linha do tempo com a produção anual de energia da América do Norte
am_norte.line(x= "year", y="coal_production", source=source)


# Grid 2x2, com todas as linhas do tempo
grid = gridplot([[europa, africa], [am_norte, oriente]], width=500, height=300)

show(grid)