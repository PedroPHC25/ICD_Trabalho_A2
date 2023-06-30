import pandas as pd
from bokeh.models import ColumnDataSource

data = pd.read_csv("World Energy Consumption.csv")



### PETRÓLEO ###


## Gráfico de linhas "Produção de petróleo das 5 maiores regiões produtoras (1900 - 2020)" ##

# Gerando CDSs apenas com os dados das regiões mais produtoras de petróleo (África, Ásia, Oriente Médio, América do Norte e Américas Central e do Sul)
cds_oil_africa = ColumnDataSource(data[data["country"] == "Africa"])
cds_oil_asia = ColumnDataSource(data[data["country"] == "Asia Pacific"])
cds_oil_middle_east = ColumnDataSource(data[data["country"] == "Middle East"])
cds_oil_north_america = ColumnDataSource(data[data["country"] == "North America"])
cds_oil_south_and_central_america = ColumnDataSource(data[data["country"] == "South & Central America"])


## Gráfico de dispersão "Consumo de petróleo x População em 2019" ##

# Gerando um dataframe apenas com os dados dos países, sem os continentes ou o mundo
data_countries = data.loc[data["country"] != "World"].dropna(subset = ["iso_code"])

# Criando uma nova coluna com a média de consumo de petróleo em função da população
data_countries["oil_mean_consumption"] = data_countries["oil_consumption"]/data_countries["population"]

# Gerando dataframes cujos países possuem um consumo de petróleo acima e abaixo da média mundial em 2019, valor esse calculado a partir da divisão do consumo pela população
data_2019_high_consumption = data_countries.loc[data_countries["year"] == 2019].loc[data_countries["oil_mean_consumption"] > 53619.925/7713467904]
data_2019_low_consumption = data_countries.loc[data_countries["year"] == 2019].loc[data_countries["oil_mean_consumption"] < 53619.925/7713467904]

# Gerando CDSs com os dados de 2019 separados com base no consumo de petróleo do país
cds_oil_2019_high_consumption = ColumnDataSource(data_2019_high_consumption)
cds_oil_2019_low_consumption = ColumnDataSource(data_2019_low_consumption)


## Grid de barras "Variação anual da produção de petróleo dos 3 maiores produtores mundiais (1900 - 2020)" ##

# Gerando tabelas filtradas referentes aos dados dos 3 maiores produtores de petróleo (Estados Unidos, Rússia e Arábia Saudita), separados por anos em que a variação na produção foi positiva e negativa
data_positive_united_states = data.loc[data["country"] == "United States"].loc[data["oil_prod_change_twh"] > 0]
data_positive_russia = data.loc[data["country"] == "Russia"].loc[data["oil_prod_change_twh"] > 0]
data_positive_saudi_arabia = data.loc[data["country"] == "Saudi Arabia"].loc[data["oil_prod_change_twh"] > 0]
data_negative_united_states = data.loc[data["country"] == "United States"].loc[data["oil_prod_change_twh"] < 0]
data_negative_russia = data.loc[data["country"] == "Russia"].loc[data["oil_prod_change_twh"] < 0]
data_negative_saudi_arabia = data.loc[data["country"] == "Saudi Arabia"].loc[data["oil_prod_change_twh"] < 0]

# Gerando CDSs apenas com os dados dos 3 maiores produtores de petróleo (Estados Unidos, Rússia e Arábia Saudita), separados por anos em que a produção aumentou ou diminuiu
cds_oil_positive_united_states = ColumnDataSource(data_positive_united_states)
cds_oil_positive_russia = ColumnDataSource(data_positive_russia)
cds_oil_positive_saudi_arabia = ColumnDataSource(data_positive_saudi_arabia)
cds_oil_negative_united_states = ColumnDataSource(data_negative_united_states)
cds_oil_negative_russia = ColumnDataSource(data_negative_russia)
cds_oil_negative_saudi_arabia = ColumnDataSource(data_negative_saudi_arabia)



### ENERGIA EÓLICA ###


## Grid de linhas "ANNUAL PERCENTAGE CHANGE IN WIND CONSUMPTION" ##

#Filtrando dados de cada país
df_brazil = data[data['country'] == 'Brazil'] #Filtrando dados do Brasil
df_india = data[data['country'] == 'India'] #Filtrando dados da India
df_argentina = data[data['country'] == 'Argentina'] #Filtrando dados da Argentina
df_china = data[data['country'] == 'China'] #Filtrando dados da China
df_united = data[data['country'] == 'United States'] #Filtrando dados dos Estados Unidos 
df_germany = data[data['country'] == 'Germany'] #Filtrando dados da Alemanha
df_kingdom = data[data['country'] == 'United Kingdom'] #Filtrando dados do Reino Unido

# Criando a origem de dados
source_brazil = ColumnDataSource(df_brazil)
source_india = ColumnDataSource(df_india)
source_argentina = ColumnDataSource(df_argentina)
source_china = ColumnDataSource(df_china)
source_united = ColumnDataSource(df_united)
source_germany = ColumnDataSource(df_germany)
source_kingdom = ColumnDataSource(df_kingdom)


# Gráfico de barras "ELECTRICITY GENERATION FROM WIND BY COUNTRY IN 2020" ##

# Filtrando dados por ano 
df_filtered_year_2020 = data[data['year'] == 2020]
df_filtered_year_2000 = data[data['year'] == 2000]

# Ordenando os valores de 'wind_electricity' em ordem decrescente
df_sorted = df_filtered_year_2020.sort_values('wind_electricity', ascending=False)

# Selecionando os 10 maiores valores da coluna 'wind_electricity'
df_top_10 = df_sorted.head(10)

# Selecionando apenas as colunas desejadas ('country' e 'wind_electricity')
df_top_10_filtered = df_top_10[['country', 'wind_electricity']]

#Identificando o país com o maior valor de wind_electricity
country_top_generation = df_top_10_filtered[df_top_10_filtered['wind_electricity'] == df_top_10_filtered['wind_electricity'].max()]['country'].iloc[0]

#Excluindo o país com o maior valor de wind_electricity
df_top_10_filtered = df_top_10_filtered[df_top_10_filtered['country'] != country_top_generation]

# Adicionando cada cor a um continente
df_top_10_filtered["continent"] = ["Asia", "America", "Europe", "Europe", "Asia", "America", "Europe", "Europe", "America"]
color_dict = {"America": "#87864D", "Europe": "#D49495", "Asia": "#8A5556"}
colors = [color_dict[continent] for continent in df_top_10_filtered["continent"]]
df_top_10_filtered["color"] = colors

# Criando ColumnDataSource
create_column_data_source_top_10_filtered = ColumnDataSource(df_top_10_filtered)


## Grid de dispersão "RATIO BETWEEN WIND ELECTRICITY AND WIND ENERGY (BOTH PER CAPITA)" ##

# Removendo linhas com valores NaN
df_filtered_year = df_filtered_year_2000.dropna(subset=['wind_energy_per_capita'])

# Verificando se há linhas restantes após a remoção de NaN
if df_filtered_year.empty:
    raise ValueError("Não há dados válidos para a regressão.")

# Removendo outliers usando o método IQR
Q1 = df_filtered_year['wind_energy_per_capita'].quantile(0.25)
Q3 = df_filtered_year['wind_energy_per_capita'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR
df_filtered_year = df_filtered_year[(df_filtered_year['wind_energy_per_capita'] >= lower_limit) & (df_filtered_year['wind_energy_per_capita'] <= upper_limit)]

# Criando o ColumnDataSource
create_column_data_source_df_filtered_year = ColumnDataSource(df_filtered_year)


## Gráfico de linha "PER CAPITA CONSUMPTION OF ELECTRICITY GENERATED BY WIND IN BRAZIL IN THE LAST 50 YEARS" ##

#Filtrando os dados para o país "Brazil" nos últimos 50 anos:
df_filtered_country = data[(data['country'] == 'Brazil') & (data['year'] >= (data['year'].max() - 50))]

df_wind_graph_line = ColumnDataSource(df_filtered_country)



### ENERGIA NUCLEAR ###


## Gráfico de bolhas "Energia nuclear por PIB em 2000"

#  Seleciona os dados do ano 2000
data_nuclear_2000 = data_countries.loc[data_countries["year"]==2000]
data_nuclear_2000["gdp_in_bi"] = data_nuclear_2000["gdp"]/ 1000000000

# Cria um dicionário que corresponde x, y e z com as colunas 'gdp_in_bi', 'nuclear_share_energy' e 'country', do dataframe 'data_nuclear_2000'.
# E gera o ColumnDataSource com esse dicionário.
data_gdp_nuclear = {"x": data_nuclear_2000["gdp_in_bi"], 
                    "y": data_nuclear_2000["nuclear_share_energy"], 
                    "z": data_nuclear_2000["country"]}

cds_nuclear_gdp_share_country = ColumnDataSource(data=data_gdp_nuclear)


## Grid de linhas "6 países que mais produzem energia nuclear (1985-2020)" ##

cds_nuclear_eua = ColumnDataSource(data=data[data["country"]=="United States"]) #Cria o ColumnDataSource apenas com os EUA
cds_nuclear_france = ColumnDataSource(data= data[data["country"]=="France"])
cds_nuclear_japan = ColumnDataSource(data= data[data["country"]=="Japan"])
cds_nuclear_germany = ColumnDataSource(data= data[data["country"]=="Germany"])
cds_nuclear_russia = ColumnDataSource(data= data[data["country"]=="Russia"])
cds_nuclear_korea = ColumnDataSource(data= data[data["country"]=="South Korea"])


## Gráfico de barras "Os 10 países que mais consumiram energia nuclear em 2018" ##

# Filtrando os dados

# Selecionando um ano
best_countries_nuclear = data_countries[data_countries["year"] == 2018]

# Ordenando e selecionando as colunas desejadas
best_countries_nuclear = best_countries_nuclear.sort_values("nuclear_consumption", ascending= False)
best_countries_nuclear_nuclear = best_countries_nuclear[["country", "year", "nuclear_consumption"]]
best_countries_nuclear = best_countries_nuclear.head(10)

#Adicionando cada cor à um continente
best_countries_nuclear["continent"] = ["América do norte", "Europa", "Ásia", "Ásia", "Ásia", "América do norte", "Europa", "Europa", "Europa", "Europa"]
color_dict = {"América do norte":"Tomato", "Europa":"SteelBlue", "Ásia": "Khaki"}
colors = []

for each_element in best_countries_nuclear["continent"]:
    colors.append(color_dict[each_element])

best_countries_nuclear["color"] = colors

#Gera os ColumnDataSources 
data_europe = ColumnDataSource(best_countries_nuclear[best_countries_nuclear["continent"] == "Europa"])
data_asia = ColumnDataSource(best_countries_nuclear[best_countries_nuclear["continent"] == "Ásia"])
data_america = ColumnDataSource(best_countries_nuclear[best_countries_nuclear["continent"] == "América do norte"])



### CARVÃO ###


## Grid de linhas "Comparação entre continentes da produção de energia a partir do carvão" ##

# África
# Filtrando apenas os dados da África
coal_africa_data = data[data["country"] == "Africa"]
coal_africa_data = ColumnDataSource(coal_africa_data)

# Oriente Médio
# Filtrando os dados
coal_sc_am_data = data[data["country"] == "South & Central America"]
coal_sc_am_data = ColumnDataSource(coal_sc_am_data)

# Europa 
# Filtrando os dados
coal_europa_data = data[data["country"] == "Europe"]
# Convertendo o arquivo para CDS
coal_europa_data = ColumnDataSource(coal_europa_data)

# América do norte
# Filtrando os dados 
coal_am_norte_data = data[data["country"] == "North America"]
# Convertendo o arquivo para CDS
coal_am_norte_data = ColumnDataSource(coal_am_norte_data)


## Gráfico de barras empilhadas "Atividades a partir do carvão em 1995 (em TWh)"

# Filtrando a base de dados
coal_stacked_countries = data[data["year"] == 1995]
coal_stacked_countries = coal_stacked_countries[["country", "coal_electricity","coal_production","coal_consumption"]]

# Renomenando as colunas
coal_stacked_countries["Eletricidade"] = coal_stacked_countries["coal_electricity"]
coal_stacked_countries["Produção"] = coal_stacked_countries["coal_production"]
coal_stacked_countries["Consumo"] = coal_stacked_countries["coal_consumption"]

# Categoria de cada parte da barra empilhada
coal_products = ["Produção","Consumo","Eletricidade"]

# Países que vão estar no gráfico
countries = ["China","United States", "India", "Russia", "Germany", "Poland", "Japan", "Ukraine", "United Kingdom", "Canada", "South Korea", "Spain", "Brazil"]

# Colocando no dataframe só os países da lista acima
coal_stacked_countries.set_index("country", inplace = True)
coal_stacked_countries = coal_stacked_countries.loc[countries]
coal_stacked_countries.reset_index(inplace= True)

cds_coal_stacked = ColumnDataSource(coal_stacked_countries)


## Gráfico de barras "Maiores consumidores de energia primária a partir do carvão (1965-2019)" ##

# Selecionando um ano
coal_rank_data = data_countries[data_countries["year"] == 1965]

# Ordenando e selecionando as colunas desejadas
coal_rank_data = coal_rank_data.sort_values("coal_consumption", ascending= False)
coal_rank_data = coal_rank_data[["country", "year", "coal_consumption"]]
coal_rank_data = coal_rank_data.head(10)

cds_coal_rank_data = ColumnDataSource(coal_rank_data)