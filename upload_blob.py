from azure.storage.blob import BlobServiceClient

connect_str = (
    "DefaultEndpointsProtocol=http;"
    "AccountName=devstoreaccount1;"
    "AccountKey=Eby8vdM02xNOcqFeqCnrC4xF+...";
    "BlobEnpoint=http://127.0.0.1:10000/devstoreaccount1;")
 
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

container_name = "datasets"

# Create container if it does not exist
try: blob_service_client.create_contaier(container_name)
except: pass

blob_client = blob_service_client.get_blob_client(
    container=container_name,
    blob="All_Diets.csv")

with open("All_Diets.csv", "rb") as data:
    blob_client.upload_blob(data, overwrite=True)


print("File upload successfully!")
