### LINGUAGEM: Python 3.10.4
### BIBLIOTECAS: pandas, matplotlib, seaborn
### IDES: Pycharm

### **PEQUENA DESCRIÇÃO DA REALIZAÇÃO DAS TARFEAS**

#### DESCRIÇÃO DAS 3 PRIMEIRAS PERGUNTAS DA TAREFA 2
● Quais são os 10 produtos mais vendidos (em quantidade) na  categoria "Bicicletas"?

● Qual é o cliente que tem o maior número de pedidos realizados?

● Em qual mês do ano ocorrem mais vendas (em valor total)?

Criei variaveis que recebem os valores dos arquivos CSV relacionados a eles,
que são lido pelo metodo de leitura de CSV do pandas, 
então eu as utilizo junto aos metodos do pandas para filtrar os conteudos das tabelas, 
então vou mesclando-as de forma parecida ao INNER JOIN do SQL, pela funçaõ merge da biblioteca,
então após obter o resultado desejado ultilizo mais uma vez o pandas para criar o arquivo CSV final.

#### DESCRIÇÃO DA ULTIMA PERGUNTA DA TAREFA 2
● Quais vendedores tiveram vendas com valor acima da média no último ano fiscal?

Não é possivel adquirir tais informações já  que os dados necessarios para tal analisa estão ausentes, 
porem é possivel medir o valor de venda por região, o que permitiria ter um vislumbre do valor total da região e 
caso fosse possivel conseguir a quantidade de loja de tal região então conseguiriamos ter uma média de valor por loja. 