from bokeh.models import Div

# Este módulo contém as partes do texto em HTML da página dos gráficos sobre energia eólica.

whind_text_1 = Div(text = """<html>

<head>
<title>Visualizações sobre energia eólica</title>

</head>

<body>

<h1>Visualizações sobre alteração percentual anual no consumo da energia proveniente do vento</h1>

Neste primeiro conjunto de dados construído pela função grid temos 6 análises que comparam a alteração percentual no consumo de energia eólica.
A comparação do Brasil com outros países é o centro da análise. Os países que foram escolhidos para essas comparações foram: China, Estados Unidos, Reino Unido, Canada, França e Argentina.
Esses cinco primeiros países citados foram escolhidos, pois são os cinco países que superaram o Brasil em índice de geração de energia por meio do vento no ano de 2020.
O último país escolhido foi a Argentina, para fazer uma comparação entre as maiores potências da América do Sul.

Quanto a parte técnica, temos 6 gráficos de linhas plotados em um grid de duas linhas e três colunas (2x3). 
As cores foram escolhidas no site Adobe Color a partir do recurso tríade, na qual o objetivo fossse a escolha de cores mais neutras.
O gráfico está todo em inglês e as escalas estão todas padronizadas.

<h2>Gráfico "ANNUAL PERCENTAGE CHANGE IN WIND CONSUMPTION"</h2>

</body>

</html>""")


wind_text_2 = Div(text = """</br> <p>O objetivo dessa visualização é exibir a evolução da produção de petróleo ao longo dos anos, olhando mais especificamente para as regiões do mundo que mais concentram essa produção: Oriente Médio, América do Norte, África, Ásia e Américas Central e do Sul. Dessa forma, o tipo de gráfico mais adequado para essa situação era o gráfico de linhas.</p> </br>

<p>A primeira coisa a se fazer após a plotagem das linhas era sua diferenciação, já que estavam todas idênticas. Para isso, foi utilizado o atributo de cor, selecionando-se cores que se destacassem umas das outras: amarelo, laranja, verde, azul e vermelho. Preferi optar por cores mais primárias e "distantes" para que não acontecesse qualquer confusão com relação a qual linha representa qual região. </br>
Em seguida, é claro que era necessária uma legenda para essas cores. Assim, criei-a na parte superior esquerda do gráfico para que não encobrisse parte dos dados.</p> </br>

<p>Por fim, adicionei anotações em caixa e em texto para destacar a forte queda na produção na década de 80, que afetou principalmente o Oriente Médio. Isso se deu devido à explosão da guerra entre o Iraque e o Irã, que gerou instabilidades na região. Assim, escolhi a cor vermelha para esses destaques para expressar a negatividade do fato.</p> </br>

<h2>Gráfico "Consumo de petróleo x População em 2019"</h2>""")


wind_text_3 = Div(text = """</br> <p>O objetivo dessa segunda visualização é mostrar a correlação existente entre a população dos países e seu consumo de petróleo. Para isso, é claro, foi utilizado um gráfico de dispersão.</p> </br>

<p>Antes de realizar a plotagem dos dados, separei os registros de acordo com sua média de consumo por habitante: os países cuja média estava acima da mundial e os países nos quais ela estava abaixo. Dessa forma, pude agrupá-los por meio da cor, caracterizando-os como vermelhos e verdes, respectivamente. Tentei fazer com que essa média fosse representada por meio de um degradê de cores, mas a diferença entre esses valores era tão pequena (questão de até milionésimos) que a variação dessas cores se tornou quase inexistente. Assim, preferi manter o modelo de 2 categorias.</br>
Após isso, novamente criei a legenda para os dados, indicando que os pontos vermelhos representavam os países com média de consumo de petróleo acima da mundial e que os verdes representavam os cuja média estava abaixo da global.</p> </br>

<p>Por fim, decidi fazer uma anotação simples, apenas destacando a proporção direta entre a população dos países e seu consumo de petróleo. Para que esse texto não ficasse tão destacado, atribui a ele uma cor cinza e tornei-o um pouco transparente, de tal forma que ele não "ofuscasse" as outras informações.</p> </br>

<h2>Gráfico "Variação anual da produção de petróleo dos 3 maiores produtores mundiais (1900 - 2020)"</h2>""")


wind_text_4 = Div(text = """</br> <p>O objetivo dessa terceira visualização é comparar as altas e as baixas na produção de petróleo dos Estados Unidos, da Rússia e da Arábia Saudita, que são, atualmente, os maiores produtores do mundo. Desse modo, optei pela utilização dos gráficos de barras para proporcionar melhor essa análise simultânea de vários momentos da história.</p> </br>

<p>Inicialmente, agrupei os dados desses países de acordo com o valor da variação anual na produção, separando-os nos anos em que essa variação foi positiva e negativa. Assim, consegui plotar os gráficos de forma que esses dois grupos possuíssem cores diferentes: verde para os positivos e vermelho para os negativos, o que melhora a percepção dos momentos de subida e de queda. Além disso, ajustei as dimensões dos gráficos para que todos tivessem o mesmo tamanho e se adequassem ao formato de gridplot.</p> </br>

<p>Em seguida, adicionei uma anotação em caixa e em texto em cada gráfico, destacando e explicando os momentos de maior variação em cada um. No dos Estados Unidos, destaquei o aumento na produção a partir de 2010 causada pelo desenvolvimento das tecnologias para extração e produção do petróleo de xisto. No da Rússia, comentei sobre a forte queda em 1990 provocada pelo fim da União Soviética. E, no da Arábia Saudita, abordei a intensa baixa na produção em 1980 gerada principalmente pela guerra entre Irã e Iraque.</br>
As caixas foram feitas com certa transparência para não encobrirem o gráfico e as cores foram escolhidas de acordo com o aspecto da informação: verde para a positiva e vermelho para as negativas.</br>
Além disso, inseri anotações em linha para deixar mais destacada a reta y = 0, de modo que é mais compreensível a localização da origem do gráfico.</p> </br>

<p>Por fim, para montar o gridplot, optei por colocar os três gráficos um acima do outro, de modo a alinhar as marcações do eixo x. Fiz isso para que fossem mais facilmente comparáveis as informações ao longo dos anos.</p> </br>

</body>

</html>""")
