#!/usr/bin/python
# -*- coding: utf-8 -*-
# blobstoragedeleteobject.py
# It is an example that handles Blob Storage containers on Microsoft Azure.
# Delete a Blob in a Blob Storage container.
# You must provide 2 parameters:
# CONTAINER_NAME = Name of the container
# BLOB_NAME = Name of the blob

import sys
import os
import configparser
from azure.storage.blob import ContainerClient


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


def delete_blob(storage_account_conn_str, container_name, blob_name):
    """
    Delete a blob in a blob storage container in a storage account.
    """
    try:
        # Create the container object
        container_client = ContainerClient.from_connection_string(conn_str=storage_account_conn_str,
                                                                    container_name=container_name)
                                                                    
        # Delete the blob in the container
        print('Deleting blob ... ')
        container_client.delete_blob(blob_name)
        print('\nDeleted')
            
    except Exception as e:
        print("\nError:")
        print(e)

    return


def main():

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if len(args) < 2:
        print('Not enough parameters.\n'\
              'Proper Usage is: python blobstoragedeleteobject.py '\
              '<CONTAINER_NAME> <BLOB_NAME>')
        sys.exit(1)

    container_name = args[0]
    blob_name = args[1]
    print('Container name: ' + container_name)
    print('Blob name: ' + blob_name)

    # Read storage account authentication information
    config_dict = load_cfg()
    cfg_storage_account_conn_str = config_dict['storageaccountconnectionstring']

    # Delete a blob in a blob storage container in a storage account
    delete_blob(cfg_storage_account_conn_str, container_name, blob_name)

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
