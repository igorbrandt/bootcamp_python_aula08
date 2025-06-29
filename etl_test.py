import pandas as pd

# criar o dataframe
file_path = 'dados.csv'
df = pd.read_csv(file_path, delimiter=',', encoding='utf-8')

# média de valor total
media = df['Valor_Total'].mean()

# numero de valores totais acima de 10.000
mais_de_10k = df[df['Valor_Total'] > 10000]

print(len(mais_de_10k))