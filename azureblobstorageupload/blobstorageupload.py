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
              'Proper Usage is: python blobstorageupload.py '\
              '<CONTAINER_NAME> <BLOB_NAME> <LOCAL_FILE_NAME>')
        sys.exit(1)

    container_name = args[0]
    print('Container:  ' + container_name)
    blob_name = args[1]
    print('Blob:       ' + blob_name)
    local_file_name = args[2]
    print('Local file: ' + local_file_name)

    # Read storage authentication information
    config_dict = loadcfg()
    cfg_account_name = config_dict['accountname']
    cfg_account_key = config_dict['accountkey']

    # Create the BlockBlockService that is used to call the Blob service for the storage account
    block_blob_service = BlockBlobService(account_name=cfg_account_name, account_key=cfg_account_key)

    try:
        if block_blob_service.exists(container_name):
            if os.path.exists(local_file_name):
                # Upload the local file to the Blob container
                print('Uploading a local file to a Blob Storage container ...')
                block_blob_service.create_blob_from_path(container_name, blob_name, local_file_name)
                print("\nUploaded")
            else:
                print('\nError: Local file "' + local_file_name + '" does NOT exist.')
        else:
            print('\nError: Blob Storage container "' + container_name + '" does NOT exist.')
    except Exception as e:
        print("\nError:")
        print(e)

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
