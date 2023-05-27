### LINGUAGEM: Python 3.10.4
### BIBLIOTECAS: itertools

### Descrição Exércicio 1:
**n** recebe um número do usuário, **i** recebe **'*'**, 
**lista** recebe **[ ]**.
Usa-se um for para fazer a multiplicação de **n** por **i**
a quantidade de vez igual a **n**, e a cada vez que o for roda
o resultado dessa multiplicação é adicionado como um novo 
elemento da lista.

### Descrição Exércicio 2:
**lista** recebe os numeros, depois ordena eles do maior para o menor, 
**lista_parcial** que vai receber o valor de suas diferenças positivas, 
**menor** recebe um valor alto para saber qual a menor diferença absoluta.
Uso dois for para ler os elementos da lista e tirar a diferença entre eles, 
aqueles, faz-se uma verificação se seu valor para atribui-lo a **menor**.
Usamos mais um for para ler os elementos de **lista_parcial** e achar aquele(s)
cuja difereça seja igual ao valor de **menor**.

### Descrição Exércicio 3:
**lista** recebe os numeros, **subconjuntos** vai ser quem recebe os subconjuntos
 de **lista**, fazemos um for que vai de 0 ate o tamanho de **lista** mais um, 
então **tupla_combinacoes** vai receber as combinações da lista com base no valor
do indice do for que tambem determina a quantidade de elementos a serem combinados, 
a combinação é feita pela função **combinations** que retona uma tupla que é convertida 
para lista pela função **map**, então depois seu valor e adicionado a **subconjuntos**