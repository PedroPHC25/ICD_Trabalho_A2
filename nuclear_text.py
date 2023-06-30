from bokeh.models import Div

# Este módulo contém as partes do texto em HTML da página dos gráficos sobre energia nuclear.

nuclear_text_1 = Div(text = """<html>

<head>

<title style="color:#00075F;">Visualizações sobre energia nuclear </title> 

</head>

<body>
<h1 style="color:#00075F;">Visualizações sobre energia nuclear </h1> 

<h2 style="color:#00075F;">Gráfico sobre consumo de energia nuclear e o PIB de cada país. </h2>

""")

nuclear_text_2 = Div(text = """<p style="text-align:justify; font-size:16px;">

O objetivo dessa visualização é exibir a correlação entre a participação da energia nuclear no consumo de 
cada país e o seu PIB, de maneira à observar se há alguma interdependencia entre as duas variáveis. 
Tendo isso em mente, o tipo de gráfico mais adequado para esse tipo de visualização seria o gráfico de dispersão, 
que plota uma bolha para cada país presente no dado.
</p> </br>

<p style="text-align:justify; font-size:16px;">
Para iniciar a produção do gráfico, foram selecionados os dados do ano pretendido, além de se criar uma nova 
coluna de dado chamada "gdp_in_bi" que divide os valores da coluna original por 1000000000. De maneira a facilitar o processo, 
foi criado um dicionário que corresponde x, y e z, com as colunas 'gdp_in_bi', 'nuclear_share_energy' e 'country'.
</p> </br>

<p style="text-align:justify; font-size:16px;">
Após isso, gerei o scatterplot, definindo o tamanho e as ferramentas presentes, o qual o PIB representa o 
eixo x e a energia nuclear representa o eixo y e também o tamanho da bolha, de maneira a dar mais enfâse na 
observação dessa variável. A cor das bolhas foi escolhida para ser uma cor escura que destacasse, mas ainda neutra, 
como esse tom de azul, com o intuito de não gerar excesso de informação visual, além de trazer transparência para 
ajudar na representação de países/bolhas próximas.
</p></br>

<p style="text-align:justify; font-size:16px;">
Um destaque para a ferramenta "tooltips" que apresenta uma etiqueta de breve descrição de cada bolha, quando o 
mouse está posicionado nela. Essa mesma ferramenta estará presentes nos gráficos seguintes, pois acredito que adiciona informações específicas que são interessantes na leitura.
</p></br>

<p style="text-align:justify; font-size:16px;">
Em seguida foram definidas todas as características do título do gráfico e dos eixos, como cor, tamanho, fonte, 
alinhamento, orientação e estilo, sempre pensando na harmonia do conjunto formado. Outra mudança realizada foi 
a forma do eixos, alterando atributos como o tamanho do tick, retirando o tick menores, arrumando a orientação e o formato 
da escala, detalhes que fazem a diferença e ajudam a simplificar as informações transmitidas.
</p></br>

<p style="text-align:justify; font-size:16px;">
Uma adição feita foi a anotação de texto que destaca a França como o país em que a energia nuclear teve a maior participação 
em 2000, de modo a chamar a atenção do leitor, por ser uma informação importante.
</p></br>

<p style="text-align:justify; font-size:16px;">
Por fim, modifiquei a cor de fundo do gráfico, tirando o branco brilhante que pode trazer cansaço na visualização e 
opitando por um tom de cinza claro que harmoniza com o restante e ao mesmo tempo não tira o foco dos outros elementos de destaque. 
</p></br></br>

<p style="text-align:justify; font-size:16px;">
Ademais, o da direta é o mesmo gráfico com uma pequena interatividade adicionada. Nele o leitor pode escolher o tamanho dos círculos, deslizando o controle e a cor dos cículos, digitando na caixa abaixo, que aceita tanto o código em formato hexadecimal ou RGB, como o nome da cor pretendida. 
</p></br></br>

<h2 style="color:#00075F;">Grid dos 6 países que mais produzem energia nuclear (1985-2020)</h2>
""")

nuclear_text_3 = Div(text = """
<p style="text-align:justify; font-size:16px;">

O objetivo da segunda visualização é trazer uma linha do tempo dos seis países que mais geram energia nuclear, de maneira a observar a evolução do uso de usinas nucleares de 1985 à 2020, que são os anos presentes na base de dados escolhida. 
</p></br>

<p style="text-align:justify; font-size:16px;">
Para a produção do Grid, foram gerados os gráficos de cada país separadamente, para só ao final junta-los em uma só visualização.
O primeiro país foi os Estados Unidos da América. Para ele, selecionei o dado e gerei o ColumnDataSource. Em seguida, produzi o gráfico de linha, atribuindo à 'renderer'.  
</p></br>

<p style="text-align:justify; font-size:16px;">
O próximo passo é definir todas as especificações do título do gráfico, seguindo na mesma linha das caracteríticas da primeira visualização, mantendo os mesmos objetivos.
Depois disso, há a especificação de todos as caracteríticas que dizem respeito aos eixos. Apectos como tamanho, cor e quantidade de ticks; orientação das escalas; fonte, cor, tamanho e estilo dos títulos dos eixos; e, por último, a definição da escala (começando de 0 até 850, de modo à deixar todos os gráficos do grid com a mesma escala e sempre começando do zero, para ser possível uma real comparação entre eles).
</p></br>

<p style="text-align:justify; font-size:16px;">
Após isso, defini-se o glifo, especificando o tamanho da linha, não muito fina ou grossa, com o intuito de encontrar um equilíbrio para uma visualização agradável. Além disso, ajusta-se o grid.
</p></br>

<p style="text-align:justify; font-size:16px;">
Todas essas especificações foram repetidas para todos os gráficos de cada um dos seis países seguintes. 
No gráfico do Japão foi adicionado também uma anotação de texto e uma de caixa em vermelho, com o intuito de destacar e explicar o fato que acontece em 2011, que faz com que a produção de energia nuclear do Japão caia bruscamente e chegue a zero em 2014, chamando mais ainda a atenção do leitor.
</p></br>

<p style="text-align:justify; font-size:16px;">
Além disso, optei por retirar o título do eixo x dos três primeiros gráficos, por se tratar do mesmo dado, diminuindo assim a poluição pela repetição, deixando essa informação apenas nos três últimos gráficos. O mesmo foi feito para o eixo y dos quatro gráficos da direita. 
</p></br>

<h2 style="color:#00075F;">Gráfico de ranking dos dez países que mais consomem energia primária proveniente da energia nuclear</h2>
""")

nuclear_text_4 = Div(text = """
<p style="text-align:justify; font-size:16px;">
Objetivo dessa última visualização é rankear os dez países que mais consomem energia primária proveniente da energia nuclear em 2018. Para isso optei pelo gráfico de barras que representa melhoor essa comparação. 
</p></br>   
    
    
<p style="text-align:justify; font-size:16px;">
Primeiramente, há a filtragem da base de dados, selecionando apenas os 10 primeiros países e o ano escolhido. Após isso, foi criada uma nova coluna que contém o continente correspondente à cada país. Em seguida, optei por utilizar da cor para agrupar por continente os países, trazendo uma informação a mais, que fica bem nítida visualmente. Para isso cria-se um dicionário que atribui uma cor para cada continente. As cores foram escolhidas de maneira a serem bem distintas e destacadas, mas não muito saturadas e com um pouco de transparência, de modo a ficar mais agradável a leitura.

</p></br>
<p style="text-align:justify; font-size:16px;">
Com os dados prontos, foi gerado o gráfico de barras, com um continente por vez. Depois, define-se as ferramentas pretendidas e o título seguindo o padrão dos primeiros gráficos.
</p></br>
    
<p style="text-align:justify; font-size:16px;">
Por fim, há a especificação de todas as características dos eixos: títulos, ticks, orientação da escala, fonte, cor, tamanho e estilo. Também foi feita a mudança da cor do fundo. Tudo isso pensado com o intuito de minimizar a quantidade de informação desnecessária e facilitar a compreensão e leitura.
    
     
</p></br>
(PS: tem um easter egg para o senhor na próxima página.)

</br></br>

<b>Autora: Paula Eduarda de Lima.</b>

</body>
</html>




""")

