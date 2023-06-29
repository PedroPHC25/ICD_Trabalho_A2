from bokeh.models import Div

# Módulo com os textos presentes no arquivo sobre energia a partir do carvão

title = Div(text = """<html>
    <head>
        <title>Análise das atividades energéticas a partir do carvão</title>
    </head>
    <body>
     <center><h1>Análise das atividades energéticas a partir do carvão</h1></center>
    """)
            
first_graph = Div(text =""" <center><h2>Comparação entre continentes da produção de energia a partir do carvão</h2></center>""")

text_grid_graph = Div(text ="""<p>O objetivo desse gráfico é criar uma comparação na evolução dos anos entre os continentes e seu consumo de energia primária a partir do carvão, os continentes escolhidos foram: América do Norte, Europa, América do Sul e Central e África.
        Os dados estão representados com um gráfico de linha pois se trata de uma mudança ao longo do tempo, o que segundo Edward Tufte é a representação mais adequada.</p>
    
    <p>Para esse gráfico tive de escolher os continentes com os melhores dados, e mesmo assim a base de dados tem um desfalque entre 1965 a 1980, tentei buscar fontes complementares mas não obtive sucesso.</p>
        
    <p>Com a base de dados original tive que filtrar apenas os países que desejava e para cada um o seu respectivo gráfico de linha, após todos confeccionados foram arranjados em um grid 2x2.</p>
    <p>Os continentes estão representados com cores diferentes e além do título também está visível uma legenda. Nesse gráfico a interatividade está presente nas linhas através da ferramenta "hover", que detalha o dado pressionado.</p>

    <p>Os continentes da direita apresentam um aumento constante e sútil na produção dos últimos anos, com suas economias emergentes e em desenvolvimento aumentar o uso de carvão é uma maneira de ajudar a impulsionar seu crescimento econômico, mesmo quando adicionam mais fontes renováveis. Já à esquerda, a Europa e América do Norte diminuem suas produções em diferentes ritmos, a demanda por carvão cai nas economias avançadas à medida que as energias renováveis o substituem cada vez mais pela geração de eletricidade.</p>
    """)

title_stackedbar = Div(text ="""   <center><h2>Atividades do carvão</h2></center>""")

text_stackedbar = Div(text ="""<p>Essa visualização trás um acumulativo das atividades do carvão em alguns países no ano de 1995, entre os aspectos estão consumo, produção de carvão e geração de eletricidade. O tipo de mensagem desse gráfico é a comparação nominal, por isso foi escolhido a representação em barras que permite maior precisão na interpretação.</p>
    
<p>Para a escolha dos países busquei aqueles que tinham as 3 categorias com dados disponíveis e relevantes, a partir disso manipulei a base de dados para ter apenas esses certos países, em seguida escolhi as cores para representar as camadas das barras.</p>
<p>Para montar o gráfico decidi deixar as barras na horizontal, o eixo vertical tem os países e o eixo horizontal o acumulativo das variáveis. Nessa visualização a interatividade está presente na legenda, ao ser pressionada oculta a camada desejada, e com "hover", que mostra a categoria da barra e o montante no respectivo país.</p>
    
<p>Analisando o gráfico vemos uma alta participação da China em todos aspectos. Entre 1970 e 1990, o consumo de energia aumentou 208% na China, em comparação com um aumento médio de 28% nos países desenvolvidos durante o mesmo período.Mesmo que a China tenha melhorado a eficiência de todas as suas usinas elétricas, grande parte do carvão queimado na China é consumido em pequenas caldeiras industriais e municipais e em milhões de fogões e aquecedores domésticos, para os quais não há combustíveis alternativos atualmente disponíveis.</p>
""")

title_rank = Div(text ="""<center><h2>Maiores consumidores de energia primária a partir do carvão (1965-2019)</h2></center>""")

text_rank = Div(text ="""<p>Nesse gráfico foi usado o Bokeh Server para permitr a interatividade do gráfico entre os anos disponíveis. A mensagem dessa visualização é um rank, assim as barras verticais foram escolhidas para representar os montantes de consumo.</p>

<p>Para esse gráfico precisei filtrar os maiores consumidores em um ano e depois foi definida uma função que atualiza o ano exibido no gráfico de acordo com o "slider". Além do slider, também está disponível o "hover" que detalha o dado da barra respectiva.</p>

<p>Novamente ocorre uma dominância da China nesse setor, especificamente a partir de 1986. Isso deve-se em parte à mudança do gás para o carvão motivada pelos preços altíssimos do gás. Outro fator determinante é a queda na qualidade do carvão extraído, o que significa que usinas e fábricas tiveram que queimar mais carvão para obter a mesma quantidade de energia.</p>
</body>

</html>""")