import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

vendas_anos = pd.read_csv('Total_Vendas_Meses.csv', index_col=0)

sb.lineplot(x='Mes', y='Total', data=vendas_anos, color='r', markers='*')
plt.show()
