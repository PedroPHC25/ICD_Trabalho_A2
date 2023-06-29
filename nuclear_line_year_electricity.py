from bokeh.plotting import figure
from bokeh.models import Range1d, Label
from bokeh.models.annotations import BoxAnnotation
from bokeh.layouts import gridplot
from cds_generator import cds_nuclear_eua, cds_nuclear_france, cds_nuclear_germany, cds_nuclear_japan, cds_nuclear_russia, cds_nuclear_korea



"""EUA"""

#Gera o gráfico de linha
line_year_nuclear_EUA = figure(width= 400, height = 400, 
                               tools = "box_zoom, pan, reset, save, wheel_zoom",
                               tooltips = [("Ano", "@year"),
                                           ("Energia nuclear", "@nuclear_electricity")])

renderer = line_year_nuclear_EUA.line(x = "year", y = "nuclear_electricity", source = cds_nuclear_eua, color="RoyalBlue")

# título
line_year_nuclear_EUA.title.text = "Estados Unidos da América"
line_year_nuclear_EUA.title.text_color = "MidnightBlue"
line_year_nuclear_EUA.title.text_font = "Arial"
line_year_nuclear_EUA.title.text_font_size = "20px"
line_year_nuclear_EUA.title.align = "center"

# Eixos
line_year_nuclear_EUA.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_EUA.xaxis.minor_tick_in = 5
line_year_nuclear_EUA.xaxis.major_label_orientation = "horizontal"
line_year_nuclear_EUA.yaxis.axis_label = "Geração de energia nuclear (TWh)"  #título do eixo y
line_year_nuclear_EUA.axis.axis_label_text_font = "normal" #Retira o itálico
line_year_nuclear_EUA.yaxis.minor_tick_line_color = "black"
line_year_nuclear_EUA.yaxis.minor_tick_in = 5
line_year_nuclear_EUA.axis.axis_label_text_font_style = "normal"
line_year_nuclear_EUA.xaxis[0].ticker.num_minor_ticks = 0 #número de ticks menores eixo x
line_year_nuclear_EUA.yaxis[0].ticker.num_minor_ticks = 0 #número de ticks menores eixo y
line_year_nuclear_EUA.yaxis.major_label_orientation = "horizontal"
line_year_nuclear_EUA.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo x
line_year_nuclear_EUA.yaxis.axis_label_text_font ="Arial" #Fonte do título do eixo y
line_year_nuclear_EUA.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo x
line_year_nuclear_EUA.xaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo y
line_year_nuclear_EUA.xaxis.axis_label_text_font_size = "20px" #Tamnho da fonte do título do eixo x
line_year_nuclear_EUA.yaxis.axis_label_text_font_size = "20px" #Tamnho da fonte do título do eixo y
line_year_nuclear_EUA.y_range = Range1d(start = 0, end = 850)   #muda a escala do eixo y

#Glifo
glyph_renderer = renderer.glyph #pega o renderizador do glifo
glyph_renderer.line_width= 3.5 #Define o tamanho da linha

# Fundo
line_year_nuclear_EUA.background_fill_color = ("WhiteSmoke") #Cor de fundo

#Grid
line_year_nuclear_EUA.xgrid.grid_line_color = "LightGray" #Cor do grid
line_year_nuclear_EUA.xgrid.grid_line_alpha = 0.6  #transparencia do gride
line_year_nuclear_EUA.ygrid.grid_line_color = "LightGray" #Cor do grid
line_year_nuclear_EUA.ygrid.grid_line_alpha = 0.6  #transparencia do gride


"""France"""

line_year_nuclear_France = figure(width= 400, height = 400, 
                                  tools = "box_zoom, pan, reset, save, wheel_zoom",
                                  tooltips = [("Ano", "@year"),
                                              ("Energia nuclear", "@nuclear_electricity")])

renderer = line_year_nuclear_France.line(x = "year", y = "nuclear_electricity", source = cds_nuclear_france, color="RoyalBlue")

# título
line_year_nuclear_France.title.text = "França"
line_year_nuclear_France.title.text_color = "MidnightBlue"
line_year_nuclear_France.title.text_font = "Arial"
line_year_nuclear_France.title.text_font_size = "20px"
line_year_nuclear_France.title.align = "center"

# Eixos
line_year_nuclear_France.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_France.xaxis.minor_tick_in = 5
line_year_nuclear_France.xaxis[0].ticker.num_minor_ticks = 0 #número de ticks menores
line_year_nuclear_France.yaxis[0].ticker.num_minor_ticks = 0
line_year_nuclear_France.xaxis.major_label_orientation = "horizontal"
line_year_nuclear_France.axis.axis_label_text_font = "normal" #retira o itálico
line_year_nuclear_France.yaxis.minor_tick_line_color = "black"
line_year_nuclear_France.yaxis.minor_tick_in = 5
line_year_nuclear_France.yaxis.major_label_orientation = "horizontal"
line_year_nuclear_France.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo
line_year_nuclear_France.yaxis.axis_label_text_font ="Arial"
line_year_nuclear_France.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo
line_year_nuclear_France.xaxis.axis_label_text_color = 'MidnightBlue'
line_year_nuclear_France.xaxis.axis_label_text_font_size = "20px" #Tamnho da fonte do título dos eixos
line_year_nuclear_France.yaxis.axis_label_text_font_size = "20px"
line_year_nuclear_France.y_range = Range1d(start = 0, end = 850)

# Fundo
line_year_nuclear_France.background_fill_color = ("WhiteSmoke")

#Grid
line_year_nuclear_France.background_fill_color = ("WhiteSmoke")
line_year_nuclear_France.xgrid.grid_line_color = "LightGray"
line_year_nuclear_France.xgrid.grid_line_alpha = 0.6  #transparencia do gride
line_year_nuclear_France.ygrid.grid_line_color = "LightGray"
line_year_nuclear_France.ygrid.grid_line_alpha = 0.6  #transparencia do gride

#Glifo
glyph_renderer = renderer.glyph #pega o renderzador do glifo
glyph_renderer.line_width= 3.5

"""Japan"""
line_year_nuclear_Japan = figure(width= 400, height = 400, 
                                 tools = "box_zoom, pan, reset, save, wheel_zoom",
                                 tooltips = [("Ano", "@year"),
                                             ("Energia nuclear", "@nuclear_electricity")])

renderer = line_year_nuclear_Japan.line(x = "year", y = "nuclear_electricity", source = cds_nuclear_japan, color="RoyalBlue")
# título
line_year_nuclear_Japan.title.text = "Japão"
line_year_nuclear_Japan.title.text_color = "MidnightBlue"
line_year_nuclear_Japan.title.text_font = "Arial"
line_year_nuclear_Japan.title.text_font_size = "20px"
line_year_nuclear_Japan.title.align = "center"

# Eixos
line_year_nuclear_Japan.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_Japan.xaxis.minor_tick_in = 5
line_year_nuclear_Japan.xaxis[0].ticker.num_minor_ticks = 0 #número de ticks menores
line_year_nuclear_Japan.yaxis[0].ticker.num_minor_ticks = 0
line_year_nuclear_Japan.xaxis.major_label_orientation = "horizontal"
line_year_nuclear_Japan.axis.axis_label_text_font_style = "normal"
line_year_nuclear_Japan.yaxis.minor_tick_line_color = "black"
line_year_nuclear_Japan.yaxis.minor_tick_in = 5
line_year_nuclear_Japan.yaxis.major_label_orientation = "horizontal"
line_year_nuclear_Japan.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo
line_year_nuclear_Japan.yaxis.axis_label_text_font ="Arial"
line_year_nuclear_Japan.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo
line_year_nuclear_Japan.xaxis.axis_label_text_color = 'MidnightBlue'
line_year_nuclear_Japan.xaxis.axis_label_text_font_size = "20px" #Tamnho da fonte do título dos eixos
line_year_nuclear_Japan.yaxis.axis_label_text_font_size = "20px"
line_year_nuclear_Japan.y_range = Range1d(start = 0, end = 850)

# Fundo
line_year_nuclear_Japan.background_fill_color = ("WhiteSmoke")

#Grid
line_year_nuclear_Japan.xgrid.grid_line_color = "LightGray"
line_year_nuclear_Japan.xgrid.grid_line_alpha = 0.6  #transparencia do gride
line_year_nuclear_Japan.ygrid.grid_line_color = "LightGray"
line_year_nuclear_Japan.ygrid.grid_line_alpha = 0.6  #transparencia do gride

#Glifo
glyph_renderer = renderer.glyph #pega o renderizador do glifo
glyph_renderer.line_width= 3.5

#Anotação
box_annotation = BoxAnnotation(left = 2010, right = 2017, fill_color = "red", fill_alpha = 0.2)
line_year_nuclear_Japan.add_layout(box_annotation)

line_year_nuclear_Japan.add_layout(Label(x = 2009, y = 500,
                                       text = "Em 2011 ocorre o acidente\n nuclear de Fukushima Daiichi",
                                       text_align = "right",
                                       text_font_size = "12px",
                                       text_color = "red", 
                                       text_alpha = 0.7))

"""Germany"""
line_year_nuclear_Germany = figure(width= 400, height = 400, 
                                   tools = "box_zoom, pan, reset, save, wheel_zoom",
                                   tooltips = [("Ano", "@year"),
                                                      ("Energia nuclear", "@nuclear_electricity")])
renderer = line_year_nuclear_Germany.line(x = "year", y = "nuclear_electricity", source = cds_nuclear_germany, color="RoyalBlue")
# ferramnetas
line_year_nuclear_Germany.toolbar.logo = None #retira a logo
line_year_nuclear_Germany.toolbar.autohide = True #deixa o barra de ferramentas invisível
line_year_nuclear_Germany.toolbar_location = "below" #define a localização barra de ferramentas
# título
line_year_nuclear_Germany.title.text = "Alemanha"
line_year_nuclear_Germany.title.text_color = "MidnightBlue"
line_year_nuclear_Germany.title.text_font = "Arial"
line_year_nuclear_Germany.title.text_font_size = "20px"
line_year_nuclear_Germany.title.align = "center"
# Eixos
line_year_nuclear_Germany.xaxis.axis_label = "Ano"  #título do eixo x
line_year_nuclear_Germany.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_Germany.xaxis.minor_tick_in = 5
line_year_nuclear_Germany.xaxis[0].ticker.num_minor_ticks = 0 #número de ticks menores
line_year_nuclear_Germany.yaxis[0].ticker.num_minor_ticks = 0
line_year_nuclear_Germany.xaxis.major_label_orientation = "horizontal"
line_year_nuclear_Germany.yaxis.axis_label = "Geração de energia nuclear (TWh) "  #título do eixo y
line_year_nuclear_Germany.axis.axis_label_text_font_style = "normal"
line_year_nuclear_Germany.yaxis.minor_tick_line_color = "black"
line_year_nuclear_Germany.yaxis.minor_tick_in = 5
line_year_nuclear_Germany.yaxis.major_label_orientation = "horizontal"
line_year_nuclear_Germany.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo
line_year_nuclear_Germany.yaxis.axis_label_text_font ="Arial"
line_year_nuclear_Germany.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo
line_year_nuclear_Germany.xaxis.axis_label_text_color = 'MidnightBlue'
line_year_nuclear_Germany.xaxis.axis_label_text_font_size = "20px" #Tamnho da fonte do título dos eixos
line_year_nuclear_Germany.yaxis.axis_label_text_font_size = "20px"
line_year_nuclear_Germany.y_range = Range1d(start = 0, end = 850)

# Fundo
line_year_nuclear_Germany.background_fill_color = ("WhiteSmoke")

#Grid
line_year_nuclear_Germany.xgrid.grid_line_color = "LightGray"
line_year_nuclear_Germany.xgrid.grid_line_alpha = 0.6  #transparencia do gride
line_year_nuclear_Germany.ygrid.grid_line_color = "LightGray"
line_year_nuclear_Germany.ygrid.grid_line_alpha = 0.6  #transparencia do gride

#Glifo
glyph_renderer = renderer.glyph #pega o renderizador do glifo
glyph_renderer.line_width= 3.5

"""Russia"""
line_year_nuclear_Russia = figure(width= 400, height = 400, 
                                  tools = "box_zoom, pan, reset, save, wheel_zoom",
                                  tooltips = [("Ano", "@year"),
                                              ("Energia nuclear", "@nuclear_electricity")])

renderer = line_year_nuclear_Russia.line(x = "year", y = "nuclear_electricity", source = cds_nuclear_russia, color="RoyalBlue")

# título
line_year_nuclear_Russia.title.text = "Rússia"
line_year_nuclear_Russia.title.text_color = "MidnightBlue"
line_year_nuclear_Russia.title.text_font = "Arial"
line_year_nuclear_Russia.title.text_font_size = "20px"
line_year_nuclear_Russia.title.align = "center"

# Eixos
line_year_nuclear_Russia.xaxis.axis_label = "Ano"  #título do eixo x
line_year_nuclear_Russia.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_Russia.xaxis.minor_tick_in = 5
line_year_nuclear_Russia.axis.axis_label_text_font_style = "normal"
line_year_nuclear_Russia.xaxis[0].ticker.num_minor_ticks = 0 #número de ticks menores
line_year_nuclear_Russia.yaxis[0].ticker.num_minor_ticks = 0
line_year_nuclear_Russia.xaxis.major_label_orientation = "horizontal"

# line_year_nuclear_Russia.yaxis.axis_label = "Geração de energia nuclear(TWh) "  #título do eixo y
line_year_nuclear_Russia.axis.axis_label_text_font = "normal"
line_year_nuclear_Russia.yaxis.minor_tick_line_color = "black"
line_year_nuclear_Russia.yaxis.minor_tick_in = 5
line_year_nuclear_Russia.yaxis.major_label_orientation = "horizontal"
line_year_nuclear_Russia.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo
line_year_nuclear_Russia.yaxis.axis_label_text_font ="Arial"
line_year_nuclear_Russia.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo
line_year_nuclear_Russia.xaxis.axis_label_text_color = 'MidnightBlue'
line_year_nuclear_Russia.xaxis.axis_label_text_font_size = "20px" #Tamnho da fonte do título dos eixos
line_year_nuclear_Russia.yaxis.axis_label_text_font_size = "20px"
line_year_nuclear_Russia.y_range = Range1d(start = 0, end = 850)

# Fundo
line_year_nuclear_Russia.background_fill_color = ("WhiteSmoke")

#Grid
line_year_nuclear_Russia.xgrid.grid_line_color = "LightGray"
line_year_nuclear_Russia.xgrid.grid_line_alpha = 0.6  #transparencia do gride
line_year_nuclear_Russia.ygrid.grid_line_color = "LightGray"
line_year_nuclear_Russia.ygrid.grid_line_alpha = 0.6  #transparencia do gride

#Glifo
glyph_renderer = renderer.glyph #pega o renderzador do glifo
glyph_renderer.line_width= 3.5

"""South Korea"""
line_year_nuclear_SouthKorea = figure(width= 400, height = 400, 
                                      tools = "box_zoom, pan, reset, save, wheel_zoom",
                                      tooltips = [("Ano", "@year"),
                                                  ("Energia nuclear", "@nuclear_electricity")])

renderer = line_year_nuclear_SouthKorea.line(x = "year", y = "nuclear_electricity", source = cds_nuclear_korea, color="RoyalBlue")

# título
line_year_nuclear_SouthKorea.title.text = "Coreia do Sul"
line_year_nuclear_SouthKorea.title.text_color = "MidnightBlue"
line_year_nuclear_SouthKorea.title.text_font = "Arial"
line_year_nuclear_SouthKorea.title.text_font_size = "20px"
line_year_nuclear_SouthKorea.title.align = "center"

# Eixos
line_year_nuclear_SouthKorea.xaxis.axis_label = "Ano"  #título do eixo x
line_year_nuclear_SouthKorea.xaxis.minor_tick_line_color = "black" 
line_year_nuclear_SouthKorea.xaxis.minor_tick_in = 5
line_year_nuclear_SouthKorea.axis.axis_label_text_font_style = "normal"
line_year_nuclear_SouthKorea.xaxis[0].ticker.num_minor_ticks = 0 #número de ticks menores
line_year_nuclear_SouthKorea.yaxis[0].ticker.num_minor_ticks = 0
line_year_nuclear_SouthKorea.xaxis.major_label_orientation = "horizontal"
line_year_nuclear_SouthKorea.axis.axis_label_text_font = "normal"
line_year_nuclear_SouthKorea.yaxis.minor_tick_line_color = "black"
line_year_nuclear_SouthKorea.yaxis.minor_tick_in = 5
line_year_nuclear_SouthKorea.yaxis.major_label_orientation = "horizontal"
line_year_nuclear_SouthKorea.xaxis.axis_label_text_font ="Arial" #Fonte do título do eixo
line_year_nuclear_SouthKorea.yaxis.axis_label_text_font ="Arial"
line_year_nuclear_SouthKorea.yaxis.axis_label_text_color = 'MidnightBlue' #cor do título do eixo
line_year_nuclear_SouthKorea.xaxis.axis_label_text_color = 'MidnightBlue'
line_year_nuclear_SouthKorea.xaxis.axis_label_text_font_size = "20px" #Tamnho da fonte do título dos eixos
line_year_nuclear_SouthKorea.yaxis.axis_label_text_font_size = "20px"
line_year_nuclear_SouthKorea.y_range = Range1d(start = 0, end = 850)

# Fundo
line_year_nuclear_SouthKorea.background_fill_color = ("WhiteSmoke")

#Grid
line_year_nuclear_SouthKorea.xgrid.grid_line_color = "LightGray"
line_year_nuclear_SouthKorea.xgrid.grid_line_alpha = 0.6  #transparencia do gride
line_year_nuclear_SouthKorea.ygrid.grid_line_color = "LightGray"
line_year_nuclear_SouthKorea.ygrid.grid_line_alpha = 0.6  #transparencia do gride

#Glifo
glyph_renderer = renderer.glyph #pega o renderzador do glifo
glyph_renderer.line_width= 3.5

#Junção dos gráficos
plot = gridplot([[line_year_nuclear_EUA, line_year_nuclear_France, line_year_nuclear_Japan],
                 [line_year_nuclear_Germany, line_year_nuclear_Russia, line_year_nuclear_SouthKorea]])
