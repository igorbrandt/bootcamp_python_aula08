import pandas as pd
import glob as g
import os

### função de extract que lê e consolida os 3 arquivos .json
def extract_data(folder: str) -> pd.DataFrame:
    
    # encontrar paths de cada um dos arquivos .json
    json_files = g.glob(os.path.join(folder, "*.json"))

    # ler cada um dos arquivos
    df_list = [pd.read_json(file) for file in json_files]

    # criar uma lista com cada um deles
    total_df = pd.concat(df_list, ignore_index=True)

    return total_df

# função que transforma

# função que carrega em csv ou parquet