import boto3
import os

# Nome do bucket S3 trusted
bucket_name = 'f1-projeto-trusted'

# Pasta local com os arquivos tratados
trusted_folder = r'C:\Users\sabri\Desktop\dataengineer-aws-f1-project\data\trusted'

# Cliente S3 boto3
s3 = boto3.client('s3')

# Loop pelos arquivos CSV na pasta trusted
for filename in os.listdir(trusted_folder):
    if filename.endswith('.csv'):
        file_path = os.path.join(trusted_folder, filename)
        s3_key = f'trusted/{filename}'  # Mantém o prefixo 'trusted/' no S3

        try:
            s3.upload_file(file_path, bucket_name, s3_key)
            print(f'✔️ Arquivo {filename} enviado para s3://{bucket_name}/{s3_key}')
        except Exception as e:
            print(f'❌ Erro ao enviar {filename}: {e}')
