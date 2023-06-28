from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.layouts import gridplot
import pandas as pd

#GRÁFICOS DE LINHA  VARIAÇÃO PERCENTUAL ANUAL NO CONSUMO DE VENTO

#1: BRASIL E INDIA 

data = pd.read_csv("World Energy Consumption.csv") #Lendo o arquivo
df_brazil = data[data['country'] == 'Brazil'] #Filtrando dados do Brasil
df_india = data[data['country'] == 'India'] #Filtrando dados da India

#Criando a figura:
p1 = figure(title="ANNUAL PERCENTAGE CHANGE IN WIND CONSUMPTION", 
            x_axis_label='YEAR', 
           y_axis_label='WIND ENERGY PER CAPITA',
           width=600, height=300)

#Plotando os gráficos de linha para cada país:
p1.line(df_brazil['year'], df_brazil['wind_cons_change_pct'], line_width=6, color='#D49495', legend_label='Brazil')
p1.line(df_india['year'], df_india['wind_cons_change_pct'], line_width=4, color='#8A5556', legend_label='India')

#Ajustando a legenda:
p1.legend.location = "top_left"
p1.legend.title = "COUNTRIES"

p1.title.text_font = "Georgia"  #Alterando a fonte do título 
p1.title.text_font_size = "10pt"  #Alterando o tamanho da fonte do título 
p1.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
p1.title.text_align = "center"  #Alinhando o título no centro do gráfico
p1.title.text_baseline = "middle"  #Alinhando o título verticalmente ao centro


p1.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
p1.xaxis.axis_label_text_font_size = "10pt"  #Alterando o tamanho da fonte do rótulo do eixo x 
p1.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x 
p1.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

p1.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
p1.yaxis.axis_label_text_font_size = "10pt"  #Alterando o tamanho da fonte do rótulo do eixo y 
p1.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
p1.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

p1.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico


#2: BRASIL E ARGENTINA

data = pd.read_csv("World Energy Consumption.csv") #Lendo o arquivo
df_brazil = data[data['country'] == 'Brazil'] #Filtrando dados do Brasil
df_argentina = data[data['country'] == 'Argentina'] #Filtrando dados da Argentina

#Criando a figura:
p2 = figure(title="ANNUAL PERCENTAGE CHANGE IN WIND CONSUMPTION", 
            x_axis_label='YEAR', 
           y_axis_label='WIND ENERGY PER CAPITA',
          width=600, height=300)

#Plotando os gráficos de linha para cada país:
p2.line(df_brazil['year'], df_brazil['wind_cons_change_pct'], line_width=6, color='#D49495', legend_label='Brazil')
p2.line(df_argentina['year'], df_argentina['wind_cons_change_pct'], line_width=4, color='#8A5556', legend_label='Argentina')

#Ajustando a legenda:
p2.legend.location = "top_left"
p2.legend.title = "COUNTRIES"

p2.title.text_font = "Georgia"  #Alterando a fonte do título 
p2.title.text_font_size = "10pt"  #Alterando o tamanho da fonte do título 
p2.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
p2.title.text_align = "center"  #Alinhando o título no centro do gráfico
p2.title.text_baseline = "middle"  #Alinhando o título verticalmente ao centro


p2.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
p2.xaxis.axis_label_text_font_size = "10pt"  #Alterando o tamanho da fonte do rótulo do eixo x 
p2.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x 
p2.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

p2.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
p2.yaxis.axis_label_text_font_size = "10pt"  #Alterando o tamanho da fonte do rótulo do eixo y 
p2.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
p2.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

p2.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico


#3: BRASIL E CHINA

data = pd.read_csv("World Energy Consumption.csv") #Lendo o arquivo
df_brazil = data[data['country'] == 'Brazil'] #Filtrando dados do Brasil
df_china = data[data['country'] == 'China'] #Filtrando dados da China

#Criando a figura:
p3 = figure(title="ANNUAL PERCENTAGE CHANGE IN WIND CONSUMPTION", 
            x_axis_label='YEAR', 
           y_axis_label='WIND ENERGY PER CAPITA',
           width=600, height=300)

#Plotando os gráficos de linha para cada país:
p3.line(df_brazil['year'], df_brazil['wind_cons_change_pct'], line_width=6, color='#D49495', legend_label='Brazil')
p3.line(df_china['year'], df_china['wind_cons_change_pct'], line_width=4, color='#8A5556', legend_label='China')

#Ajustando a legenda:
p3.legend.location = "top_left"
p3.legend.title = "COUNTRIES"

p3.title.text_font = "Georgia"  #Alterando a fonte do título 
p3.title.text_font_size = "10pt"  #Alterando o tamanho da fonte do título 
p3.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
p3.title.text_align = "center"  #Alinhando o título no centro do gráfico
p3.title.text_baseline = "middle"  #Alinhando o título verticalmente ao centro


p3.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
p3.xaxis.axis_label_text_font_size = "10pt"  #Alterando o tamanho da fonte do rótulo do eixo x 
p3.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x 
p3.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

p3.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
p3.yaxis.axis_label_text_font_size = "10pt"  #Alterando o tamanho da fonte do rótulo do eixo y 
p3.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
p3.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

p3.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico

#4: Brasil e Estados Unidos 
data = pd.read_csv("World Energy Consumption.csv") #Lendo o arquivo
df_brazil = data[data['country'] == 'Brazil'] #Filtrando dados do Brasil
df_united = data[data['country'] == 'United States'] #Filtrando dados dos Estados Unidos 

#Criando a figura:
p4 = figure(title="ANNUAL PERCENTAGE CHANGE IN WIND CONSUMPTION", 
            x_axis_label='YEAR', 
           y_axis_label='WIND ENERGY PER CAPITA',
           width=600, height=300)

#Plotando os gráficos de linha para cada país:
p4.line(df_brazil['year'], df_brazil['wind_cons_change_pct'], line_width=6, color='#D49495', legend_label='Brazil')
p4.line(df_united['year'], df_united['wind_cons_change_pct'], line_width=4, color='#8A5556', legend_label='United States')

#Ajustando a legenda:
p4.legend.location = "top_left"
p4.legend.title = "COUNTRIES"

p4.title.text_font = "Georgia"  #Alterando a fonte do título 
p4.title.text_font_size = "10pt"  #Alterando o tamanho da fonte do título 
p4.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
p4.title.text_align = "center"  #Alinhando o título no centro do gráfico
p4.title.text_baseline = "middle"  #Alinhando o título verticalmente ao centro


p4.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
p4.xaxis.axis_label_text_font_size = "10pt"  #Alterando o tamanho da fonte do rótulo do eixo x 
p4.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x 
p4.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

p4.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
p4.yaxis.axis_label_text_font_size = "10pt"  #Alterando o tamanho da fonte do rótulo do eixo y 
p4.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
p4.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

p4.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico

#5: BRASIL E ALEMANHA
data = pd.read_csv("World Energy Consumption.csv") #Lendo o arquivo
df_brazil = data[data['country'] == 'Brazil'] #Filtrando dados do Brasil
df_germany = data[data['country'] == 'Germany'] #Filtrando dados da Argentina

#Criando a figura:
p5 = figure(title="ANNUAL PERCENTAGE CHANGE IN WIND CONSUMPTION", 
            x_axis_label='YEAR', 
           y_axis_label='WIND ENERGY PER CAPITA',
           width=600, height=300)

#Plotando os gráficos de linha para cada país:
p5.line(df_brazil['year'], df_brazil['wind_cons_change_pct'], line_width=6, color='#D49495', legend_label='Brazil')
p5.line(df_germany['year'], df_germany['wind_cons_change_pct'], line_width=4, color='#8A5556', legend_label='Germany')

#Ajustando a legenda:
p5.legend.location = "top_left"
p5.legend.title = "COUNTRIES"

p5.title.text_font = "Georgia"  #Alterando a fonte do título 
p5.title.text_font_size = "10pt"  #Alterando o tamanho da fonte do título 
p5.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
p5.title.text_align = "center"  #Alinhando o título no centro do gráfico
p5.title.text_baseline = "middle"  #Alinhando o título verticalmente ao centro


p5.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
p5.xaxis.axis_label_text_font_size = "10pt"  #Alterando o tamanho da fonte do rótulo do eixo x 
p5.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x 
p5.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

p5.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
p5.yaxis.axis_label_text_font_size = "10pt"  #Alterando o tamanho da fonte do rótulo do eixo y 
p5.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
p5.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

p5.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico

#6: Brasil e Reino Unido

data = pd.read_csv("World Energy Consumption.csv") #Lendo o arquivo
df_brazil = data[data['country'] == 'Brazil'] #Filtrando dados do Brasil
df_kingdom = data[data['country'] == 'United Kingdom'] #Filtrando dados do Reino Unido

#Criando a figura:
p6 = figure(title="ANNUAL PERCENTAGE CHANGE IN WIND CONSUMPTION", 
            x_axis_label='YEAR', 
           y_axis_label='WIND ENERGY PER CAPITA',
           width=600, height=300)

#Plotando os gráficos de linha para cada país:
p6.line(df_brazil['year'], df_brazil['wind_cons_change_pct'], line_width=6, color='#D49495', legend_label='Brazil')
p6.line(df_kingdom['year'], df_kingdom['wind_cons_change_pct'], line_width=4, color='#8A5556', legend_label='Reino Unido')

#Ajustando a legenda:
p6.legend.location = "top_left"
p6.legend.title = "COUNTRIES"

p6.title.text_font = "Georgia"  #Alterando a fonte do título 
p6.title.text_font_size = "10pt"  #Alterando o tamanho da fonte do título 
p6.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
p6.title.text_align = "center"  #Alinhando o título no centro do gráfico
p6.title.text_baseline = "middle"  #Alinhando o título verticalmente ao centro


p6.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
p6.xaxis.axis_label_text_font_size = "10pt"  #Alterando o tamanho da fonte do rótulo do eixo x 
p6.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x 
p6.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

p6.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
p6.yaxis.axis_label_text_font_size = "10pt"  #Alterando o tamanho da fonte do rótulo do eixo y 
p6.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
p6.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

p6.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico

#Criando um grid com os gráficos
grid = gridplot([[p1, p2, p3], [p4, p5, p6]])

#Configurando a saída para um arquivo HTML
output_file("grid.html")

#Exibindo o grid
show(grid)