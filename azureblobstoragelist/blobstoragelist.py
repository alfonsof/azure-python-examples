#!/usr/bin/python
# -*- coding: utf-8 -*-
# blobstoragelist.py
# It is an example that handles Blob Storage containers on Microsoft Azure.
# List information about the blobs in a Blob Storage container in an Azure storage account.
# You must provide 1 parameter:
# CONTAINER_NAME = Name of the container

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


def list_container_blobs(storage_account_conn_str, container_name):
    """
    List the blobs in a container in a storage account.
    """
    try:
        # Create the container object
        container_client = ContainerClient.from_connection_string(conn_str=storage_account_conn_str,
                                                                    container_name=container_name)
        # List the blobs in the container
        print('List of blobs in Blob Storage container "'+ container_name + '":')
        blob_list = container_client.list_blobs()
        for blob in blob_list:
            print('- Blob name: ' + blob.name)
            print('       size: ', blob.size)
            
    except Exception as e:
        print("\nError:")
        print(e)


def main():

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if len(args) < 1:
        print('Not enough parameters.\n'\
              'Proper Usage is: python blobstoragelist.py <CONTAINER_NAME>')
        sys.exit(1)

    container_name = args[0]

    # Read storage account authentication information
    config_dict = load_cfg()
    cfg_storage_account_conn_str = config_dict['storageaccountconnectionstring']

    # List the blobs in the container
    list_container_blobs(cfg_storage_account_conn_str, container_name)

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
