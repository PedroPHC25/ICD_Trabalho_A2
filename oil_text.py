from bokeh.models import Div

# Este módulo contém as partes do texto em HTML da página dos gráficos sobre petróleo.

oil_text_1 = Div(text = """<html>

<head>
<title>Visualizações sobre petróleo</title>

</head>

<body>

<h1>Visualizações sobre petróleo e seus produtores e consumidores</h1>

<h2>Gráfico "Produção de petróleo das 5 maiores regiões produtoras (1900 - 2020)"</h2>""")


oil_text_2 = Div(text = """</br> <p>O objetivo dessa visualização é exibir a evolução da produção de petróleo ao longo dos anos, olhando mais especificamente para as regiões do mundo que mais concentram essa produção: Oriente Médio, América do Norte, África, Ásia e Américas Central e do Sul. Dessa forma, o tipo de gráfico mais adequado para essa situação era o gráfico de linhas.</p> </br>

<p>A primeira coisa a se fazer após a plotagem das linhas era sua diferenciação, já que estavam todas idênticas. Para isso, foi utilizado o atributo de cor, selecionando-se cores que se destacassem umas das outras: amarelo, laranja, verde, azul e vermelho. Preferi optar por cores mais primárias e "distantes" para que não acontecesse qualquer confusão com relação a qual linha representa qual região. </br>
Em seguida, é claro que era necessária uma legenda para essas cores. Assim, criei-a na parte superior esquerda do gráfico para que não encobrisse parte dos dados.</p> </br>

<p>Após isso, comecei a manipular os eixos. Exclui os ticks secundários pois considerava-os irrelevantes, de tal forma que acabavam sendo apenas um elemento de poluição. Inseri seus títulos de modo a ficarem precisos e concisos, e optei por não alterar seus tamanhos, mudando apenas seus estilos (de itálico para normal) e suas fontes para Arial.</p> </br>

<p>Feito isso, criei o título da visualização, indicando todos os dados presentes no gráfico: a produção de petróleo, os anos e as regiões. Reduzi a fonte para que ele coubesse na parte de cima do gráfico e centralizei-o com a visualização.</p> </br>

<p>Com relação ao fundo, considerei como melhor opção manter a cor branca, apenas alterando levemente a opacidade dos eixos, para que não ficassem tão destacados e incomodassem a visualização dos dados.</p> </br>

<p>Trabalhando agora com as ferramentas, depois de uma análise individual das possibilidades, avaliei como realmente úteis apenas as ferramentas "pan", para movimentar o gráfico, "wheel_zoom", para dar zoom, "reset", para retornar à posição inicial, e "save", para baixar uma versão da visualização. Além disso, desativei a logo do Bokeh da toolbar, pois não era necessária aqui, e habilitei a função "autohide", para que ela só fosse exibida quando solicitada.</p> </br>

<p>Por fim, adicionei anotações em caixa e em texto para destacar a forte queda na produção na década de 80, que afetou principalmente o Oriente Médio. Isso se deu devido à explosão da guerra entre o Iraque e o Irã, que gerou instabilidades na região. Assim, escolhi a cor vermelha para esses destaques para expressar a negatividade do fato.</p> </br>

<h2>Gráfico "Consumo de petróleo x População em 2019"</h2>""")


oil_text_3 = Div(text = """</br> <p>O objetivo dessa segunda visualização é mostrar a correlação existente entre a população dos países e seu consumo de petróleo. Para isso, é claro, foi utilizado um gráfico de dispersão.</p> </br>

<p>Antes de realizar a plotagem dos dados, separei os registros de acordo com sua média de consumo por habitante: os países cuja média estava acima da mundial e os países nos quais ela estava abaixo. Dessa forma, pude agrupá-los por meio da cor, caracterizando-os como vermelhos e verdes, respectivamente. Tentei fazer com que essa média fosse representada por meio de um degradê de cores, mas a diferença entre esses valores era tão pequena (questão de até milionésimos) que a variação dessas cores se tornou quase inexistente. Assim, preferi manter o modelo de 2 categorias.</br>
Após isso, novamente criei a legenda para os dados, indicando que os pontos vermelhos representavam os países com média de consumo de petróleo acima da mundial e que os verdes representavam os cuja média estava abaixo da global.</p> </br>

<p>Trabalhando agora com os eixos, primeiramente, configurei-os para a escala logarítmica, pois os dados estavam ficando muito agrupados na parte inferior esquerda. Assim, é possível exibir melhor sua distribuição. </br>
Em seguida, eliminei novamente os ticks secundários, pois avaliei-os como irrelevantes, ainda mais agora com a escala logarítmica, que os tornava bem confusos.</br>
Depois, converti os valores dos eixos de notação científica para números "normais". Entretanto, os valores do eixo x, que representa a população, acabaram ficando muito extensos e com muitos zeros, dificultando a leitura. Dessa forma, transformei-os em suas versões escritas por extenso para torná-los legíveis.</br>
Com relação aos seus títulos, da mesma forma que anteriormente, criei-os de uma forma curta e precisa, apenas modificando sua fonte e seu estilo.</p> </br>

<p>Após isso, adicionei e formatei o título, deixando-o com as mesmas configurações que o do primeiro gráfico e escrevendo-o de uma maneira que resumisse bem as informações presentes na visualização.</p> </br>

<p>A respeito do fundo, novamente, optei por manter a cor branca padrão, pois as cores do gráfico já estavam bem destacadas, fazendo com que uma outra cor de fundo o deixasse muito poluído visualmente. Assim, a única coisa que modifiquei foi a opacidade do grid, tornando-o um pouco mais sutil.</p> </br>

<p>Trabalhando agora com a toolbar, assim como na primeira visualização, ativei a funcionalidade "autohide" e ocultei a logo do Bokeh. Já com relação às ferramentas em si, mantive as mesmas que anteriormente, apenas adicionando a ferramenta "hover" e configurando-a para que exibisse o país correspondente a cada ponto quando o mouse fosse passado por ele. Como antes eu não tinha nenhum indicativo de quais eram aqueles países, considerei bastante útil essa informação adicional, que agrega valor aos dados do gráfico.</p> </br>

<p>Por fim, decidi fazer uma anotação simples, apenas destacando a proporção direta entre a população dos países e seu consumo de petróleo. Para que esse texto não ficasse tão destacado, atribui a ele uma cor cinza e tornei-o um pouco transparente, de tal forma que ele não "ofuscasse" as outras informações.</p> </br>

<h2>Gráfico "Variação anual da produção de petróleo dos 3 maiores produtores mundiais (1900 - 2020)"</h2>""")


oil_text_4 = Div(text = """</br> <p>O objetivo dessa terceira visualização é comparar as altas e as baixas na produção de petróleo dos Estados Unidos, da Rússia e da Arábia Saudita, que são, atualmente, os maiores produtores do mundo. Desse modo, optei pela utilização dos gráficos de barras para proporcionar melhor essa análise simultânea de vários momentos da história.</p> </br>

<p>Inicialmente, agrupei os dados desses países de acordo com o valor da variação anual na produção, separando-os nos anos em que essa variação foi positiva e negativa. Assim, consegui plotar os gráficos de forma que esses dois grupos possuíssem cores diferentes: verde para os positivos e vermelho para os negativos, o que melhora a percepção dos momentos de subida e de queda. Além disso, ajustei as dimensões dos gráficos para que todos tivessem o mesmo tamanho e se adequassem ao formato de gridplot.</p> </br>

<p>Em seguida, comecei a customizar os eixos. Primeiramente, ajustei os limites dos eixos x e y para que todos os gráficos mantivessem a mesma proporção e para que não ocorresse qualquer interpretação equivocada. Após isso, mais uma vez, retirei os ticks secundários por considerá-los irrelevantes.</br>
Pensei em tirar totalmente os eixos x dos dois gráficos de cima e deixar como referência apenas o de baixo. No entanto, dois problemas surgiram: primeiro, os valores dos anos estavam muito longe dos dados do primeiro gráfico, dificultando sua análise; e segundo, como os gráficos são móveis graças à interatividade, se os dois primeiros fossem movimentados, seria perdida totalmente a informação dos anos, já que o eixo do gráfico de baixo não se aplicaria mais. Assim, decidi manter os 3 eixos.</br>
Depois, apenas coloquei e configurei os títulos dos eixos da mesma forma que anteriormente, mas colocando o título do eixo x apenas no gráfico de baixo e o do eixo y apenas no do meio, já que não há necessidade de repeti-los por serem a mesma variável nos 3 gráficos.</p> </br>

<p>A seguir, inseri o título de cada gráfico como o nome do país correspondente. Nesse caso, optei por alinhá-los à esquerda para que ficassem mais separados de todas as outras informações. Além disso, infelizmente, não há uma maneira (não encontramos, pelo menos) de colocar um título no gridplot em si. Portanto, ele acabou sem um título próprio.</p> </br>

<p>Com relação ao fundo, novamente, a única alteração que fiz foi tornar os grids um pouco mais sutis.</p> </br>

<p>A respeito das ferramentas, mantive nessa visualização as mesmas do segundo gráfico, apenas com a mudança de que configurei o hover para exibir o ano correspondente a cada barra e o seu valor da variação anual, o que avaliei como útil para melhorar o detalhamento das informações. Assim como antes, ativei o autohide e exclui a logo do Bokeh. Finalmente, mudei a posição da toolbar de cima para a lateral direita dos gráficos, pois a montagem já estava um pouco grande demais em altura.</p> </br>

<p>Em seguida, adicionei uma anotação em caixa e em texto em cada gráfico, destacando e explicando os momentos de maior variação em cada um. No dos Estados Unidos, destaquei o aumento na produção a partir de 2010 causada pelo desenvolvimento das tecnologias para extração e produção do petróleo de xisto. No da Rússia, comentei sobre a forte queda em 1990 provocada pelo fim da União Soviética. E, no da Arábia Saudita, abordei a intensa baixa na produção em 1980 gerada principalmente pela guerra entre Irã e Iraque.</br>
As caixas foram feitas com certa transparência para não encobrirem o gráfico e as cores foram escolhidas de acordo com o aspecto da informação: verde para a positiva e vermelho para as negativas.</br>
Além disso, inseri anotações em linha para deixar mais destacada a reta y = 0, de modo que é mais compreensível a localização da origem do gráfico.</p> </br>

<p>Por fim, para montar o gridplot, optei por colocar os três gráficos um acima do outro, de modo a alinhar as marcações do eixo x. Fiz isso para que fossem mais facilmente comparáveis as informações ao longo dos anos.</p> </br>

</body>

</html>""")