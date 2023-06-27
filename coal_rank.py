import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

# Gráfico de barras com os maiores consumidores de energia vinda do carvão

output_file("rank_interativo.html")

# Lendo o arquivo csv
data = pd.read_csv("World Energy Consumption.csv")


# Filtrando os dados
rank = data[~data["iso_code"].isnull()] 

rank = rank[rank["country"] != "World"]

rank_int = rank[rank["year"] == 2015]

rank_int = rank_int.sort_values("coal_consumption", ascending= False)

rank_int = rank_int.head(5)

print(rank_int)

