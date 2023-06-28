# Importando as funções e métodos necessários
from bokeh.plotting import figure
from bokeh.models import Label, PrintfTickFormatter

# Pegando os dados do arquivo gerador de CDS
from cds_generator import cds_oil_2019_high_consumption, cds_oil_2019_low_consumption

# Esta visualização será um gráfico de dispersão mostrando a relação entre a população de cada país e o consumo de petróleo

# Criando o objeto figura com os eixos em escala logarítmica e com as ferramentas adequadas
graph_pop_consumption = figure(x_axis_type = "log", 
                               y_axis_type = "log", 
                               tools = "pan, wheel_zoom, reset, hover, save",
                               tooltips = [("País", "@country")])

# Gerando o gráfico de dispersão com os dados dos CDSs, agrupando os dados por cor (verde são os países com consumo abaixo da média mundial e vermelho são os com consumo acima)
graph_pop_consumption.circle(x = "population", 
                             y = "oil_consumption", 
                             source = cds_oil_2019_high_consumption, 
                             fill_color = "red",
                             line_color = "red",
                             size = 5,  
                             legend_label = "Acima da média mundial")
graph_pop_consumption.circle(x = "population", 
                             y = "oil_consumption", 
                             source = cds_oil_2019_low_consumption, 
                             fill_color = "lime",
                             line_color = "lime",
                             size = 5, 
                             legend_label = "Abaixo da média mundial")

# Excluindo os ticks secundários
graph_pop_consumption.xaxis.minor_tick_line_color = None
graph_pop_consumption.yaxis.minor_tick_line_color = None

# Ajustando os rótulos dos eixos
graph_pop_consumption.xaxis[0].formatter = PrintfTickFormatter(format="%5f")
graph_pop_consumption.yaxis[0].formatter = PrintfTickFormatter(format="%5f")
graph_pop_consumption.xaxis.major_label_overrides = {1000000: '1 milhão', 
                                                     10000000: '10 milhões', 
                                                     100000000: '100 milhões', 
                                                     1000000000: "1 bilhão"}

# Inserindo e customizando o título
graph_pop_consumption.title.text = "Consumo de petróleo x População em 2019"
graph_pop_consumption.title.text_font = "arial"
graph_pop_consumption.title.text_font_size = "15px"
graph_pop_consumption.title.align = "center"

# Adicionando os títulos dos eixos
graph_pop_consumption.xaxis.axis_label = "População"
graph_pop_consumption.yaxis.axis_label = "Consumo (em terawatts-hora)"
graph_pop_consumption.axis.axis_label_text_font_style = "normal"
graph_pop_consumption.xaxis.axis_label_text_font = "arial"
graph_pop_consumption.yaxis.axis_label_text_font = "arial"

# Gerando a legenda
graph_pop_consumption.legend.location = "top_left"

# Ajustando o grid
graph_pop_consumption.xgrid.grid_line_alpha = 0.4
graph_pop_consumption.ygrid.grid_line_alpha = 0.4

# Ajustando a barra de ferramentas
graph_pop_consumption.toolbar.autohide = True
graph_pop_consumption.toolbar.logo = None

# Adicionando uma anotação
graph_pop_consumption.add_layout(Label(x = 100000000,
                                       y = 15, 
                                       text = "Em geral, quanto maior \na população, maior \no consumo de petróleo",
                                       text_font_size = "12px",
                                       text_color = "darkslategray",
                                       text_alpha = 0.8))