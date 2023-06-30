from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.layouts import gridplot
from cds_generator import df_brazil, df_argentina, df_china, df_germany, df_kingdom, df_india, df_united

#GRÁFICOS DE LINHA  VARIAÇÃO PERCENTUAL ANUAL NO CONSUMO DE VENTO

#1: BRASIL E INDIA 

#Criando a figura:
grid_brazil_india = figure(title="ANNUAL PERCENTAGE CHANGE IN WIND CONSUMPTION", 
                           x_axis_label='YEAR', 
                           y_axis_label='WIND ENERGY PER CAPITA',
                           width=450, 
                           height=300)

# Criando a origem de dados para os dados do Brasil
source_brazil = ColumnDataSource(df_brazil)

# Criando a origem de dados para os dados da Índia
source_india = ColumnDataSource(df_india)

# Plotando os gráficos de linha para cada país, usando as origens de dados
grid_brazil_india.line('year', 
                       'wind_cons_change_pct', 
                       line_width=6, 
                       color='#D49495', 
                       legend_label='Brazil', 
                       source=source_brazil)
grid_brazil_india.line('year', 
                       'wind_cons_change_pct', 
                       line_width=4, 
                       color='#8A5556', 
                       legend_label='India', 
                       source=source_india)

#Ajustando a legenda:
grid_brazil_india.legend.location = "top_right"
grid_brazil_india.legend.title = "COUNTRIES"

grid_brazil_india.title.text_font = "Georgia"  #Alterando a fonte do título 
grid_brazil_india.title.text_font_size = "8pt"  #Alterando o tamanho da fonte do título 
grid_brazil_india.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
grid_brazil_india.title.text_align = "center"  #Alinhando o título no centro do gráfico
grid_brazil_india.title.text_baseline = "middle"  #Alinhando o título verticalmente ao centro

grid_brazil_india.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
grid_brazil_india.xaxis.axis_label_text_font_size = "8pt"  #Alterando o tamanho da fonte do rótulo do eixo x 
grid_brazil_india.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x 
grid_brazil_india.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

grid_brazil_india.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
grid_brazil_india.yaxis.axis_label_text_font_size = "8pt"  #Alterando o tamanho da fonte do rótulo do eixo y 
grid_brazil_india.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
grid_brazil_india.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

grid_brazil_india.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico


#2: BRASIL E ARGENTINA

#Criando a figura:
grid_brazil_argentina = figure(title="ANNUAL PERCENTAGE CHANGE IN WIND CONSUMPTION", 
                               x_axis_label='YEAR', 
                               y_axis_label='WIND ENERGY PER CAPITA',
                               width=450, 
                               height=300)

# Criando a origem de dados para os dados do Brasil
source_brazil = ColumnDataSource(df_brazil)

# Criando a origem de dados para os dados da Argentina
source_argentina = ColumnDataSource(df_argentina)

# Plotando os gráficos de linha para cada país, usando as origens de dados
grid_brazil_argentina.line('year', 
                           'wind_cons_change_pct', 
                           line_width=6, 
                           color='#D49495', 
                           legend_label='Brazil', 
                           source=source_brazil)
grid_brazil_argentina.line('year', 
                           'wind_cons_change_pct', 
                           line_width=4, 
                           color='#8A5556', 
                           legend_label='Argentina', 
                           source=source_argentina)

#Ajustando a legenda:
grid_brazil_argentina.legend.location = "top_right"
grid_brazil_argentina.legend.title = "COUNTRIES"

grid_brazil_argentina.title.text_font = "Georgia"  #Alterando a fonte do título 
grid_brazil_argentina.title.text_font_size = "8pt"  #Alterando o tamanho da fonte do título 
grid_brazil_argentina.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
grid_brazil_argentina.title.text_align = "center"  #Alinhando o título no centro do gráfico
grid_brazil_argentina.title.text_baseline = "middle"  #Alinhando o título verticalmente ao centro


grid_brazil_argentina.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
grid_brazil_argentina.xaxis.axis_label_text_font_size = "8pt"  #Alterando o tamanho da fonte do rótulo do eixo x 
grid_brazil_argentina.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x 
grid_brazil_argentina.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

grid_brazil_argentina.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
grid_brazil_argentina.yaxis.axis_label_text_font_size = "8pt"  #Alterando o tamanho da fonte do rótulo do eixo y 
grid_brazil_argentina.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
grid_brazil_argentina.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

grid_brazil_argentina.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico


#3: BRASIL E CHINA

#Criando a figura:
grid_brazil_china = figure(title="ANNUAL PERCENTAGE CHANGE IN WIND CONSUMPTION", 
                           x_axis_label='YEAR', 
                           y_axis_label='WIND ENERGY PER CAPITA',
                           width=450, 
                           height=300)

# Criando a origem de dados para os dados do Brasil
source_brazil = ColumnDataSource(df_brazil)

# Criando a origem de dados para os dados da China
source_china = ColumnDataSource(df_china)

# Plotando os gráficos de linha para cada país, usando as origens de dados
grid_brazil_china.line('year', 
                       'wind_cons_change_pct', 
                       line_width=6, 
                       color='#D49495', 
                       legend_label='Brazil', 
                       source=source_brazil)
grid_brazil_china.line('year', 
                       'wind_cons_change_pct', 
                       line_width=4, 
                       color='#8A5556', 
                       legend_label='China', 
                       source=source_china)

#Ajustando a legenda:
grid_brazil_china.legend.location = "top_right"
grid_brazil_china.legend.title = "COUNTRIES"

grid_brazil_china.title.text_font = "Georgia"  #Alterando a fonte do título 
grid_brazil_china.title.text_font_size = "8pt"  #Alterando o tamanho da fonte do título 
grid_brazil_china.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
grid_brazil_china.title.text_align = "center"  #Alinhando o título no centro do gráfico
grid_brazil_china.title.text_baseline = "middle"  #Alinhando o título verticalmente ao centro

grid_brazil_china.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
grid_brazil_china.xaxis.axis_label_text_font_size = "8pt"  #Alterando o tamanho da fonte do rótulo do eixo x 
grid_brazil_china.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x 
grid_brazil_china.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

grid_brazil_china.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
grid_brazil_china.yaxis.axis_label_text_font_size = "8pt"  #Alterando o tamanho da fonte do rótulo do eixo y 
grid_brazil_china.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
grid_brazil_china.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

grid_brazil_china.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico

#4: Brasil e Estados Unidos 

#Criando a figura:
grid_brazil_united_states = figure(title="ANNUAL PERCENTAGE CHANGE IN WIND CONSUMPTION", 
                                   x_axis_label='YEAR', 
                                   y_axis_label='WIND ENERGY PER CAPITA',
                                   width=450, 
                                   height=300)

# Criando a origem de dados para os dados do Brasil
source_brazil = ColumnDataSource(df_brazil)

# Criando a origem de dados para os dados dos Estados Unidos
source_united = ColumnDataSource(df_united)

# Plotando os gráficos de linha para cada país, usando as origens de dados
grid_brazil_united_states.line('year', 
                               'wind_cons_change_pct', 
                               line_width=6, 
                               color='#D49495', 
                               legend_label='Brazil', 
                               source=source_brazil)
grid_brazil_united_states.line('year', 
                               'wind_cons_change_pct', 
                               line_width=4, 
                               color='#8A5556', 
                               legend_label='United States', 
                               source=source_united)

# Configurando a escala do eixo y
grid_brazil_united_states.y_range.start = 0
grid_brazil_united_states.y_range.end = 3500

#Ajustando a legenda:
grid_brazil_united_states.legend.location = "top_right"
grid_brazil_united_states.legend.title = "COUNTRIES"

grid_brazil_united_states.title.text_font = "Georgia"  #Alterando a fonte do título 
grid_brazil_united_states.title.text_font_size = "8pt"  #Alterando o tamanho da fonte do título 
grid_brazil_united_states.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
grid_brazil_united_states.title.text_align = "center"  #Alinhando o título no centro do gráfico
grid_brazil_united_states.title.text_baseline = "middle"  #Alinhando o título verticalmente ao centro

grid_brazil_united_states.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
grid_brazil_united_states.xaxis.axis_label_text_font_size = "8pt"  #Alterando o tamanho da fonte do rótulo do eixo x 
grid_brazil_united_states.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x 
grid_brazil_united_states.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

grid_brazil_united_states.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
grid_brazil_united_states.yaxis.axis_label_text_font_size = "8pt"  #Alterando o tamanho da fonte do rótulo do eixo y 
grid_brazil_united_states.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
grid_brazil_united_states.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

grid_brazil_united_states.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico

#5: BRASIL E ALEMANHA

#Criando a figura:
grid_brazil_germany = figure(title="ANNUAL PERCENTAGE CHANGE IN WIND CONSUMPTION", 
                             x_axis_label='YEAR', 
                             y_axis_label='WIND ENERGY PER CAPITA',
                             width=450, 
                             height=300)

# Criando a origem de dados para os dados do Brasil
source_brazil = ColumnDataSource(df_brazil)

# Criando a origem de dados para os dados da Alemanha
source_germany = ColumnDataSource(df_germany)

# Plotando os gráficos de linha para cada país, usando as origens de dados
grid_brazil_germany.line('year', 
                         'wind_cons_change_pct', 
                         line_width=6, 
                         color='#D49495', 
                         legend_label='Brazil', 
                         source=source_brazil)
grid_brazil_germany.line('year', 
                         'wind_cons_change_pct', 
                         line_width=4, 
                         color='#8A5556', 
                         legend_label='Germany', 
                         source=source_germany)

#Ajustando a legenda:
grid_brazil_germany.legend.location = "top_right"
grid_brazil_germany.legend.title = "COUNTRIES"

grid_brazil_germany.title.text_font = "Georgia"  #Alterando a fonte do título 
grid_brazil_germany.title.text_font_size = "8pt"  #Alterando o tamanho da fonte do título 
grid_brazil_germany.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
grid_brazil_germany.title.text_align = "center"  #Alinhando o título no centro do gráfico
grid_brazil_germany.title.text_baseline = "middle"  #Alinhando o título verticalmente ao centro


grid_brazil_germany.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
grid_brazil_germany.xaxis.axis_label_text_font_size = "8pt"  #Alterando o tamanho da fonte do rótulo do eixo x 
grid_brazil_germany.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x 
grid_brazil_germany.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

grid_brazil_germany.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
grid_brazil_germany.yaxis.axis_label_text_font_size = "8pt"  #Alterando o tamanho da fonte do rótulo do eixo y 
grid_brazil_germany.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
grid_brazil_germany.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

grid_brazil_germany.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico

#6: Brasil e Reino Unido


#Criando a figura:
grid_brazil_united_kingdom = figure(title="ANNUAL PERCENTAGE CHANGE IN WIND CONSUMPTION", 
                                    x_axis_label='YEAR', 
                                    y_axis_label='WIND ENERGY PER CAPITA',
                                    width=450, 
                                    height=300)

# Criando a origem de dados para os dados do Brasil
source_brazil = ColumnDataSource(df_brazil)

# Criando a origem de dados para os dados do Reino Unido
source_kingdom = ColumnDataSource(df_kingdom)

# Plotando os gráficos de linha para cada país, usando as origens de dados
grid_brazil_united_kingdom.line('year', 
                                'wind_cons_change_pct', 
                                line_width=6, 
                                color='#D49495', 
                                legend_label='Brazil', 
                                source=source_brazil)
grid_brazil_united_kingdom.line('year', 
                                'wind_cons_change_pct', 
                                line_width=4, 
                                color='#8A5556', 
                                legend_label='Reino Unido', 
                                source=source_kingdom)

#Ajustando a legenda:
grid_brazil_united_kingdom.legend.location = "top_right"
grid_brazil_united_kingdom.legend.title = "COUNTRIES"

grid_brazil_united_kingdom.title.text_font = "Georgia"  #Alterando a fonte do título 
grid_brazil_united_kingdom.title.text_font_size = "8pt"  #Alterando o tamanho da fonte do título 
grid_brazil_united_kingdom.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
grid_brazil_united_kingdom.title.text_align = "center"  #Alinhando o título no centro do gráfico
grid_brazil_united_kingdom.title.text_baseline = "middle"  #Alinhando o título verticalmente ao centro

grid_brazil_united_kingdom.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
grid_brazil_united_kingdom.xaxis.axis_label_text_font_size = "8pt"  #Alterando o tamanho da fonte do rótulo do eixo x 
grid_brazil_united_kingdom.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x 
grid_brazil_united_kingdom.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

grid_brazil_united_kingdom.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
grid_brazil_united_kingdom.yaxis.axis_label_text_font_size = "8pt"  #Alterando o tamanho da fonte do rótulo do eixo y 
grid_brazil_united_kingdom.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
grid_brazil_united_kingdom.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

grid_brazil_united_kingdom.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico

#Criando um grid com os gráficos
wind_grid_comparison_graph = gridplot([[grid_brazil_india, grid_brazil_argentina, grid_brazil_china], 
                                       [grid_brazil_united_states, grid_brazil_germany, grid_brazil_united_kingdom]])
