output_file("nuclear_rascunho4.html")

paises_com_mais_usinas = ["United States", "France", "Japan", "Germany", "Russia", "South Korea"]
cinco_primeiros_países = data[data["country"].isin(paises_com_mais_usinas)]
cinco_primeiros_países = cinco_primeiros_países[cinco_primeiros_países["year"]=="2018"]
cinco_primeiros_países = cinco_primeiros_países.sort_values("nuclear_share_energy", ascending= False)
cinco_primeiros_países = cinco_primeiros_países[["country", "year", "nuclear_share_energy"]]

print(cinco_primeiros_países[""])

bar_year_nuclear = figure(x_range = cinco_primeiros_países["country"])
pais = cinco_primeiros_países["country"]
y = cinco_primeiros_países["nuclear_share_energy"]
bar_year_nuclear.vbar(x=pais, top=y, width=0.5)

# print(top)
show(bar_year_nuclear)



# data_source = ColumnDataSource(cinco_países[cinco_países["year"]=="2016"]) #Cria o ColumnDataSource
# bar_year_nuclear = figure(width= 650, height = 600, tools = "box_zoom, pan, reset, save, wheel_zoom")
# bar_year_nuclear.vbar(x = "country", top = "nuclear_elec_per_capita", source = data_source)


# data_pib_nuclear_elec = {"x": cinco_primeiros_países["country"], "y": cinco_primeiros_países["nuclear_electricity"]}

# data_source = ColumnDataSource(data=data_pib_nuclear_elec )

#  #configura o tamanho e as ferramentas pretendidas
# bar_year_nuclear = figure( x_range = cinco_primeiros_países["country"], tools = "box_zoom, pan, reset, save, wheel_zoom")

# bar_year_nuclear.vbar(x = "x", top = "y", source = data_source)

# show(bar_year_nuclear)



#deu errado

# output_file("nuclear_rascunho2.html")

# data_2019 = data.loc[data["year"]>=2019]
# data_2019_world = data_2019.loc[data_2019["country"]== "world"]
# print(data_2019_world)

# data_nuclear_2019 = {"x": data_2019_world["year"], "y": data_2019["nuclear_share_energy"]}
# data_source = ColumnDataSource(data=data_nuclear_2019)
# print(data_source)
# bar_nuclear_2019 = figure()
# bar_nuclear_2019.vbar(x= "year", top= "nuclear_share_energy", data = data_source, width=0.5)

# show(bar_nuclear_2019)


# Seleciona os dados a partir do ano 2000

# data_anos = data.sort_values("year", ascending= False)
# data_anos = data_anos[["country", "year", "nuclear_electricity"]]
# data_anos = data_anos.head(5)

# bar_19_20_nuclear = figure(x_range = data_anos["year"])
# anos = data_anos["year"]
# y = data_anos["nuclear_electricity"]
# bar_19_20_nuclear.vbar(x=anos, top=y, width=0.5)

# data_pib_nuclear_elec = {"x": data_anos["year"], "y": data["nuclear_electricity"]}

# data_source = ColumnDataSource(data=data_pib_nuclear_elec )

#  #configura o tamanho e as ferramentas pretendidas
# scatterplot_gdp_nuclear = figure( tools = "box_zoom, pan, reset, save, wheel_zoom")

# scatterplot_gdp_nuclear.vbar(x = "x", y = "y", source = data_source)

# # scatterplot_gdp_nuclear.xaxis[0].formatter.use_scientific=False


################################################################################################################################

# pais = cinco_países["country"]
# y = cinco_países["nuclear_consumption"]
# bar_rank_nuclear.vbar(x="country", top="nuclear_consumption", color = "color", width=0.5, source = data_source)


# bar_rank_nuclear.xaxis.major_label_overrides = {'United States': 'Estados Unidos'} 
                                                    #  'France': 'França', 
                                                    #  'China': 'China', 
                                                    #  'Russia': 'Rússia',
                                                    #  'South Korea': 'Coréia do Sul', 
                                                    #  'Canada': 'Canadá', 
                                                    #  'Ukraine': 'Ucrânia',
                                                    #  'Germany': 'Alemanha',
                                                    #  'Sweden': 'Suécia',
                                                    #  'United Kingdom': 'Reino \nUnido'}


# data_source = ColumnDataSource(data= best_countries_nuclear)

