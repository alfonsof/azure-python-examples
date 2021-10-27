#!/usr/bin/python
# -*- coding: utf-8 -*-
# blobstoragecreate.py
# It is an example that handles Blob Storage containers on Microsoft Azure.
# Create a new Blob Storage container.
# You must provide 1 parameter:
# CONTAINER_NAME = Name of the container

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


def create_container(storage_account_conn_str, container_name):
    """
    Create a new Blob Storage container
    """
    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(storage_account_conn_str)

    try:
        print('Creating container ...')
        # Create the container
        container_client = blob_service_client.create_container(container_name)
        print('\nCreated')
    except Exception as e:
        print("\nError:")
        print(e)

    return


def main():

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if len(args) < 1:
        print('Not enough parameters.\n'\
              'Proper Usage is: python blobstoragecreate.py <CONTAINER_NAME>')
        sys.exit(1)

    container_name = args[0]
    print('Container name: ' + container_name)

    # Read storage account authentication information
    config_dict = load_cfg()
    cfg_storage_account_conn_str = config_dict['storageaccountconnectionstring']

    # Create a new Blob Storage container
    create_container(cfg_storage_account_conn_str, container_name)

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
