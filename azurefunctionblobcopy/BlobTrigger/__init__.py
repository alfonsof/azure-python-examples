import logging

import azure.functions as func


def main(inputblob: func.InputStream, outputblob: func.Out[bytes]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Blob Name: {inputblob.name}\n"
                 f"Blob Size: {inputblob.length} bytes\n"
                 f"Blob URI: {inputblob.uri}")
    readbytes = inputblob.read()
    logging.info(f'Trigger function processed {len(readbytes)} bytes')
    # Copy blob to output
    outputblob.set(readbytes)
    logging.info(f"Copied")
