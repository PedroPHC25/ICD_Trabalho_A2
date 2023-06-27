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


