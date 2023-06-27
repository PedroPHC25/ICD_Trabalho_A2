from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
import pandas as pd
'''
#1: GRÁFICO DE BARRAS DE GERAÇÃO DE ELETRICIDADE A PARTIR DO VENTO POR PAÍS (MEDIDDO EM TERAWATT-HORA)

data = pd.read_csv("World Energy Consumption.csv") #Lendo o arquivo
df_filtered = data[data['year'] == 2020] #Filtrando dados do ano de 2020

# Ordenar os valores da coluna 'wind_electricity' em ordem decrescente
df_sorted = df_filtered.sort_values('wind_electricity', ascending=False)

# Selecionar os 10 maiores valores da coluna 'wind_electricity'
df_top_10 = df_sorted.head(10)

# Selecionar apenas as colunas desejadas ('country' e 'wind_electricity')
df_top_10_filtered = df_top_10[['country', 'wind_electricity']]

# Identificar o país com o maior valor de wind_electricity
pais_maior_geracao = df_top_10_filtered[df_top_10_filtered['wind_electricity'] == df_top_10_filtered['wind_electricity'].max()]['country'].iloc[0]

# Excluir o país com o maior valor de wind_electricity
df_top_10_filtered = df_top_10_filtered[df_top_10_filtered['country'] != pais_maior_geracao]

# Criar um ColumnDataSource com os dados organizados
data_organized = ColumnDataSource(df_top_10_filtered)

# Configurar a saída para um arquivo HTML
output_file("grafico_barras.html")

# Criar a figura
p = figure(x_range=df_top_10_filtered['country'], height=600, width=800, title="ELECTRICITY GENERATION FROM WIND BY COUNTRY IN 2020")

# Plotar as barras
p.vbar(x='country', top='wind_electricity', width=0.9, color="#022601", source=data_organized)

# Configurar rótulos e títulos dos eixos
p.xaxis.axis_label = "COUNTRY"
p.yaxis.axis_label = "ELECTRICITY GENERATION FROM WIND (TWh)"

p.title.text_font = "Georgia"  # Altera a fonte do título para Georgia
p.title.text_font_size = "16pt"  # Altera o tamanho da fonte do título para 14 pontos
p.title.text_color = "#0C3B40"  # Altera a cor do texto do título para vermelho
p.title.text_align = "center"  # Alinhando o título no centro do gráfico

p.xaxis.axis_label_text_font = "Georgia"  # Altera a fonte do rótulo do eixo x para Georgia
p.xaxis.axis_label_text_font_size = "16pt"  # Altera o tamanho da fonte do rótulo do eixo x para 12 pontos
p.xaxis.axis_label_text_color = "#0C3B40"  # Altera a cor do texto do rótulo do eixo x para azul
p.xaxis.major_label_text_font_style = "bold"  # Colocando em negrito os rótulos das escalas do eixo x

p.yaxis.axis_label_text_font = "Georgia"  # Altera a fonte do rótulo do eixo y para Georgia
p.yaxis.axis_label_text_font_size = "16pt"  # Altera o tamanho da fonte do rótulo do eixo y para 10 pontos
p.yaxis.axis_label_text_color = "#0C3B40"  # Altera a cor do texto do rótulo do eixo y para verde
p.yaxis.major_label_text_font_style = "bold"  # Colocando em negrito os rótulos das escalas do eixo y

p.background_fill_color = "#38ABF2"  # Altera a cor de fundo do gráfico 

# Exibir o gráfico
show(p)

#2: GRÁFICO DE LINHA CONSUMO PER CAPITA DE ELETRICIDADE DO VENTO( MEDIDA EM kWh)

# Leitura do arquivo CSV
data = pd.read_csv("World Energy Consumption.csv")

# Filtragem de dados para o país "Brazil" nos últimos 50 anos:
df_filtered_country = data[(data['country'] == 'Brazil') & (data['year'] >= (data['year'].max() - 50))]

# Criando o ColumnDataSource com os dados
source = ColumnDataSource(df_filtered_country)

# Configurando a saída para um arquivo HTML:
output_file("line_chart.html") 

# Criando uma figura:
p = figure(title="PER CAPITA CONSUMPTION OF ELECTRICITY GENERATED BY WIND IN BRAZIL IN THE LAST 50 YEARS",
           x_axis_label='YEAR', y_axis_label='PER CAPITA WIND ENERGY CONSUMPTION', width=1200, height=600)

# Plotando o gráfico de linha:
p.line('year', 'wind_energy_per_capita', line_width=4, source=source)

# Alterando o tamanho e a cor da linha:
p.line('year', 'wind_energy_per_capita', line_width=2, line_color="#0C3B40", source=source)

p.title.text_font = "Georgia"  # Altera a fonte do título para Georgia
p.title.text_font_size = "14pt"  # Altera o tamanho da fonte do título para 14 pontos
p.title.text_color = "#0C3B40"  # Altera a cor do texto do título para vermelho
p.title.text_align = "center"  # Alinhando o título no centro do gráfico

p.xaxis.axis_label_text_font = "Georgia"  # Altera a fonte do rótulo do eixo x para Georgia
p.xaxis.axis_label_text_font_size = "16pt"  # Altera o tamanho da fonte do rótulo do eixo x para 12 pontos
p.xaxis.axis_label_text_color = "#0C3B40"  # Altera a cor do texto do rótulo do eixo x para azul
p.xaxis.major_label_text_font_style = "bold"  # Colocando em negrito os rótulos das escalas do eixo x

p.yaxis.axis_label_text_font = "Georgia"  # Altera a fonte do rótulo do eixo y para Georgia
p.yaxis.axis_label_text_font_size = "16pt"  # Altera o tamanho da fonte do rótulo do eixo y para 10 pontos
p.yaxis.axis_label_text_color = "#0C3B40"  # Altera a cor do texto do rótulo do eixo y para verde
p.yaxis.major_label_text_font_style = "bold"  # Colocando em negrito os rótulos das escalas do eixo y

p.background_fill_color = "#38ABF2"  # Altera a cor de fundo do gráfico 


# Mostrando o gráfico:
show(p)

#GRÁFICO 3: VARIAÇÃO PERCENTUAL ANUAL NO CONSUMO DE VENTO, COMPARAÇÃO ENTRE BRASIL E ARGENTINA

data = pd.read_csv("World Energy Consumption.csv") #Lendo o arquivo
df_brazil = data[data['country'] == 'Brazil'] #Filtrando dados do Brasil
df_argentina = data[data['country'] == 'Argentina'] #Filtrando dados da Argentina

#Crie a figura para o gráfico:
p = figure(title="                                        ANNUAL PERCENTAGE CHANGE IN WIND CONSUMPTION", x_axis_label='YEAR', 
           y_axis_label='WIND ENERGY PER CAPITA',
           width=1200, height=600)

#Plote os gráficos de linha para cada país:
p.line(df_brazil['year'], df_brazil['wind_cons_change_pct'], line_width=6, color='#1A5AD9', legend_label='Brazil')
p.line(df_argentina['year'], df_argentina['wind_cons_change_pct'], line_width=4, color='#C2D918', legend_label='Argentina')

#Ajuste a legenda para mostrar os nomes dos países:
p.legend.location = "top_left"
p.legend.title = "COUNTRIES"

p.title.text_font = "Georgia"  # Altera a fonte do título para Georgia
p.title.text_font_size = "14pt"  # Altera o tamanho da fonte do título 
p.title.text_color = "#0C3B40"  # Altera a cor do texto do título 
p.title.text_align = "center"  # Alinhando o título no centro do gráfico
p.title.text_baseline = "middle"  # Alinhando o título verticalmente ao centro


p.xaxis.axis_label_text_font = "Georgia"  # Altera a fonte do rótulo do eixo x para Georgia
p.xaxis.axis_label_text_font_size = "16pt"  # Altera o tamanho da fonte do rótulo do eixo x 
p.xaxis.axis_label_text_color = "#0C3B40"  # Altera a cor do texto do rótulo do eixo x 
p.xaxis.major_label_text_font_style = "bold"  # Colocando em negrito os rótulos das escalas do eixo x

p.yaxis.axis_label_text_font = "Georgia"  # Altera a fonte do rótulo do eixo y para Georgia
p.yaxis.axis_label_text_font_size = "16pt"  # Altera o tamanho da fonte do rótulo do eixo y para 10 pontos
p.yaxis.axis_label_text_color = "#0C3B40"  # Altera a cor do texto do rótulo do eixo y para verde
p.yaxis.major_label_text_font_style = "bold"  # Colocando em negrito os rótulos das escalas do eixo y

p.background_fill_color = "#38ABF2"  # Altera a cor de fundo do gráfico


#Configure a saída para um arquivo HTML e mostre o gráfico:
output_file("line_chart2.html")
show(p)

'''
#GRÁFICO 4: DISPERSÃO 

import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import Slope
from sklearn.linear_model import RANSACRegressor

# Leitura do arquivo CSV
data = pd.read_csv("World Energy Consumption.csv")

# Filtrar os dados para o ano de 2000
df_filtered_year = data[data['year'] == 2000]

# Remover linhas com valores NaN
df_filtered_year = df_filtered_year.dropna(subset=['wind_energy_per_capita'])

# Verificar se há linhas restantes após a remoção de NaN
if df_filtered_year.empty:
    raise ValueError("Não há dados válidos para a regressão.")

# Criar a figura
p = figure(height=400, width=600, title="Relação entre Wind Elec per Capita e Wind Energy per Capita")

# Plotar o gráfico de dispersão
p.scatter(x='wind_elec_per_capita', y='wind_energy_per_capita', source=df_filtered_year)

# Configurar rótulos e títulos dos eixos
p.xaxis.axis_label = "Wind Elec per Capita"
p.yaxis.axis_label = "Wind Energy per Capita"

# Aplicar regressão RANSAC
ransac = RANSACRegressor()
x = df_filtered_year['wind_elec_per_capita'].values.reshape(-1, 1)
y = df_filtered_year['wind_energy_per_capita'].values.reshape(-1, 1)
ransac.fit(x, y)

# Calcular a reta de regressão
slope = ransac.estimator_.coef_[0][0]
intercept = ransac.estimator_.intercept_[0]

# Criar a reta de regressão
x_line = np.array([df_filtered_year['wind_elec_per_capita'].min(), df_filtered_year['wind_elec_per_capita'].max()])
y_line = slope * x_line + intercept
regression_line = Slope(gradient=slope, y_intercept=intercept, line_color='red', line_width=2)

# Adicionar a reta de regressão ao gráfico
p.add_layout(regression_line)

p.title.text_font = "Georgia"  # Altera a fonte do título para Georgia
p.title.text_font_size = "14pt"  # Altera o tamanho da fonte do título 
p.title.text_color = "#0C3B40"  # Altera a cor do texto do título 
p.title.text_align = "center"  # Alinhando o título no centro do gráfico
p.title.text_baseline = "middle"  # Alinhando o título verticalmente ao centro


p.xaxis.axis_label_text_font = "Georgia"  # Altera a fonte do rótulo do eixo x para Georgia
p.xaxis.axis_label_text_font_size = "16pt"  # Altera o tamanho da fonte do rótulo do eixo x 
p.xaxis.axis_label_text_color = "#0C3B40"  # Altera a cor do texto do rótulo do eixo x 
p.xaxis.major_label_text_font_style = "bold"  # Colocando em negrito os rótulos das escalas do eixo x

p.yaxis.axis_label_text_font = "Georgia"  # Altera a fonte do rótulo do eixo y para Georgia
p.yaxis.axis_label_text_font_size = "16pt"  # Altera o tamanho da fonte do rótulo do eixo y para 10 pontos
p.yaxis.axis_label_text_color = "#0C3B40"  # Altera a cor do texto do rótulo do eixo y para verde
p.yaxis.major_label_text_font_style = "bold"  # Colocando em negrito os rótulos das escalas do eixo y

p.background_fill_color = "#38ABF2"  # Altera a cor de fundo do gráfico

# Configurar a saída para um arquivo HTML
output_file("scatter_plot.html")

# Exibir o gráfico
show(p)
