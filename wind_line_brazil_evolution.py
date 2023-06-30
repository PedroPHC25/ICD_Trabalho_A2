from bokeh.models import Label, BoxAnnotation
from bokeh.plotting import figure
from cds_generator import df_wind_graph_line

#GRÁFICO DE LINHA CONSUMO PER CAPITA DE ELETRICIDADE DO VENTO PARA O BRASIL NOS ÚLTIMOS 50 ANOS

#Criando uma figura:
wind_line_brazil_evolution_graph = figure(title="      PER CAPITA CONSUMPTION OF ELECTRICITY GENERATED BY WIND IN BRAZIL IN THE LAST 50 YEARS",
           x_axis_label='YEAR', y_axis_label='WIND ENERGY CONSUMPTION (kWh)', width=1200, height=600)

# Plotando o gráfico de linha:
wind_line_brazil_evolution_graph.line('year', 'wind_energy_per_capita', line_width=6, line_color="#8A5556", source=df_wind_graph_line)

wind_line_brazil_evolution_graph.title.text_font = "Georgia"  #Alterando a fonte do título 
wind_line_brazil_evolution_graph.title.text_font_size = "14pt"  #Alterando o tamanho da fonte do título 
wind_line_brazil_evolution_graph.title.text_color = "#8A5556"  #Alterando a cor do texto do título 
wind_line_brazil_evolution_graph.title.text_align = "center"  #Alinhando o título no centro do gráfico

wind_line_brazil_evolution_graph.xaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo x 
wind_line_brazil_evolution_graph.xaxis.axis_label_text_font_size = "16pt"  #Alterando o tamanho da fonte do rótulo do eixo x 
wind_line_brazil_evolution_graph.xaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo x
wind_line_brazil_evolution_graph.xaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo x

wind_line_brazil_evolution_graph.yaxis.axis_label_text_font = "Georgia"  #Alterando a fonte do rótulo do eixo y 
wind_line_brazil_evolution_graph.yaxis.axis_label_text_font_size = "16pt"  #Alterando o tamanho da fonte do rótulo do eixo y
wind_line_brazil_evolution_graph.yaxis.axis_label_text_color = "#8A5556"  #Alterando a cor do texto do rótulo do eixo y 
wind_line_brazil_evolution_graph.yaxis.major_label_text_font_style = "bold"  #Colocando em negrito os rótulos das escalas do eixo y

wind_line_brazil_evolution_graph.background_fill_color = "#D4D3A9"  #Alterando a cor de fundo do gráfico 

text_lines = [
    "In 2009, 10 projects were under construction, with a capacity of 256 MW,",
    "and in 2010, 45 started their construction to generate 2,139 MW,",
    "in several states. There is a public-private partnership."
]
text = '\n'.join(text_lines)

wind_line_brazil_evolution_graph.add_layout(Label(x=2016, y=500,
                    text=text,
                    text_align="right",
                    text_font_size="12px",
                    text_color="#8A5556",
                    text_alpha=1))

annotation = BoxAnnotation(left=2010, right=2020, fill_color='#D49495', fill_alpha=0.3)
wind_line_brazil_evolution_graph.add_layout(annotation)

 