from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.layouts import gridplot
import pandas as pd

#GRÁFICO DE LINHA CONSUMO PER CAPITA DE ELETRICIDADE DO VENTO PARA O BRASIL NOS ÚLTIMOS 50 ANOS

data = pd.read_csv("World Energy Consumption.csv") #Lendo o arquivo

#Filtrando os dados para o país "Brazil" nos últimos 50 anos:
df_filtered_country = data[(data['country'] == 'Brazil') & (data['year'] >= (data['year'].max() - 50))]

source = ColumnDataSource(df_filtered_country) #Criando o ColumnDataSource 

#Criando uma figura:
p1 = figure(title="      PER CAPITA CONSUMPTION OF ELECTRICITY GENERATED BY WIND IN BRAZIL IN THE LAST 50 YEARS",
           x_axis_label='YEAR', y_axis_label='WIND ENERGY CONSUMPTION (kWh)', width=1200, height=600)

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

#Configurando a saída para um arquivo HTML
output_file("linha_brazil.html")

#Exibindo o grid
show(p1)