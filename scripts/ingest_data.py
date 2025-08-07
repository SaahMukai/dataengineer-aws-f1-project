import boto3
import os

# Nome do bucket de destino
bucket_name = 'f1-projeto-raw'

# Caminho local da pasta com os arquivos CSV
local_folder = r'C:\Users\sabri\Desktop\dataengineer-aws-f1-project\data\raw'

# Cria cliente do S3
s3 = boto3.client('s3')

for filename in os.listdir(local_folder):
    if filename.endswith('.csv'):
        file_path = os.path.join(local_folder, filename)
        object_name = f'raw/{filename}'  # para manter a pasta raw no bucket

        try:
            s3.upload_file(file_path, bucket_name, object_name)
            print(f'✔️ Arquivo {filename} enviado para {bucket_name}/{object_name}')
        except Exception as e:
            print(f'❌ Erro ao enviar {filename}: {e}')
