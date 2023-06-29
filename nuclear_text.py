from bokeh.models import Div

# Este módulo contém as partes do texto em HTML da página dos gráficos sobre energia nuclear.

nuclear_text_1 = Div(text = """<html>

<head>
<title>Visualizações sobre energia nuclear</title>

<h1>Visualização sobre consumo de energia nuclear e o PIB de cada país. </h1>

""")

nuclear_text_2 = Div(text = """
</br><p>
O objetivo dessa visualização é exibir a correlação entre a participação da energia nuclear no consumo de 
cada país com o seu PIB, de maneira à observar se há alguma interdependencia entre as duas variáveis. 
Tendo isso em mente, o tipo de gráfico mais adequado para esse tipo de visualização seria o gráfico de dispersão, 
que plota uma bolha para cada país presente no dado.
</p></br>

</br><p>
Para iniciar a produção do gráfico, foram selecionados os dados do ano pretendido, além de se criar uma nova 
coluna de dado chamada "gdp_in_bi" que divide a coluna original por 1000000000. De maneira a facilitar o processo, 
foi criado um dicionário que corresponde x, y e z, com as colunas 'gdp_in_bi', 'nuclear_share_energy' e 'country'.
</p></br>

</br><p>
Após isso, gerei o scatterplot, definindo o tamanho e as ferramentas que presentes, o qual o PIB representa o 
eixo x e a energia nuclear representa o eixo y e também o tamanho da bolha, de maneira a dar mais enfâse na 
observação dessa variável. A cor das bolhas foi escolhida para ser uma cor escura que destacase, mas ainda neutra, 
como esse tom de azul, com o intuito de não gerar excesso de informação visual, além de trazer transparência para 
ajudar na representação dos países próximos.
</p></br>

</br><p>
Um destaque para a ferramenta "tooltips" que apresenta uma etiqueta de breve descrição de cada bolha, quando o 
mouse está posicionado nela. 
</br><p>

</br><p>
Em seguida foram definidas todas as características do título do gráfico e eixos, como cor, tamanho, fonte, 
alinhamento, orientação e estilo, sempre pensando na harmonia do conjunto formado. Outra mudança realizada foi 
a forma do eixos, alterando atributos como o tamanho do tick, retirando o tick menores, a orientação e o formato 
da escala, detalhes que fazem a diferença e ajudam a simplificar as informações transmitidas.
</p></br>

</br><p>
Outra adição foi uma anotação de texto que destaca a França como país em a energia nuclear teve a maior participação 
em 2000, de modo a chamar a atenção do leitor por ser uma informação importante.
</p></br>

</br><p>
Por fim, modifiquei a cor de fundo do gráfico, tirando o branco vibrante que pode trazer cansaço no visualização e 
opitando por um tom de cinza claro que harmoniza com o restante e ao mesmo tempo na tira o foco dos outros elementos
 de destaque. 
</p></br>

<h2>Grid dos 6 países que mais produzem energia nuclear(1985-2020)</h2>""")
