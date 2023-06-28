from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.layouts import gridplot
import pandas as pd

#1:GRÁFICO DE LINHA CONSUMO PER CAPITA DE ELETRICIDADE DO VENTO PARA O BRASIL NOS ÚLTIMOS 50 ANOS

data = pd.read_csv("World Energy Consumption.csv") #Lendo o arquivo

#Filtrando os dados para o país "Brazil" nos últimos 50 anos:
df_filtered_country = data[(data['country'] == 'Brazil') & (data['year'] >= (data['year'].max() - 50))]

source = ColumnDataSource(df_filtered_country) #Criando o ColumnDataSource 

#Criando uma figura:
p1 = figure(title="      PER CAPITA CONSUMPTION OF ELECTRICITY GENERATED BY WIND IN BRAZIL IN THE LAST 50 YEARS",
           x_axis_label='YEAR', y_axis_label='PER CAPITA WIND ENERGY CONSUMPTION (MEDIDA EM kWh)', width=1200, height=600)

# Plotando o gráfico de linha:
p1.line('year', 'wind_energy_per_capita', line_width=6, line_color="#8A5556", source=source)

p1.title.text_font = "Georgia"  #Alterando a fonte do título 
p1.title.text_font_size = "14pt"  #Alterando o tamanho da fonte do título 
p1.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
p1.title.text_align = "center"  #Alinhando o título no centro do gráfico

p1.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
p1.xaxis.axis_label_text_font_size = "16pt"  #Alterando o tamanho da fonte do rótulo do eixo x 
p1.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x
p1.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

p1.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
p1.yaxis.axis_label_text_font_size = "16pt"  #Alterando o tamanho da fonte do rótulo do eixo y
p1.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
p1.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

p1.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico 


#2: GRÁFICO DE LINHA  VARIAÇÃO PERCENTUAL ANUAL NO CONSUMO DE VENTO, BRASIL E ARGENTINA

data = pd.read_csv("World Energy Consumption.csv") #Lendo o arquivo
df_brazil = data[data['country'] == 'Brazil'] #Filtrando dados do Brasil
df_argentina = data[data['country'] == 'Argentina'] #Filtrando dados da Argentina

#Criando a figura:
p2 = figure(title="                                          ANNUAL PERCENTAGE CHANGE IN WIND CONSUMPTION", 
            x_axis_label='YEAR', 
           y_axis_label='WIND ENERGY PER CAPITA',
           width=1200, height=600)

#Plotando os gráficos de linha para cada país:
p2.line(df_brazil['year'], df_brazil['wind_cons_change_pct'], line_width=6, color='#D49495', legend_label='Brazil')
p2.line(df_argentina['year'], df_argentina['wind_cons_change_pct'], line_width=4, color='#8A5556', legend_label='Argentina')

#Ajustando a legenda:
p2.legend.location = "top_left"
p2.legend.title = "COUNTRIES"

p2.title.text_font = "Georgia"  #Alterando a fonte do título 
p2.title.text_font_size = "14pt"  #Alterando o tamanho da fonte do título 
p2.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
p2.title.text_align = "center"  #Alinhando o título no centro do gráfico
p2.title.text_baseline = "middle"  #Alinhando o título verticalmente ao centro


p2.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
p2.xaxis.axis_label_text_font_size = "16pt"  #Alterando o tamanho da fonte do rótulo do eixo x 
p2.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x 
p2.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

p2.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
p2.yaxis.axis_label_text_font_size = "16pt"  #Alterando o tamanho da fonte do rótulo do eixo y 
p2.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
p2.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

p2.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico


#3:

data = pd.read_csv("World Energy Consumption.csv") #Lendo o arquivo
df_brazil = data[data['country'] == 'Brazil'] #Filtrando dados do Brasil
df_argentina = data[data['country'] == 'China'] #Filtrando dados da Argentina

#Criando a figura:
p3 = figure(title="                                          ANNUAL PERCENTAGE CHANGE IN WIND CONSUMPTION", 
            x_axis_label='YEAR', 
           y_axis_label='WIND ENERGY PER CAPITA',
           width=1200, height=600)

#Plotando os gráficos de linha para cada país:
p3.line(df_brazil['year'], df_brazil['wind_cons_change_pct'], line_width=6, color='#D49495', legend_label='Brazil')
p3.line(df_argentina['year'], df_argentina['wind_cons_change_pct'], line_width=4, color='#8A5556', legend_label='China')

#Ajustando a legenda:
p3.legend.location = "top_left"
p3.legend.title = "COUNTRIES"

p3.title.text_font = "Georgia"  #Alterando a fonte do título 
p3.title.text_font_size = "14pt"  #Alterando o tamanho da fonte do título 
p3.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
p3.title.text_align = "center"  #Alinhando o título no centro do gráfico
p3.title.text_baseline = "middle"  #Alinhando o título verticalmente ao centro


p3.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
p3.xaxis.axis_label_text_font_size = "16pt"  #Alterando o tamanho da fonte do rótulo do eixo x 
p3.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x 
p3.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

p3.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
p3.yaxis.axis_label_text_font_size = "16pt"  #Alterando o tamanho da fonte do rótulo do eixo y 
p3.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
p3.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

p3.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico

#4:
data = pd.read_csv("World Energy Consumption.csv") #Lendo o arquivo
df_brazil = data[data['country'] == 'Brazil'] #Filtrando dados do Brasil
df_argentina = data[data['country'] == 'United States'] #Filtrando dados da Argentina

#Criando a figura:
p4 = figure(title="                                          ANNUAL PERCENTAGE CHANGE IN WIND CONSUMPTION", 
            x_axis_label='YEAR', 
           y_axis_label='WIND ENERGY PER CAPITA',
           width=1200, height=600)

#Plotando os gráficos de linha para cada país:
p4.line(df_brazil['year'], df_brazil['wind_cons_change_pct'], line_width=6, color='#D49495', legend_label='Brazil')
p4.line(df_argentina['year'], df_argentina['wind_cons_change_pct'], line_width=4, color='#8A5556', legend_label='United States')

#Ajustando a legenda:
p4.legend.location = "top_left"
p4.legend.title = "COUNTRIES"

p4.title.text_font = "Georgia"  #Alterando a fonte do título 
p4.title.text_font_size = "14pt"  #Alterando o tamanho da fonte do título 
p4.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
p4.title.text_align = "center"  #Alinhando o título no centro do gráfico
p4.title.text_baseline = "middle"  #Alinhando o título verticalmente ao centro


p4.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
p4.xaxis.axis_label_text_font_size = "16pt"  #Alterando o tamanho da fonte do rótulo do eixo x 
p4.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x 
p4.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

p4.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
p4.yaxis.axis_label_text_font_size = "16pt"  #Alterando o tamanho da fonte do rótulo do eixo y 
p4.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
p4.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

p4.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico













#Criando um grid com os 4 gráficos
grid = gridplot([[p1], [p2], [p3], [p4]])

#Configurando a saída para um arquivo HTML
output_file("grid.html")

#Exibindo o grid
show(grid)