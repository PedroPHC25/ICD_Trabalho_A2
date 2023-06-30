from bokeh.plotting import figure
from cds_generator import df_top_10_filtered, create_column_data_source_top_10_filtered

# Criando a figura, plotando as barras e criando legendas
wind_bar_top_countries_graph = figure(x_range=df_top_10_filtered['country'], 
                                      height=600, 
                                      width=1200,
                                      title="ELECTRICITY GENERATION FROM WIND BY COUNTRY IN 2020")

#Criando a legenda 
wind_bar_top_countries_graph.vbar(x="country", 
                                  top='wind_electricity', 
                                  legend_label = "Europe", 
                                  fill_alpha = 1, 
                                  line_color='none',
                                  color = "#D49495", 
                                  width=0.01, 
                                  source = create_column_data_source_top_10_filtered)
wind_bar_top_countries_graph.vbar(x="country", 
                                  top='wind_electricity', 
                                  legend_label = "Asia", 
                                  fill_alpha = 1, 
                                  line_color='none',
                                  color = "#8A5556", 
                                  width=0.01, 
                                  source = create_column_data_source_top_10_filtered)
wind_bar_top_countries_graph.vbar(x="country", 
                                  top='wind_electricity', 
                                  legend_label = "America", 
                                  fill_alpha = 1, 
                                  line_color='none', 
                                  color = "#87864D", 
                                  width=0.01, 
                                  source = create_column_data_source_top_10_filtered)
wind_bar_top_countries_graph.vbar(x='country', 
                                  top='wind_electricity', 
                                  width=0.9, 
                                  fill_color='color', 
                                  line_color='none', 
                                  source=create_column_data_source_top_10_filtered)

#Ajustando os títulos dos eixos
wind_bar_top_countries_graph.xaxis.axis_label = "COUNTRY"
wind_bar_top_countries_graph.yaxis.axis_label = "ELECTRICITY GENERATION FROM WIND (TWh)"

wind_bar_top_countries_graph.title.text_font = "Georgia"  #Alterando a fonte do título 
wind_bar_top_countries_graph.title.text_font_size = "16pt"  #Alterando o tamanho da fonte do título 
wind_bar_top_countries_graph.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
wind_bar_top_countries_graph.title.align = "center"  #Alinhando o título no centro do gráfico

wind_bar_top_countries_graph.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
wind_bar_top_countries_graph.xaxis.axis_label_text_font_size = "16pt"  #Alterando o tamanho da fonte do rótulo do eixo x 
wind_bar_top_countries_graph.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x 
wind_bar_top_countries_graph.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

wind_bar_top_countries_graph.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
wind_bar_top_countries_graph.yaxis.axis_label_text_font_size = "16pt"  #Alterando o tamanho da fonte do rótulo do eixo y 
wind_bar_top_countries_graph.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
wind_bar_top_countries_graph.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

wind_bar_top_countries_graph.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico

