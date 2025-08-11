import os

# Caminho local da pasta trusted
trusted_folder = r"C:\Users\sabri\Desktop\dataengineer-aws-f1-project\data\trusted"

# Renomeia arquivos para trusted_nome.csv
for filename in os.listdir(trusted_folder):
    if filename.endswith(".csv") and not filename.startswith("trusted_"):
        old_path = os.path.join(trusted_folder, filename)
        new_filename = f"trusted_{filename}"
        new_path = os.path.join(trusted_folder, new_filename)
        os.rename(old_path, new_path)
        print(f"Renomeado: {filename} → {new_filename}")

print("Renomeação concluída!")
