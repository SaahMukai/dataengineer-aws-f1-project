import boto3
import os

# Nome do bucket e pasta local
BUCKET_NAME = "f1-data-engineer-project"
TRUSTED_FOLDER = r"C:\Users\sabri\Desktop\dataengineer-aws-f1-project\data\trusted"

# Cliente S3
s3 = boto3.client("s3")

def upload_trusted():
    for filename in os.listdir(TRUSTED_FOLDER):
        if filename.endswith(".csv"):
            local_path = os.path.join(TRUSTED_FOLDER, filename)

            # pega o nome do arquivo sem extensão pra virar nome da pasta (circuits.csv = circuits)
            folder_name = os.path.splitext(filename)[0].lower()  

            # monta o caminho no S3 → trusted/circuits/circuits.csv
            s3_path = f"trusted/{folder_name}/{filename}"

            s3.upload_file(local_path, BUCKET_NAME, s3_path)
            print(f"{filename} enviado para s3://{BUCKET_NAME}/{s3_path}")

if __name__ == "__main__":
    upload_trusted()
    print("Upload concluído!")
