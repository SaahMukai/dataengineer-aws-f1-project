import os
import pandas as pd

# Caminhos das pastas
raw_folder = os.path.join("data", "raw")
trusted_folder = os.path.join("data", "trusted")

# Criar pasta trusted se não existir
os.makedirs(trusted_folder, exist_ok=True)

# Loop por todos os arquivos CSV no raw
for filename in os.listdir(raw_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(raw_folder, filename)

        # Ler o CSV
        df = pd.read_csv(file_path)

        # ===== TRATAMENTOS BÁSICOS =====
        # Remove linhas duplicadas
        df.drop_duplicates(inplace=True)

        # Remove linhas totalmente vazias
        df.dropna(how="all", inplace=True)

        # Tenta converter colunas numéricas que estão como texto
        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="ignore")

        # Salvar no trusted
        trusted_path = os.path.join(trusted_folder, filename)
        df.to_csv(trusted_path, index=False)

        print(f"Arquivo processado e salvo em: {trusted_path}")

print("✅ Transformação concluída e arquivos salvos na pasta 'trusted'.")
