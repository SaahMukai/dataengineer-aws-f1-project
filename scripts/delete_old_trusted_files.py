import boto3

# Nome do bucket
BUCKET_NAME = "f1-data-engineer-project"
PREFIX = "trusted/"

# Criar cliente S3
s3 = boto3.client("s3")

def delete_trusted_files():
    # Listar todos os objetos no prefix "trusted/"
    response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=PREFIX)

    if "Contents" not in response:
        print("Nenhum arquivo encontrado em 'trusted/'.")
        return

    # Criar lista para deletar
    objects_to_delete = [{"Key": obj["Key"]} for obj in response["Contents"]]

    # Deletar todos de uma vez
    s3.delete_objects(
        Bucket=BUCKET_NAME,
        Delete={"Objects": objects_to_delete}
    )

    print(f"{len(objects_to_delete)} arquivos deletados de s3://{BUCKET_NAME}/{PREFIX}")

if __name__ == "__main__":
    delete_trusted_files()
