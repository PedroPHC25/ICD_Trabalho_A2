from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.layouts import gridplot
import pandas as pd

#GRÁFICO DE BARRAS DE GERAÇÃO DE ELETRICIDADE A PARTIR DO VENTO POR PAÍS (MEDIDO EM TERAWATT-HORA)

data = pd.read_csv("World Energy Consumption.csv") #Lendo o arquivo
df_filtered = data[data['year'] == 2020] #Filtrando dados do ano de 2020

#Ordenando os valores de 'wind_electricity' em ordem decrescente
df_sorted = df_filtered.sort_values('wind_electricity', ascending=False)

#Selecionando os 10 maiores valores da coluna 'wind_electricity'
df_top_10 = df_sorted.head(10)

#Selecionando apenas as colunas desejadas ('country' e 'wind_electricity')
df_top_10_filtered = df_top_10[['country', 'wind_electricity']]

#Identificando o país com o maior valor de wind_electricity
pais_maior_geracao = df_top_10_filtered[df_top_10_filtered['wind_electricity'] == df_top_10_filtered['wind_electricity'].max()]['country'].iloc[0]

#Excluindo o país com o maior valor de wind_electricity
df_top_10_filtered = df_top_10_filtered[df_top_10_filtered['country'] != pais_maior_geracao]

#Criando ColumnDataSource
data_organized = ColumnDataSource(df_top_10_filtered)

#Criando a figura e plotando as barras
p = figure(x_range=df_top_10_filtered['country'], height=600, width=1200, 
           title="             ELECTRICITY GENERATION FROM WIND BY COUNTRY IN 2020")
p.vbar(x='country', top='wind_electricity', width=0.9, color="#A95974", source=data_organized)

#Ajustando os títulos dos eixos
p.xaxis.axis_label = "COUNTRY"
p.yaxis.axis_label = "ELECTRICITY GENERATION FROM WIND (TWh)"

p.title.text_font = "Georgia"  #Alterando a fonte do título 
p.title.text_font_size = "16pt"  #Alterando o tamanho da fonte do título 
p.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
p.title.text_align = "center"  #Alinhando o título no centro do gráfico

p.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
p.xaxis.axis_label_text_font_size = "16pt"  #Alterando o tamanho da fonte do rótulo do eixo x 
p.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x 
p.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

p.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
p.yaxis.axis_label_text_font_size = "16pt"  #Alterando o tamanho da fonte do rótulo do eixo y 
p.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
p.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

p.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico

