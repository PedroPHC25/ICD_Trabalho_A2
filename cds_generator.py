import pandas as pd
from bokeh.models import ColumnDataSource

data = pd.read_csv("World Energy Consumption.csv")

# Gerando um dataframe apenas com os dados dos países, sem os continentes ou o mundo
data_countries = data.loc[data["country"] != "World"].dropna(subset = ["iso_code"])

# Criando uma nova coluna com a média de consumo de petróleo em função da população
data_countries["oil_mean_consumption"] = data_countries["oil_consumption"]/data_countries["population"]

# Gerando dataframes cujos países possuem um consumo de petróleo acima e abaixo da média mundial em 2019, valor esse calculado a partir da divisão do consumo pela população
data_2019_high_consumption = data_countries.loc[data_countries["year"] == 2019].loc[data_countries["oil_mean_consumption"] > 53619.925/7713467904]
data_2019_low_consumption = data_countries.loc[data_countries["year"] == 2019].loc[data_countries["oil_mean_consumption"] < 53619.925/7713467904]

# Gerando tabelas filtradas referentes aos dados dos 3 maiores produtores de petróleo (Estados Unidos, Rússia e Arábia Saudita), separados por anos em que a variação na produção foi positiva e negativa
data_positive_united_states = data.loc[data["country"] == "United States"].loc[data["oil_prod_change_twh"] > 0]
data_positive_russia = data.loc[data["country"] == "Russia"].loc[data["oil_prod_change_twh"] > 0]
data_positive_saudi_arabia = data.loc[data["country"] == "Saudi Arabia"].loc[data["oil_prod_change_twh"] > 0]
data_negative_united_states = data.loc[data["country"] == "United States"].loc[data["oil_prod_change_twh"] < 0]
data_negative_russia = data.loc[data["country"] == "Russia"].loc[data["oil_prod_change_twh"] < 0]
data_negative_saudi_arabia = data.loc[data["country"] == "Saudi Arabia"].loc[data["oil_prod_change_twh"] < 0]

# Gerando CDSs com os dados de 2019 separados com base no consumo de petróleo do país
cds_oil_2019_high_consumption = ColumnDataSource(data_2019_high_consumption)
cds_oil_2019_low_consumption = ColumnDataSource(data_2019_low_consumption)

# Gerando CDSs apenas com os dados dos 3 maiores produtores de petróleo (Estados Unidos, Rússia e Arábia Saudita), separados por anos em que a produção aumentou ou diminuiu
cds_oil_positive_united_states = ColumnDataSource(data_positive_united_states)
cds_oil_positive_russia = ColumnDataSource(data_positive_russia)
cds_oil_positive_saudi_arabia = ColumnDataSource(data_positive_saudi_arabia)
cds_oil_negative_united_states = ColumnDataSource(data_negative_united_states)
cds_oil_negative_russia = ColumnDataSource(data_negative_russia)
cds_oil_negative_saudi_arabia = ColumnDataSource(data_negative_saudi_arabia)

# Gerando CDSs apenas com os dados das regiões mais produtoras de petróleo (África, Ásia, Oriente Médio, América do Norte e Américas Central e do Sul)
cds_oil_africa = ColumnDataSource(data[data["country"] == "Africa"])
cds_oil_asia = ColumnDataSource(data[data["country"] == "Asia Pacific"])
cds_oil_middle_east = ColumnDataSource(data[data["country"] == "Middle East"])
cds_oil_north_america = ColumnDataSource(data[data["country"] == "North America"])
cds_oil_south_and_central_america = ColumnDataSource(data[data["country"] == "South & Central America"])