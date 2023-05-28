import pandas as pd
categorias = pd.read_csv("AdventureWorks_Product_Categories.csv")
sub_categorias = pd.read_csv("AdventureWorks_Product_Subcategories.csv")
produtos = pd.read_csv("AdventureWorks_Products.csv")
vendas2015 = pd.read_csv("AdventureWorks_Sales_2015.csv")
vendas2016 = pd.read_csv("AdventureWorks_Sales_2016.csv")
vendas2017 = pd.read_csv("AdventureWorks_Sales_2017.csv")
vendastotais = pd.concat([vendas2015, vendas2016, vendas2017])
territorios = pd.read_csv('AdventureWorks_Territories.csv')

#melhores vendas por produto
vendas_totais_por_produto = vendastotais.groupby(['ProductKey'], as_index=False).sum().sort_values(by='OrderQuantity', ascending=False)

#10 BICICLETAS MAIS VENDIDAS
categoria_bikes = categorias.loc[categorias['CategoryName'] == 'Bikes']
subcategoria_bikes = pd.merge(categoria_bikes, sub_categorias, how='inner')
produtos_bikes = pd.merge(subcategoria_bikes, produtos, how='inner')
top_bikes = pd.merge(vendas_totais_por_produto, produtos_bikes, how='inner')
top_bikes = top_bikes.rename(columns={'OrderQuantity': 'Quantidade'}).head(10)
top_bikes = top_bikes.loc[:, ['ProductKey', 'ProductName', 'Quantidade']]
top_bikes = top_bikes.set_index('ProductKey')
top_bikes.to_csv('10_Bicicletas_Mais_Vendidas.csv')

# CLIENTE COM MAIS PEDIDOS
pedidos_totais_clientes = vendastotais.groupby(['CustomerKey'], as_index=True).count()
pedidos_totais_clientes = pedidos_totais_clientes.sort_values(by='OrderQuantity', ascending=False).head(1)
pedidos_totais_clientes = pedidos_totais_clientes.loc[:, ['OrderQuantity']]
pedidos_totais_clientes.to_csv('Cliente_com_mais_pedidos.csv')

# TOTAL VENDA POR MÊS
total_vendas_meses = produtos
total_vendas_meses['Lucro'] = total_vendas_meses['ProductPrice'] - total_vendas_meses['ProductCost']
total_vendas_meses = pd.merge(total_vendas_meses, vendastotais, how='inner')
total_vendas_meses['OrderDate'] = pd.to_datetime(total_vendas_meses['OrderDate'])
total_vendas_meses['Mes'] = total_vendas_meses['OrderDate'].dt.month
total_vendas_meses['Total'] = total_vendas_meses['OrderQuantity'] * total_vendas_meses['Lucro']
total_vendas_territorio = total_vendas_meses
total_vendas_meses = pd.DataFrame(total_vendas_meses.loc[:, ['Mes', 'Total']]).sort_values(by=['Mes'])
total_vendas_meses = total_vendas_meses.groupby(['Mes']).sum()
total_vendas_meses.to_csv('Total_Vendas_Meses.csv')

#VENDAS POR REGIÃO
territorios = pd.DataFrame(territorios.loc[:, ['SalesTerritoryKey', 'Region']])
total_vendas_territorio = pd.DataFrame(total_vendas_territorio.loc[:, ['TerritoryKey','Total']]).sort_values(by=['TerritoryKey'])
total_vendas_territorio = pd.DataFrame(total_vendas_territorio.groupby(['TerritoryKey']).sum())
territorios = territorios.merge(total_vendas_territorio, left_on='SalesTerritoryKey', right_on='TerritoryKey')
territorios = territorios.drop(columns=['SalesTerritoryKey']).set_index('Region')
territorios.to_csv("Vendas_Por_Região.csv")