# pip install azure-storage-blob
# pip install azure-storage-blob --upgrade

import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Configure storage connection string to system
# setx AZURE_STORAGE_CONNECTION_STRING "DefaultEndpointsProtocol=https;AccountName=youtubestatsblobstorage;AccountKey=JVDn6zYcUxIFr+I33s06PZKyyS4e2WeiYib7bk2So5PrpwdoP7R+RQUeBmX6jwCDmcq/rf35SexvaC69mk8dXQ==;EndpointSuffix=core.windows.net"

# Retrieve the connection string for use with the application.
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

try:
    print("Azure Blob storage v12 - Python quickstart sample")
    
    # Quick start code goes here
        # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    # Create a unique name for the container
    container_name = "msftvisualstudiochnl" + str(uuid.uuid4())
    # Create the container
    container_client = blob_service_client.create_container(container_name)
    # Create a file in local data directory to upload and download
    local_path = "./data"
    local_file_name = "microsoft_visual_studio.json"
    upload_file_path = os.path.join(local_path, local_file_name)
    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)
    # Upload the created file
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)

except Exception as ex:
    print('Exception:')
    print(ex)

