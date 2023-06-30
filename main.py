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

# Pegando os textos e os gráficos dos arquivos de energia nuclear
from nuclear_text import nuclear_text_1, nuclear_text_2, nuclear_text_3, nuclear_text_4
from nuclear_bar_country_consumption import bar_rank_nuclear
from nuclear_line_year_electricity import grid_line_nuclear_contries
from nuclear_scatter_pib_energy import grid_scatter_gdp_nuclear_share

# Pegando os textos e os gráficos dos arquivos de carvão
from coal_text import title_html, first_graph, text_grid_graph, title_stackedbar, text_stackedbar, title_rank, text_rank
from coal_stacked import coal_bar_stacked
# from coal_rank import rank 

# Pegando os textos e os gráficos dos arquivos de energia nuclear
from coal_text import title_html, first_graph, text_grid_graph, title_stackedbar, text_stackedbar, title_rank, text_rank, coal_gif
from coal_stacked import coal_bar_stacked
from coal_continents import coal_grid


# Gerando a página sobre petróleo
# output_file("html_pages/oil.html")

# save(column(oil_text_1, 
#             graph_best_regions, 
#             oil_text_2, 
#             graph_pop_consumption, 
#             oil_text_3, 
#             oil_grid, 
#             oil_text_4))

# Gerando a página sobre energia eólica
# output_file("html_pages/wind.html")

# save(column(wind_text_0, 
#             wind_grid_comparison_graph,
#             wind_text_1,
#             wind_bar_top_countries_graph, 
#             wind_text_2, 
#             wind_grid_scatter_plot, 
#             wind_text_3, 
#             wind_line_brazil_evolution_graph, 
#             wind_text_4))

#  Gerando a página sobre energia nuclear
output_file("html_pages/nuclear.html")

save(column(nuclear_text_1, 
            grid_scatter_gdp_nuclear_share, 
            nuclear_text_2, 
            grid_line_nuclear_contries, 
            nuclear_text_3, 
            bar_rank_nuclear, 
            nuclear_text_4))

#  Gerando a página sobre carvão
# output_file("html_pages/coal.html")

# save(column(title_html,
#             first_graph, 
#             coal_grid,
#             text_grid_graph , 
#             title_stackedbar,
#             coal_bar_stacked, 
#             text_stackedbar, 
#             title_rank,
#             coal_gif,
#             text_rank))