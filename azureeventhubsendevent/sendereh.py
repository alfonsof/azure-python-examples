#!/usr/bin/python
# -*- coding: utf-8 -*-
# sendereh.py
# It is an example that handles Event Hubs on Microsoft Azure.
# It handles an Event Hub and sends events to an event hub event stream.

import sys
import os
import configparser
import asyncio
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData


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


async def run(event_hub_connection_string, event_hub_name):
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    producer = EventHubProducerClient.from_connection_string(conn_str=event_hub_connection_string, eventhub_name=event_hub_name)
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        print('Preparing batch of events ...')
        event_data_batch.add(EventData('First event'))
        event_data_batch.add(EventData('Second event'))
        event_data_batch.add(EventData('Third event'))

        # Send the batch of events to the event hub.
        print('Sending batch of events to Event Hub...')
        await producer.send_batch(event_data_batch)


def main():
    # Read configuration information
    config_dict = loadcfg()
    cfg_event_hub_connection_string = config_dict['eventhubconnectionstring']
    cfg_event_hub_name = config_dict['eventhubname']

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(cfg_event_hub_connection_string, cfg_event_hub_name))
    print('Sent')


if __name__ == '__main__':
    main()