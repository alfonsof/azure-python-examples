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
from azure.storage.blob import BlockBlobService, PublicAccess


def loadcfg():
    """
    Read storage authentication information from a config file
    and return the values in a dictionary.
    """
    config_file = 'app.cfg'
    if os.path.exists(config_file):
        config = configparser.RawConfigParser()
        config.read(config_file)
    else:
        print('Config file "' + config_file + '" does not exist')
        sys.exit(1)

    return dict(config.items('StorageAuthentication'))


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

    # Read storage authentication information
    config_dict = loadcfg()
    cfg_account_name = config_dict['accountname']
    cfg_account_key = config_dict['accountkey']

    # Create the BlockBlockService that is used to call the Blob service for the storage account
    block_blob_service = BlockBlobService(account_name=cfg_account_name, account_key=cfg_account_key)

    try:
        if block_blob_service.exists(container_name):
            if block_blob_service.exists(container_name, blob_name):
                print('Deleting blob ...')
                # Delete the blob
                block_blob_service.delete_blob(container_name, blob_name)
                print('\nDeleted')
            else:
                print('\nError: Blob "' + blob_name + '" does NOT exist.')
        else:
            print('\nError: Blob Storage container "' + container_name + '" does NOT exist.')
    except Exception as e:
        print("\nError:")
        print(e)

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
