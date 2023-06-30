from bokeh.plotting import figure
from cds_generator import wind_scatter_sem_outlier, wind_scatter_com_outlier, regression_line, regression_line_new_scale

from bokeh.plotting import figure, show, output_file, save
from bokeh.layouts import gridplot

#GRÁFICO DE DISPERSÃO

# Criando a figura
wind_ratio_figure = figure(height=600, width=1200,
            title="                       RATIO BETWEEN WIND ELECTRICITY AND WIND ENERGY (BOTH PER CAPITA)",
                               tools = "pan, wheel_zoom, reset, hover, save",
                               tooltips = [("País", "@country")])


# Plotando o gráfico de dispersão
wind_ratio_figure.scatter(x='wind_elec_per_capita', y='wind_energy_per_capita', source=wind_scatter_sem_outlier,
           fill_color="#D49495", size=10)


# Ajustando rótulos e títulos dos eixos
wind_ratio_figure.xaxis.axis_label = "WIND ELECTRICITY PER CAPITA"
wind_ratio_figure.yaxis.axis_label = "WIND ENERGY PER CAPITA"


# Adicionando a reta de regressão ao gráfico
wind_ratio_figure.add_layout(regression_line)


# Configurando as propriedades visuais
wind_ratio_figure.title.text_font = "Georgia"
wind_ratio_figure.title.text_font_size = "14pt"
wind_ratio_figure.title.text_color = "#8A5556"
wind_ratio_figure.title.align = "center"
wind_ratio_figure.title.text_baseline = "middle"

wind_ratio_figure.xaxis.axis_label_text_font = "Georgia"
wind_ratio_figure.xaxis.axis_label_text_font_size = "16pt"
wind_ratio_figure.xaxis.axis_label_text_color = "#8A5556"
wind_ratio_figure.xaxis.major_label_text_font_style = "bold"

wind_ratio_figure.yaxis.axis_label_text_font = "Georgia"
wind_ratio_figure.yaxis.axis_label_text_font_size = "16pt"
wind_ratio_figure.yaxis.axis_label_text_color = "#8A5556"
wind_ratio_figure.yaxis.major_label_text_font_style = "bold"

wind_ratio_figure.background_fill_color = "#D4D3A9"


#MESMO GRÁFICO, OUTRA ESCALA

# Criando a figura
wind_ratio_figure_new_scale = figure(height=600, width=1200,
            title="            RATIO BETWEEN WIND ELECTRICITY AND WIND ENERGY (BOTH PER CAPITA)",
                               tools = "pan, wheel_zoom, reset, hover, save",
                               tooltips = [("País", "@country")])


# Plotando o gráfico de dispersão
wind_ratio_figure_new_scale.scatter(x='wind_elec_per_capita', y='wind_energy_per_capita', source=wind_scatter_com_outlier,
           fill_color="#D49495", size=10)


# Ajustando rótulos e títulos dos eixos
wind_ratio_figure_new_scale.xaxis.axis_label = "WIND ELECTRICITY PER CAPITA"
wind_ratio_figure_new_scale.yaxis.axis_label = "WIND ENERGY PER CAPITA"


# Adicionando a reta de regressão ao gráfico
wind_ratio_figure_new_scale.add_layout(regression_line_new_scale)


# Configurando as propriedades visuais
wind_ratio_figure_new_scale.title.text_font = "Georgia"
wind_ratio_figure_new_scale.title.text_font_size = "14pt"
wind_ratio_figure_new_scale.title.text_color = "#8A5556"
wind_ratio_figure_new_scale.title.align = "center"
wind_ratio_figure_new_scale.title.text_baseline = "middle"


wind_ratio_figure_new_scale.xaxis.axis_label_text_font = "Georgia"
wind_ratio_figure_new_scale.xaxis.axis_label_text_font_size = "16pt"
wind_ratio_figure_new_scale.xaxis.axis_label_text_color = "#8A5556"
wind_ratio_figure_new_scale.xaxis.major_label_text_font_style = "bold"


wind_ratio_figure_new_scale.yaxis.axis_label_text_font = "Georgia"
wind_ratio_figure_new_scale.yaxis.axis_label_text_font_size = "16pt"
wind_ratio_figure_new_scale.yaxis.axis_label_text_color = "#8A5556"
wind_ratio_figure_new_scale.yaxis.major_label_text_font_style = "bold"


wind_ratio_figure_new_scale.background_fill_color = "#D4D3A9"


#Criando um grid com os gráficos
wind_grid_scatter_plot = gridplot([[wind_ratio_figure_new_scale], 
                                   [wind_ratio_figure]])


#Configurando a saída para um arquivo HTML
output_file("wind_grid_scatter_plot.html")


#Exibindo o grid
show(wind_grid_scatter_plot)
save(wind_grid_scatter_plot)
