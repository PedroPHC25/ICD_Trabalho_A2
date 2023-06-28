import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import Slope, ColumnDataSource
from scipy import stats
from bokeh.layouts import gridplot


#GRÁFICO DE DISPERSÃO

data = pd.read_csv("World Energy Consumption.csv") # Lendo o arquivo CSV
df_filtered_year = data[data['year'] == 2000] # Filtrando os dados do ano de 2000

# Removendo linhas com valores NaN
df_filtered_year = df_filtered_year.dropna(subset=['wind_energy_per_capita'])

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
source = ColumnDataSource(df_filtered_year)

# Criando a figura
p3 = figure(height=600, width=1200, 
            title="                       RATIO BETWEEN WIND ELECTRICITY AND WIND ENERGY (BOTH PER CAPITA)", 
                               tools = "pan, wheel_zoom, reset, hover, save",
                               tooltips = [("País", "@country")])

# Plotando o gráfico de dispersão
p3.scatter(x='wind_elec_per_capita', y='wind_energy_per_capita', source=source,
           fill_color="#D49495", size=10)

# Ajustando rótulos e títulos dos eixos
p3.xaxis.axis_label = "WIND ELECTRICITY PER CAPITA"
p3.yaxis.axis_label = "WIND ENERGY PER CAPITA"

# Aplicando regressão linear usando scipy
slope, intercept, r_value, p_value, std_err = stats.linregress(df_filtered_year['wind_elec_per_capita'], df_filtered_year['wind_energy_per_capita'])

# Criando a reta de regressão
x_line = np.array([df_filtered_year['wind_elec_per_capita'].min(), df_filtered_year['wind_elec_per_capita'].max()])
y_line = slope * x_line + intercept
regression_line = Slope(gradient=slope, y_intercept=intercept, line_color='#8A5556', line_width=2)

# Adicionando a reta de regressão ao gráfico
p3.add_layout(regression_line)

# Configurando as propriedades visuais
p3.title.text_font = "Georgia"
p3.title.text_font_size = "14pt"
p3.title.text_color = "#8A5556"
p3.title.text_align = "center"
p3.title.text_baseline = "middle"

p3.xaxis.axis_label_text_font = "Georgia"
p3.xaxis.axis_label_text_font_size = "16pt"
p3.xaxis.axis_label_text_color = "#8A5556"
p3.xaxis.major_label_text_font_style = "bold"

p3.yaxis.axis_label_text_font = "Georgia"
p3.yaxis.axis_label_text_font_size = "16pt"
p3.yaxis.axis_label_text_color = "#8A5556"
p3.yaxis.major_label_text_font_style = "bold"

p3.background_fill_color = "#D4D3A9"


#MESMO GRÁFICO, OUTRA ESCALA

data = pd.read_csv("World Energy Consumption.csv") # Lendo o arquivo CSV
df_filtered_year = data[data['year'] == 2000] # Filtrando os dados do ano de 2000

# Removendo linhas com valores NaN
df_filtered_year = df_filtered_year.dropna(subset=['wind_energy_per_capita'])

# Verificando se há linhas restantes após a remoção de NaN
if df_filtered_year.empty:
    raise ValueError("Não há dados válidos para a regressão.")

# Criando o ColumnDataSource
source2 = ColumnDataSource(df_filtered_year)

# Criando a figura
p4 = figure(height=600, width=1200, 
            title="            RATIO BETWEEN WIND ELECTRICITY AND WIND ENERGY (BOTH PER CAPITA)", 
                               tools = "pan, wheel_zoom, reset, hover, save",
                               tooltips = [("País", "@country")])

# Plotando o gráfico de dispersão
p4.scatter(x='wind_elec_per_capita', y='wind_energy_per_capita', source=source2,
           fill_color="#D49495", size=10)

# Ajustando rótulos e títulos dos eixos
p4.xaxis.axis_label = "WIND ELECTRICITY PER CAPITA"
p4.yaxis.axis_label = "WIND ENERGY PER CAPITA"

# Aplicando regressão linear usando scipy
slope, intercept, r_value, p_value, std_err = stats.linregress(df_filtered_year['wind_elec_per_capita'], df_filtered_year['wind_energy_per_capita'])

# Criando a reta de regressão
x_line = np.array([df_filtered_year['wind_elec_per_capita'].min(), df_filtered_year['wind_elec_per_capita'].max()])
y_line = slope * x_line + intercept
regression_line = Slope(gradient=slope, y_intercept=intercept, line_color='#8A5556', line_width=2)

# Adicionando a reta de regressão ao gráfico
p4.add_layout(regression_line)

# Configurando as propriedades visuais
p4.title.text_font = "Georgia"
p4.title.text_font_size = "14pt"
p4.title.text_color = "#8A5556"
p4.title.text_align = "center"
p4.title.text_baseline = "middle"

p4.xaxis.axis_label_text_font = "Georgia"
p4.xaxis.axis_label_text_font_size = "16pt"
p4.xaxis.axis_label_text_color = "#8A5556"
p4.xaxis.major_label_text_font_style = "bold"

p4.yaxis.axis_label_text_font = "Georgia"
p4.yaxis.axis_label_text_font_size = "16pt"
p4.yaxis.axis_label_text_color = "#8A5556"
p4.yaxis.major_label_text_font_style = "bold"

p4.background_fill_color = "#D4D3A9"

#Criando um grid com os gráficos
grid2 = gridplot([[p4], [p3]])

#Configurando a saída para um arquivo HTML
output_file("grid2.html")

#Exibindo o grid
show(grid2)