import pandas as pd
def bikes():
    categorias = pd.read_csv("AdventureWorks_Product_Categories.csv")
    sub_categorias = pd.read_csv("AdventureWorks_Product_Subcategories.csv")
    produtos = pd.read_csv("AdventureWorks_Products.csv")

    bikes = categorias.loc[categorias['CategoryName']=='Bikes']
    print('Subcategoias Bicicletas\n', sub_categorias.loc[sub_categorias['ProductCategoryKey']==1])
    df_cat_subcat = pd.merge(bikes, sub_categorias, how='inner')
    print(df_cat_subcat)
    df_cat_subcat_prod = pd.merge(df_cat_subcat, produtos, how='inner')
    print(df_cat_subcat_prod[['CategoryName', 'ProductCategoryKey', 'ProductSubcategoryKey','ProductSKU','ProductName','ModelName']].head(10))
    # df_cat_subcat_prod.to_csv("bicicletas", sep=',', index=False)
    # df_cat_subcat_prod.to_excel("bicicletas.xlsx", index=False)

def vendas():
    vendas2015 = pd.read_csv("AdventureWorks_Sales_2015.csv")
    # print(vendas2015.head(10))
    vendas2016 = pd.read_csv("AdventureWorks_Sales_2016.csv")
    # print(vendas2016.head(10))
    vendas2017 = pd.read_csv("AdventureWorks_Sales_2017.csv")
    # print(vendas2017.head(10))
    vendas151617 = pd.concat([vendas2015,vendas2016,vendas2017], keys=[2015,2016,2017])
    print(vendas151617)

vendas()