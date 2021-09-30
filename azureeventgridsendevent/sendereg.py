#!/usr/bin/python
# -*- coding: utf-8 -*-
# sendereg.py
# It is an example that handles Event Grids on Microsoft Azure.
# It handles an Event Grid and sends events to an Event Grid Topic.

import sys
import os
import configparser
from azure.core.credentials import AzureKeyCredential
from azure.eventgrid import EventGridPublisherClient
from azure.eventgrid import EventGridEvent


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


def main():
    # Read configuration information
    config_dict = loadcfg()
    cfg_event_grid_topic_key = config_dict['eventgridtopickey']
    cfg_event_grid_topic_endpoint = config_dict['eventgridtopicendpoint']

    event = EventGridEvent(
        data={"make": "Audi", "model": "Q5"},
        subject="myapp/vehicles/cars",
        event_type="recordInserted",
        data_version="1.0"
    )

    credential = AzureKeyCredential(cfg_event_grid_topic_key)
    print('Sending event to Event Grid Topic ...')
    client = EventGridPublisherClient(cfg_event_grid_topic_endpoint, credential)
    # Send event
    client.send(event)
    print('Sent')


if __name__ == '__main__':
    main()