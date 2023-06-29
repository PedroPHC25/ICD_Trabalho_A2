import pandas as pd
from bokeh.io import output_file, show, save 
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

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

# Criando a figura, plotando as barras e criando legendas
wind_bar_top_countries_graph = figure(x_range=df_top_10_filtered['country'], height=600, width=1200,
           title="                               ELECTRICITY GENERATION FROM WIND BY COUNTRY IN 2020")

#Criando a legenda 
wind_bar_top_countries_graph.vbar(x="country", top='wind_electricity', legend_label = "Europe", fill_alpha = 1, line_color='none',color = "#D49495", width=0.01, source = data_organized)
wind_bar_top_countries_graph.vbar(x="country", top='wind_electricity', legend_label = "Asia", fill_alpha = 1, line_color='none',color = "#8A5556", width=0.01, source = data_organized)
wind_bar_top_countries_graph.vbar(x="country", top='wind_electricity', legend_label = "America", fill_alpha = 1, line_color='none', color = "#87864D", width=0.01, source = data_organized)

wind_bar_top_countries_graph.vbar(x='country', top='wind_electricity', width=0.9, fill_color='color', line_color='none', source=data_organized)

#Ajustando os títulos dos eixos
wind_bar_top_countries_graph.xaxis.axis_label = "COUNTRY"
wind_bar_top_countries_graph.yaxis.axis_label = "ELECTRICITY GENERATION FROM WIND (TWh)"

wind_bar_top_countries_graph.title.text_font = "Georgia"  #Alterando a fonte do título 
wind_bar_top_countries_graph.title.text_font_size = "16pt"  #Alterando o tamanho da fonte do título 
wind_bar_top_countries_graph.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
wind_bar_top_countries_graph.title.text_align = "center"  #Alinhando o título no centro do gráfico

wind_bar_top_countries_graph.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
wind_bar_top_countries_graph.xaxis.axis_label_text_font_size = "16pt"  #Alterando o tamanho da fonte do rótulo do eixo x 
wind_bar_top_countries_graph.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x 
wind_bar_top_countries_graph.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

wind_bar_top_countries_graph.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
wind_bar_top_countries_graph.yaxis.axis_label_text_font_size = "16pt"  #Alterando o tamanho da fonte do rótulo do eixo y 
wind_bar_top_countries_graph.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
wind_bar_top_countries_graph.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

wind_bar_top_countries_graph.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico

#Configurando a saída para um arquivo HTML
save(wind_bar_top_countries_graph)
output_file("wind_bar_top_countries_graph.html")
show(wind_bar_top_countries_graph)
