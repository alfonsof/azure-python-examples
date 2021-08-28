from typing import List
import logging

import azure.functions as func


def main(events: List[func.EventHubEvent]):
    for event in events:
        logging.info('Python EventHub trigger processed an event: %s',
                        event.get_body().decode('utf-8'))
        logging.info(f'  EnqueuedTimeUtc = {event.enqueued_time}')
        logging.info(f'  SequenceNumber = {event.sequence_number}')
        logging.info(f'  Offset = {event.offset}')

        # Metadata
        for key in event.metadata:
            logging.info(f'Metadata: {key} = {event.metadata[key]}')
