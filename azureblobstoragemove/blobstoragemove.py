#!/usr/bin/python
# -*- coding: utf-8 -*-
# blobstoragemove.py
# It is an example that handles Blob Storage containers on Microsoft Azure.
# Copy a blob from a Blob Storage container to another Blob Storage container.
# You must provide 3 parameters:
# SOURCE_CONTAINER      = Source container name
# SOURCE_BLOB           = Source blob name
# DESTINATION_CONTAINER = Destination container name

import sys
import os
import time
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
    if len(args) < 3:
        print('Not enough parameters.\n'\
              'Proper Usage is: python blobstoragemove.py '\
              '<SOURCE_CONTAINER> <SOURCE_BLOB> <DESTINATION_CONTAINER>')
        sys.exit(1)

    source_container_name = args[0]
    print('Source container name: ' + source_container_name)
    source_blob_name = args[1]
    print('Source blob name: ' + source_blob_name)
    dest_container_name = args[2]
    print('Destination container name: ' + dest_container_name)
    dest_blob_name = source_blob_name

    # Read storage authentication information
    config_dict = loadcfg()
    cfg_account_name = config_dict['accountname']
    cfg_account_key = config_dict['accountkey']

    # Create the BlockBlockService that is used to call the Blob service for the storage account
    block_blob_service = BlockBlobService(account_name=cfg_account_name, account_key=cfg_account_key)

    try:
        if block_blob_service.exists(source_container_name):
            if block_blob_service.exists(source_container_name, source_blob_name):
                if block_blob_service.exists(dest_container_name):
                    print('Moving a Blob from a Blob Storage container to another one ...')
                    # Get blob url: https://storageaccountname.blob.core.windows.net/containername/blobname
                    source_blob_url = block_blob_service.make_blob_url(source_container_name, source_blob_name)
                    # Copy Blob
                    copy = block_blob_service.copy_blob(dest_container_name, dest_blob_name, source_blob_url)
                    # Poll for copy completion
                    while copy.status != 'success':
                        time.sleep(30)
                        copy = block_blob_service.get_blob_properties(dest_container_name, dest_blob_name).properties.copy
                    # Delete Blob in the source container
                    block_blob_service.delete_blob(source_container_name, source_blob_name)
                    print('\nMoved')
                else:
                    print('\nError: Destination Blob Storage container "' + source_container_name + '" does NOT exist.')
            else:
                print('\nError: Blob "' + source_blob_name + '" does NOT exist.')
        else:
            print('\nError: Source Blob Storage container "' + source_container_name + '" does NOT exist.')
    except Exception as e:
        print("\nError:")
        print(e)

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
