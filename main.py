# Importando as funções e métodos necessários
from bokeh.io import output_file, save
from bokeh.layouts import column

# Pegando os textos e os gráficos dos arquivos de petróleo
from oil_text import oil_text_1, oil_text_2, oil_text_3, oil_text_4
from oil_line_production_year import graph_best_regions
from oil_scatter_population_consumption import graph_pop_consumption
from oil_grid_variation_year import oil_grid

# Pegando os textos e os gráficos dos arquivos de energia eólica
from wind_text import wind_text_0, wind_text_1, wind_text_2, wind_text_3, wind_text_4
from wind_bar_top_countries import wind_bar_top_countries_graph
from wind_grid_comparison_six_countries import wind_grid_comparison_graph
from wind_grid_scatter_plot import wind_grid_scatter_plot
from wind_line_brazil_evolution import wind_line_brazil_evolution_graph

# Gerando a página sobre petróleo
output_file("html_pages/oil.html")

save(column(oil_text_1, 
            graph_best_regions, 
            oil_text_2, 
            graph_pop_consumption, 
            oil_text_3, 
            oil_grid, 
            oil_text_4))

# Gerando a página sobre energia eólica
output_file("html_pages/wind.html")

save(column(wind_text_0, 
            wind_grid_comparison_graph,
            wind_text_1,
            wind_bar_top_countries_graph, 
            wind_text_2, 
            wind_grid_scatter_plot, 
            wind_text_3, 
            wind_line_brazil_evolution_graph, 
            wind_text_4))