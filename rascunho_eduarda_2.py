import pandas as pd
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.models import Legend, LegendItem

# Lendo o arquivo
data = pd.read_csv("World Energy Consumption.csv")

# Filtrando dados do ano de 2020
df_filtered = data[data['year'] == 2020]

# Ordenando os valores de 'wind_electricity' em ordem decrescente
df_sorted = df_filtered.sort_values('wind_electricity', ascending=False)

# Selecionando os 10 maiores valores da coluna 'wind_electricity'
df_top_10 = df_sorted.head(10)

# Selecionando apenas as colunas desejadas ('country' e 'wind_electricity')
df_top_10_filtered = df_top_10[['country', 'wind_electricity']]

#Identificando o país com o maior valor de wind_electricity
pais_maior_geracao = df_top_10_filtered[df_top_10_filtered['wind_electricity'] == df_top_10_filtered['wind_electricity'].max()]['country'].iloc[0]

#Excluindo o país com o maior valor de wind_electricity
df_top_10_filtered = df_top_10_filtered[df_top_10_filtered['country'] != pais_maior_geracao]

# Adicionando cada cor a um continente
df_top_10_filtered["continent"] = ["Asia", "America", "Europe", "Europe", "Asia", "America", "Europe", "Europe", "America"]
color_dict = {"America": "#87864D", "Europe": "#D49495", "Asia": "#8A5556"}

colors = [color_dict[continent] for continent in df_top_10_filtered["continent"]]

df_top_10_filtered["color"] = colors

# Criando ColumnDataSource
data_organized = ColumnDataSource(df_top_10_filtered)

# Criando a figura e plotando as barras
p = figure(x_range=df_top_10_filtered['country'], height=600, width=1200,
           title="ELECTRICITY GENERATION FROM WIND BY COUNTRY IN 2020")
p.vbar(x='country', top='wind_electricity', width=0.9, fill_color='color', line_color='none', source=data_organized)

from bokeh.models import Rect

legend_items = []
for continent, color in color_dict.items():
    glyph = Rect(x='x', y='y', width=0, height=0, fill_color=color)
    legend_item = LegendItem(label=continent, index=0, renderers=[glyph], label_text_color=color)
    legend_items.append(legend_item)

legend = Legend(items=legend_items, label_standoff=5, click_policy="hide")
p.add_layout(legend, 'right')

legend.spacing = 5
legend.margin = 5
legend.padding = 5
legend.label_text_font_size = '10pt'


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

#Configurando a saída para um arquivo HTML
output_file("barras_eduarda.html")
show(p)


