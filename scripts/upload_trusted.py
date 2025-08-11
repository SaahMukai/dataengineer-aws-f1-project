import boto3
import os

BUCKET_NAME = "f1-data-engineer-project"
TRUSTED_FOLDER = r'C:\Users\sabri\Desktop\dataengineer-aws-f1-project\data\trusted'

s3 = boto3.client("s3")

def upload_trusted():
    for filename in os.listdir(TRUSTED_FOLDER):
        local_path = os.path.join(TRUSTED_FOLDER, filename)
        if os.path.isfile(local_path):
            new_filename = f"trusted_{filename}"
            s3_path = f"trusted/{new_filename}"
            s3.upload_file(local_path, BUCKET_NAME, s3_path)
            print(f"{filename} enviado para s3://{BUCKET_NAME}/{s3_path}")

if __name__ == "__main__":
    print("Iniciando upload da pasta TRUSTED...")
    upload_trusted()
    print("Upload TRUSTED concluído!")

