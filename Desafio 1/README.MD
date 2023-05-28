### LINGUAGEM: Python 3.10.4
### BIBLIOTECAS: pandas

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
● Quais vendedores tiveram vendas com valor acima da média no
último ano fiscal?