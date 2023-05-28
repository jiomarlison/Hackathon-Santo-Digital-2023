import pandas as pd
import matplotlib

vendas2015 = pd.read_csv("AdventureWorks_Sales_2015.csv")
vendas2016 = pd.read_csv("AdventureWorks_Sales_2016.csv")
vendas2017 = pd.read_csv("AdventureWorks_Sales_2017.csv")
vendas_anos = pd.concat([vendas2015, vendas2016, vendas2017])

vendas_anos['OrderDate'] = pd.to_datetime(vendas_anos['OrderDate'])
# vendas_anos['Ano'] = vendas_anos['OrderDate'].dt.year
vendas_anos['Mes'] = vendas_anos['OrderDate'].dt.month
vendas_anos = pd.DataFrame(vendas_anos.loc[:, ['OrderQuantity', 'Mes']])
vendas_anos = vendas_anos.rename(columns={'OrderQuantity': 'Quantidade Vendido'})
vendas_anos = pd.DataFrame(vendas_anos.groupby(['Mes'], as_index=False).sum())

vendas_anos.to_excel('RelatorioVendasMensais.xlsx')

print(vendas_anos)