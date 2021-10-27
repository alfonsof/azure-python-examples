#!/usr/bin/python
# -*- coding: utf-8 -*-
# blobstoragelistall.py
# It is an example that handles Blob Storage containers on Microsoft Azure.
# List information about all Blob Storage containers and the blobs they contain in an Azure storage account.

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


def list_containers(storage_account_conn_str):
    """
    List the containers and the blobs they contain in a storage account
    """
    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(storage_account_conn_str)

    try:
        print('Listing Blob Storage containers ...')
        # List the containers
        container_list = blob_service_client.list_containers()
        for container in container_list:
            # Get the container object
            container_client = blob_service_client.get_container_client(container)
            # List the blobs in the container
            print('* Blob container "' + container.name + '", list of blobs:')
            blob_list = container_client.list_blobs()
            for blob in blob_list:
                print('  - Blob name: ' + blob.name)
                print('         size: ', blob.size)

    except Exception as e:
        print("\nError:")
        print(e)

    return


def main():

    # Read storage account authentication information
    config_dict = load_cfg()
    cfg_storage_account_conn_str = config_dict['storageaccountconnectionstring']

    # List the containers in the storage account
    list_containers(cfg_storage_account_conn_str)

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
