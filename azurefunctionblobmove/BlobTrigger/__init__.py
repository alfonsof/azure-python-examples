import logging
import os

import azure.functions as func
from azure.storage.blob import BlobServiceClient


def main(inputblob: func.InputStream, outputblob: func.Out[bytes]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Blob Name: {inputblob.name}\n"
                 f"Blob Size: {inputblob.length} bytes\n"
                 f"Blob URI: {inputblob.uri}")
    readbytes = inputblob.read()
    logging.info(f'Trigger function processed {len(readbytes)} bytes')
    
    # Copy blob to output
    outputblob.set(readbytes)
    
    # Delete blob from input
    blob_url = inputblob.uri
    container_name = blob_url.split("/")[-2].split("?")[0]
    blob_name = blob_url.split("/")[-1].split("?")[0]
    logging.info(f'Container name: {container_name}')
    logging.info(f'Blob name: {blob_name}')
    blob_service_client = BlobServiceClient.from_connection_string(os.environ['MY_STORAGE_IN'])
    blob_to_delete = blob_service_client.get_blob_client(container=container_name,blob=blob_name)   
    blob_to_delete.delete_blob()
    logging.info(f"Moved")
