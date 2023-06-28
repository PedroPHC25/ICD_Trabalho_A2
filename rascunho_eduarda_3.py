# GRÁFICO DE DISPERSÃO 

import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import Slope
from sklearn.linear_model import RANSACRegressor

data = pd.read_csv("World Energy Consumption.csv") #Lendo o arquivo CSV
df_filtered_year = data[data['year'] == 2000] #Filtrando os dados do ano de 2000

#Removendo linhas com valores NaN
df_filtered_year = df_filtered_year.dropna(subset=['wind_energy_per_capita'])

#Verificando se há linhas restantes após a remoção de NaN
if df_filtered_year.empty:
    raise ValueError("Não há dados válidos para a regressão.")

#Criando a figura:
p3 = figure(height=600, width=1200, title="            RATIO BETWEEN WIND ELECTRICITY AND WIND ENERGY (BOTH PER CAPITA)")

#Plotando o gráfico de dispersão
p3.scatter(x='wind_elec_per_capita', y='wind_energy_per_capita', source=df_filtered_year,
           fill_color="#D49495", size=10)

#Ajustando rótulos e títulos dos eixos
p3.xaxis.axis_label = "WIND ELECTRICITY PER CAPITA"
p3.yaxis.axis_label = "WIND ENERGY PER CAPITA"

#Aplicando regressão RANSAC
ransac = RANSACRegressor()
x = df_filtered_year['wind_elec_per_capita'].values.reshape(-1, 1)
y = df_filtered_year['wind_energy_per_capita'].values.reshape(-1, 1)
ransac.fit(x, y)

#Calculando a reta de regressão
slope = ransac.estimator_.coef_[0][0]
intercept = ransac.estimator_.intercept_[0]

#Criandoa reta de regressão
x_line = np.array([df_filtered_year['wind_elec_per_capita'].min(), df_filtered_year['wind_elec_per_capita'].max()])
y_line = slope * x_line + intercept
regression_line = Slope(gradient=slope, y_intercept=intercept, line_color='#8A5556', line_width=2)

#Adicionando a reta de regressão ao gráfico
p3.add_layout(regression_line)

p3.title.text_font = "Georgia"  #Alterando a fonte do título 
p3.title.text_font_size = "14pt"  #Alterando o tamanho da fonte do título 
p3.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
p3.title.text_align = "center"  #Alinhando o título no centro do gráfico
p3.title.text_baseline = "middle"  #Alinhando o título verticalmente ao centro

p3.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
p3.xaxis.axis_label_text_font_size = "16pt"  #Alterando tamanho da fonte do rótulo do eixo x 
p3.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x 
p3.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

p3.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
p3.yaxis.axis_label_text_font_size = "16pt"  #Alterando o tamanho da fonte do rótulo do eixo y 
p3.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
p3.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

p3.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico