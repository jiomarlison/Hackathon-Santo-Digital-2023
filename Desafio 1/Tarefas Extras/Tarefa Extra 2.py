import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
bicicletas = pd.read_csv('10_Bicicletas_Mais_Vendidas.csv', index_col=0)
sb.barplot(x='ProductName', y='Quantidade', data=bicicletas, width=0.5)
plt.show()
