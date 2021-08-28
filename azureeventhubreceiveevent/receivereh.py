#!/usr/bin/python
# -*- coding: utf-8 -*-
# receivereh.py
# It is an example that handles Event Hubs on Microsoft Azure.
# It handles an Event Hub and receives events from an event hub event stream.

import sys
import os
import configparser
import asyncio
from azure.eventhub.aio import EventHubConsumerClient
from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore


def loadcfg():
    """
    Read configuration information from a config file
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


async def on_event(partition_context, event):
    # Print the event data.
    print('Received an event: \"{}\"'.format(event.body_as_str(encoding='UTF-8')))
    print(f'  from the partition with ID: {partition_context.partition_id}')
    print(f'  EnqueuedTimeUtc: {event.enqueued_time}')
    print(f'  SequenceNumber: {event.sequence_number}')
    print(f'  Offset: {event.offset}')

    # Update the checkpoint so that the program doesn't read the events
    # that it has already read when you run it next time.
    await partition_context.update_checkpoint(event)


async def run(storage_account_connection_string, blob_name, event_hub_connection_string, event_hub_name):
    # Create an Azure blob checkpoint store to store the checkpoints.
    checkpoint_store = BlobCheckpointStore.from_connection_string(storage_account_connection_string,
                                                                    blob_name)

    # Create a consumer client for the event hub.
    client = EventHubConsumerClient.from_connection_string(event_hub_connection_string,
                                                             consumer_group="$Default",
                                                             eventhub_name=event_hub_name,
                                                             checkpoint_store=checkpoint_store)

    async with client:
        # Call the receive method. Read from the beginning of the partition (starting_position: "-1")
        await client.receive(on_event=on_event,  starting_position="-1")


def main():
    # Read configuration information
    config_dict = loadcfg()
    cfg_storage_account_connection_string = config_dict['storageaccountconnectionstring']
    cfg_blob_name = config_dict['blobname']
    cfg_event_hub_connection_string = config_dict['eventhubconnectionstring']
    cfg_event_hub_name = config_dict['eventhubname']

    print('Waiting for events')
    loop = asyncio.get_event_loop()
    # Run the main method.
    loop.run_until_complete(run(cfg_storage_account_connection_string, cfg_blob_name, cfg_event_hub_connection_string, cfg_event_hub_name))   


if __name__ == '__main__':
    main()
