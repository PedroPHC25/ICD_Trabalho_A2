from bokeh.models import Div

# Este módulo contém as partes do texto em HTML da página dos gráficos sobre energia eólica.

wind_text_0 = Div(text = """<html>

<head>
<title>Visualizações sobre Energia Eólica</title>

</head>

<body>

<h1>VISUALIZAÇÕES SOBRE ENERGIA EÓLICA</h1>

<h2>Gráfico 1:  "ANNUAL PERCENTAGE CHANGE IN WIND CONSUMPTION"</h2>""")


wind_text_1 = Div(text = """</br> <p style="font-size:16px">Neste primeiro conjunto de dados construído pela função grid temos 6 análises que comparam a alteração 
percentual no consumo de energia eólica. A comparação do Brasil com outros países é o centro da análise. 
Os países que foram escolhidos para essas comparações foram: China, Estados Unidos, Reino Unido, Canada, França e 
Argentina. Esses cinco primeiros países citados foram escolhidos, pois são os cinco países que superaram o Brasil em
índice de geração de energia por meio do vento no ano de 2020. O último país escolhido foi a Argentina, para fazer 
uma comparação entre as maiores potências da América do Sul. </p> </br>

<p style="font-size:16px"> Quanto a parte técnica, temos 6 gráficos de linhas plotados em um grid de duas linhas e três colunas (2x3). 
As cores foram escolhidas no site Adobe Color a partir do recurso tríade, na qual o objetivo era a escolha de cores mais neutras.
O gráfico está todo em inglês e as escalas estão todas padronizadas. </p> </br>

<h2>Gráfico 2: "ELECTRICITY GENERATION FROM WIND BY COUNTRY IN 2020"</h2>""")


wind_text_2 = Div(text = """</br> <p style="font-size:16px"> Nesta segunda visualização temos um gráfico de barras que mostra os nove países que lideram o ranking do 
índice de eletricidade gerada a partir do vento no ano de 2020. O ano de 2020 foi escolhido para esta análise por
ser o ano mais recente presente na base de dados. O objetivo era chegar a conclusões que mais estivesse próximo da
realidade atual. Os países são, em ordem decrescente no ranking: China, Estados Unidos, Alemanha, Reino Unido, 
India, Brasil, Espanha, França e Canadá. </p> </br>

<p style="font-size:16px">Além disso, fiz um agrupamento por continente. Os países de um mesmo continente estão preenchidos com a mesma 
cor. Isto foi feito para que ficasse claro quais países se destacam na produção de energia eólica e quais os 
continentes que também se destacam aparecendo mais vezes no ranking. Nesse contexto, o continente que mais aparece 
repetidas vezes é o Europeu, mas o país que mais contribui com a geração de energia eólica é a China(um país 
asiático). </p> </br>

<p style="font-size:16px">Quanto a parte técnica, temos um gráficos de barras plotado usando recursos do bokeh. As cores foram escolhidas 
no site Adobe Color a partir do recurso tríade, na qual o objetivo fossse a escolha de cores mais neutras. Perceba, 
a partir de agora, que os gráficos passados e os futuros estão todos seguindo a mesma paleta de cores. Nem todas 
as cores da paleta escolhida estão em todos os gráficos, mas todos os gráficos são construídos com a mesma paleta. 
Isso foi feito para que ao final, ao juntarmos todas as peças gráficas, elas permaneçam coesas entre si não apenas 
pela temática, que é sobre energia eólica, mas também pelas cores, ou seja, pela parte visual. Ademais, 
o gráfico está em inglês. </p> </br> 

<h2>Gráfico 3: "RATIO BETWEEN WIND ELECTRICITY AND WIND ENERGY (BOTH PER CAPITA)"</h2>""")


wind_text_3 = Div(text = """</br> <p style="font-size:16px">Nesta terceira peça de visualização temos um segundo grid. Nesse caso, temos o mesmo gráfico plotando em 
escalas diferentes. A temática aqui explorada foi a relação entre o índice de energia produzida a partir do vento e
o índice de energia produzido a partir do vento. Perceba que estamos falando de coisas diferentes, pois a definição
de energia é muito mais ampla que a de energia elétrica que é apenas um tipo de energia. Podemos ter também a 
energia mecâncica. A plotagem de duas escalas foi feita para que o leitor pudesse ter diferentes percepções acerca
dos resultados. No primeiro gráfico de maior escala, a impressão que dá é que estamos falando de uma reta perfeita
com apenas um outlier. Depois, ajusto a escala para que o país que representa o outlier não seja plotado e possamos
ver com mais detalhes os outros países e a tendência mundial (que é representada por um país chamado World). </p> </br>

<p style="font-size:16px">Quanto a parte técnica, temos dois gráficos de dispersão plotados usando recursos do bokeh. As cores foram 
escolhidas no site Adobe Color a partir do recurso tríade, na qual o objetivo fossse a escolha de cores mais 
neutras. Perceba que este gráfico segue o mesmo padrão de cores que os anteriores. O gráfico está em inglês. 
O contorno dos pontos e o preenchimento dos pontos estão coloridos de forma distinta. Foi adicionado uma reta de 
regressão. E por último, foi adicionado os recursos tools e tooltips para que ao passar o mouse por cima dos pontos,
seja possível visualizar o país ao qual o dado se refere. </p> </br>

<h2>Gráfico 4: PER CAPITA CONSUMPTION OF ELECTRICITY GENERATED BY WIND IN BRAZIL IN THE LAST 50 YEARS</h2>""")

wind_text_4 = Div(text = """</br> <p style="font-size:16px"> Por último, mas não menos importante temos mais um gráfico de linhas. Este representa a evolução do Brasil, ao 
longo dos últimos 50 anos, quanto ao consumo per capita de energia eólica.  </p> </br>

<p style="font-size:16px"> O gráfico mostra que esse consumo se manteve praticamente constante até o final da década de 2000. O começo da
década seguinte marca um crescimento quase que exponencial que colocou o Brasil em posição de destaque perante ao 
mundo no que se trata de produção e consumo de energia eólica. Um discreto texto foi adicionado na área do gráfico
para explicar esse crescimento fortemente significativo, que é resulto de muitos investimentos do Governo Brasileiro
e de parcerias público-privadas por todo o país. </p> </br>

<p style="font-size:16px"> Quanto a parte técnica, temos um gráfico de linha plotado usando recursos do bokeh. As cores foram escolhidas
 no site Adobe Color a partir do recurso tríade, na qual o objetivo fossse a escolha de cores mais neutras. 
 Novamente, este gráfico segue o mesmo padrão de cores que os anteriores. O gráfico está em inglês.  </p> </br>

<b> Autora: Maria Eduarda Mesquita Magalhães </b>

</body>

</html>""")