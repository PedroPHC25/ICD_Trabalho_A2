# ICD_Trabalho_A2

Trabalho referente à avaliação 2 do curso de Introdução à Ciência de Dados.

Integrantes do grupo:
- **Maria Eduarda Mesquita Magalhães**
    - Código: 231708018
    - Email: B51085@fgv.edu.br
- **Mariana Fernandes Rocha**
    - Código: 231708025
    - Email: mariana.rocha@fgv.edu.br
- **Paula Eduarda de Lima**
    - Código: 231708024
    - Email: B51097@fgv.edu.br
- **Pedro Henrique Coterli**
    - Código: 231708009
    - Email: B51063@fgv.edu.br


Os arquivos estão organizados da seguinte forma:
- Na pasta principal do repositório, estão apenas a base de dados em formato csv, os arquivos .py `main` e `cds_generator` (leitor do csv e gerador dos ColumnDataSources) e a página principal do site `index.html`.
- Os códigos geradores dos gráficos e dos textos estão divididos entre as pastas `graphics`, sendo cada pasta referente a um tipo de energia explorada. Cada pasta contém de 4 a 5 arquivos: um é o gerador das variáveis de texto para o HTML e os demais são os códigos das visualizações, com cada um armazenando o código de uma visualização.
- Dentro da pasta `html_pages`, estão os arquivos HTML oficiais, que são referenciados na página principal do site do repositório.
- Na pasta `images`, estão imagens utilizadas na criação do HTML principal.
- E na pasta `drafts`, estão apenas rascunhos que fizemos durante todo o processo de elaboração do trabalho.

Observação: Se for desejado executar o arquivo `main.py`, é necessário antes instalar a biblioteca `scipy` por meio do comando `pip install scipy`, pois ela foi utilizada em uma das visualizações.
