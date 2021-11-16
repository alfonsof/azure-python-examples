#!/usr/bin/python
# -*- coding: utf-8 -*-
# blobstoragecopy.py
# It is an example that handles Blob Storage containers on Microsoft Azure.
# Copy a Blob from a Blob Storage container to another Blob Storage container.
# You must provide 3 parameters:
# SOURCE_CONTAINER      = Source container name
# SOURCE_BLOB           = Source blob name
# DESTINATION_CONTAINER = Destination container name

import sys
import os
import time
import configparser
from azure.storage.blob import BlobClient, BlobLeaseClient


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


def copy_blob(storage_account_conn_str, source_container_name, source_blob_name, dest_container_name):
    """
    Copy a blob in a blob storage container to another blob storage container in a storage account.
    """
    try:
        # Create the blob object representing the source
        source_blob_client = BlobClient.from_connection_string(conn_str=storage_account_conn_str,
                                                                    container_name=source_container_name,
                                                                    blob_name=source_blob_name)

        # Create the blob object representing the destination
        dest_blob_client = BlobClient.from_connection_string(conn_str=storage_account_conn_str,
                                                                    container_name=dest_container_name,
                                                                    blob_name=source_blob_name)

        print('Copying a Blob from a Blob container to another one ... ')
        
        # Lease the source blob for the copy operation
        # to prevent another client from modifying it.
        lease = BlobLeaseClient(source_blob_client)
        lease.acquire()

        # Get the source blob's properties and display the lease state.
        source_props = source_blob_client.get_blob_properties()
        print("Lease state: " + source_props.lease.state)

        # Start the copy operation.
        dest_blob_client.start_copy_from_url(source_blob_client.url)

        # Get the destination blob's properties to check the copy status.
        properties = dest_blob_client.get_blob_properties()
        copy_props = properties.copy

        # Display the copy status.
        print("Copy status: " + copy_props["status"])
        print("Copy progress: " + copy_props["progress"])
        print("Completion time: " + str(copy_props["completion_time"]))
        print("Total bytes: " + str(properties.size))
        
        if (source_props.lease.state == "leased"):
            # Break the lease on the source blob.
            lease.break_lease()

            # Update the destination blob's properties to check the lease state.
            source_props = source_blob_client.get_blob_properties()
            print("Lease state: " + source_props.lease.state)

        print('\nCopied')
            
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
              'Proper Usage is: python blobstoragecopy.py '\
              '<SOURCE_CONTAINER> <SOURCE_BLOB> <DESTINATION_CONTAINER>')
        sys.exit(1)

    source_container_name = args[0]
    print('Source container name: ' + source_container_name)
    source_blob_name = args[1]
    print('Source blob name: ' + source_blob_name)
    dest_container_name = args[2]
    print('Destination container name: ' + dest_container_name)
    dest_blob_name = source_blob_name

    # Read storage account authentication information
    config_dict = load_cfg()
    cfg_storage_account_conn_str = config_dict['storageaccountconnectionstring']

    # Copy a blob in a blob storage container to another blob storage container in a storage account
    copy_blob(cfg_storage_account_conn_str, source_container_name, source_blob_name, dest_container_name)

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
