import pandas as pd
import glob
import os

### função de extract que lê e consolida os 3 arquivos .json
def extract_data(folder: str) -> pd.DataFrame:

    # encontrar paths de cada um dos arquivos .json
    json_files = glob.glob(os.path.join(folder, "*.json"))

    # ler cada um dos arquivos
    df_list = [pd.read_json(file) for file in json_files]

    # criar uma lista com cada um deles
    total_df = pd.concat(df_list, ignore_index=True)

    return total_df

# função que transforma
def calcular_valor_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Valor_Total"] = df["Quantidade"] * df["Venda"]
    return df

# função que carrega em csv ou parquet. função recebe dois parâmetros: o DF e o formato (csv, parquet, ou ambos)
def load_data(df: pd.DataFrame, output_format: list):
    for format in output_format:
        if format == "csv":
            df.to_csv("dados.csv", index=False)
        if format == "parquet":
            df.to_parquet("dados.parquet", index=False)


if __name__ == "__main__":
    folder = "data"
    print(extract_data(folder))