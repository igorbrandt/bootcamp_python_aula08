from etl import extract_data, calcular_valor_vendas, load_data

pasta = "data"

df = extract_data(pasta)
df_transformado = calcular_valor_vendas(df)
print(load_data(df_transformado, ["parquet", "csv"]))
