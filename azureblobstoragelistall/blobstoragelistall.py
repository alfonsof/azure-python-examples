#!/usr/bin/python
# -*- coding: utf-8 -*-
# blobstoragelistall.py
# It is an example that handles Blob Storage containers on Microsoft Azure.
# List the blobs in all Blob Storage containers.

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

  # Read storage authentication information
  config_dict = loadcfg()
  cfg_account_name = config_dict['accountname']
  cfg_account_key = config_dict['accountkey']

  # Create the BlockBlockService that is used to call the Blob service for the storage account
  block_blob_service = BlockBlobService(account_name=cfg_account_name, account_key=cfg_account_key)

  try:
    # List the containers
    containers_list = block_blob_service.list_containers()
    for container in containers_list:
      # List the blobs in the container
      print('List of blobs in container "'+ container.name + '":')
      blobs_list = block_blob_service.list_blobs(container.name)
      for blob in blobs_list:
        props = blob.properties
        print('- Blob name: ' + blob.name)
        print('       size: ', props.content_length)
  except Exception as e:
    print("\nError:")
    print(e)

  return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
