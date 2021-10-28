#!/usr/bin/python
# -*- coding: utf-8 -*-
# blobstorageupload.py
# It is an example that handles Blob Storage containers on Microsoft Azure.
# Upload a local file to a Blob Storage container in an Azure storage account.
# You must provide 3 parameters:
# CONTAINER_NAME   = Name of the container
# BLOB_NAME        = Blob name in the container
# LOCAL_FILE_NAME  = Local file name
 
import sys
import os
import configparser
from azure.storage.blob import BlobServiceClient


def load_cfg():
    """
    Read storage account authentication information from a config file
    and return the values in a dictionary.
    """
    config_file = 'app.cfg'
    if os.path.exists(config_file):
        config = configparser.RawConfigParser()
        config.read(config_file)
    else:
        print('Config file "' + config_file + '" does not exist')
        sys.exit(1)

    return dict(config.items('Configuration'))


def upload_blob(storage_account_conn_str, container_name, blob_name, local_file_name):
    """
    Upload a Blob to a blob storage container.
    """
    try:
        # Create the BlobServiceClient object which will be used to create a blob client
        blob_service_client = BlobServiceClient.from_connection_string(storage_account_conn_str)

        # Create a blob client using the blob name
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        if os.path.exists(local_file_name):
            # Upload the local file to the Blob container
            print('Uploading the local file to the Blob Storage container ...')
            with open(local_file_name, "rb") as data:
                blob_client.upload_blob(data)
            print("\nUploaded")
        else:
            print('\nError: Local file "' + local_file_name + '" does NOT exist.')

    except Exception as e:
        print("\nError:")
        print(e)

    return


def main():

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if len(args) < 3:
        print('Not enough parameters.\n'\
              'Proper Usage is: python blobstorageupload.py '\
              '<CONTAINER_NAME> <BLOB_NAME> <LOCAL_FILE_NAME>')
        sys.exit(1)

    container_name = args[0]
    print('Container:  ' + container_name)
    blob_name = args[1]
    print('Blob:       ' + blob_name)
    local_file_name = args[2]
    print('Local file: ' + local_file_name)

    # Read storage account authentication information
    config_dict = load_cfg()
    cfg_storage_account_conn_str = config_dict['storageaccountconnectionstring']

    # Upload a Blob to a blob storage container
    upload_blob(cfg_storage_account_conn_str, container_name, blob_name, local_file_name)

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
