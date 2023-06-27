import geopandas as gpd
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource


shapefile = 'map_data/ne_110m_admin_0_countries.shp'
# Lendo o arquivo com o geopandas
gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]
# Renomeando as colunas
gdf.columns = ['country', 'country_code', 'geometry']

# Lendo os dados sobre energia
data = pd.read_csv("World Energy Consumption.csv")

# Retirando os continentes e organizações
map_data = data[~data["iso_code"].isnull()] 
map_data = map_data[map_data["country"] != "World"]

# Selecionando um ano
map_data = map_data[["country", "year","coal_electricity"]]
map_data = map_data[map_data["year"] == 2000]
print(map_data)
