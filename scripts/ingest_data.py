import os
import pandas as pd

def transform(df):
    df.drop_duplicates(inplace=True)
    df.dropna(how="all", inplace=True)
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")
    return df

raw_folder = os.path.join("data", "raw")
trusted_folder = os.path.join("data", "trusted")
os.makedirs(trusted_folder, exist_ok=True)

for filename in os.listdir(raw_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(raw_folder, filename)
        df = pd.read_csv(file_path)
        df = transform(df)
        trusted_path = os.path.join(trusted_folder, filename)
        df.to_csv(trusted_path, index=False)
        print(f"Arquivo processado e salvo em: {trusted_path}")

print("Transformação concluída e arquivos salvos na pasta 'trusted'.")

