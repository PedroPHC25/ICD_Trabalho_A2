# Importando as funções e métodos necessários
from bokeh.io import output_file, save
from bokeh.models import Div
from bokeh.layouts import column

# Pegando os textos e os gráficos dos arquivos de petróleo
from oil_text import oil_text_1, oil_text_2, oil_text_3, oil_text_4
from oil_production_year import graph_best_regions
from oil_population_consumption import graph_pop_consumption
from oil_variation_year import oil_grid

# Gerando a página sobre petróleo
output_file("oil.html")

save(column(oil_text_1, 
            graph_best_regions, 
            oil_text_2, 
            graph_pop_consumption, 
            oil_text_3, 
            oil_grid, 
            oil_text_4))