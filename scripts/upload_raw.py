import boto3
import os

BUCKET_NAME = "f1-data-engineer-project"
RAW_FOLDER = r'C:\Users\sabri\Desktop\dataengineer-aws-f1-project\data\raw'

s3 = boto3.client("s3")

def upload_raw():
    for filename in os.listdir(RAW_FOLDER):
        local_path = os.path.join(RAW_FOLDER, filename)
        if os.path.isfile(local_path):
            s3_path = f"raw/{filename}"
            s3.upload_file(local_path, BUCKET_NAME, s3_path)
            print(f"{filename} enviado para s3://{BUCKET_NAME}/{s3_path}")

if __name__ == "__main__":
    print("Iniciando upload da pasta RAW...")
    upload_raw()
    print("Upload RAW concluído!")