# Python examples on Microsoft Azure

This repo contains Python code examples on Microsoft Azure.

These examples show how to use Python 3 and Azure SDK for Python in order to manage services on Microsoft Azure.

Azure SDK for Python allows Python developers to write software that makes use of Azure services like Virtual Machines and Blob storage.

## Quick start

You must have a [Microsoft Azure](https://azure.microsoft.com/) subscription.

You must have an Azure storage account for the Azure Blob Storage examples.

The code for the samples is contained in individual folders on this repository.

For instructions on running the code, please consult the README in each folder.

This is the list of examples:

**Compute - Azure Virtual Machines:**

* [azurevm](/azurevm) - Azure Virtual Machines: Example of how to handle Azure Virtual Machines.

**Compute - Azure Functions:**

* [azurefunctionhttprequest](/azurefunctionhttprequest) - Azure Function HTTP Request: Example of how to handle an Azure Function that responds to an HTTP request.
* [azurefunctionblobevent](/azurefunctionblobevent) - Azure Function Blob Storage event: Example of how to handle an Azure Function that responds to a Blob Storage event (trigger) when a blob appears in a blob storage.
* [azurefunctionblobcopy](/azurefunctionblobcopy) - Azure Function Blob Storage copy: Example of how to handle an Azure Function that responds to a Blob Storage event (trigger) and copy the blob when it appears in a blob storage to another blob storage.
* [azurefunctionblobmove](/azurefunctionblobmove) - Azure Function Blob Storage move: Example of how to handle an Azure Function that responds to a Blob Storage event (trigger) and move the blob when it appears in a blob storage to another blob storage.
* [azurefunctioneventgridevent](/azurefunctioneventgridevent) - Azure Function Event Grid event: Example of how to handle an Azure Function that responds to an Event Grid event (trigger) when an event is sent to an Event Grid topic.
* [azurefunctioneventhubevent](/azurefunctioneventhubevent) - Azure Function Event Hub event: Example of how to handle an Azure Function that responds to an Event Hub event (trigger) when an event is sent to an event hub event stream.

**Storage - Azure Blob Storage:**

* [azureblobstoragecreate](/azureblobstoragecreate) - Azure Blob Storage Create: Example of how to handle Azure Blob Storage and create a new Blob Storage container in an Azure storage account.
* [azureblobstoragedelete](/azureblobstoragedelete) - Azure Blob Storage Delete: Example of how to handle Azure Blob Storage and delete a Blob Storage container in an Azure storage account.
* [azureblobstoragelist](/azureblobstoragelist) - Azure Blob Storage List: Example of how to handle Azure Blob Storage and list the blobs in a Blob Storage container in an Azure storage account.
* [azureblobstoragelistall](/azureblobstoragelistall) - Azure Blob Storage List All: Example of how to handle Azure Blob Storage and List the blobs in all Blob Storage containers in an Azure storage account.
* [azureblobstorageupload](/azureblobstorageupload) - Azure Blob Storage Upload: Example of how to handle Azure Blob Storage and upload a local file to a Blob Storage container in an Azure storage account.
* [azureblobstoragedownload](/azureblobstoragedownload) - Azure Blob Storage Download: Example of how to handle Azure Blob Storage and Download a Blob from a Blob Storage container in an Azure storage account.
* [azureblobstoragedeleteobject](/azureblobstoragedeleteobject) - Azure Blob Storage Delete Object: Example of how to handle Azure Blob Storage and delete a Blob in a Blob Storage container in an Azure storage account.
* [azureblobstoragecopy](/azureblobstoragecopy) - Azure Blob Storage Copy: Example of how to handle Azure Blob Storage and copy a Blob from a Blob Storage container to another one in an Azure storage account.
* [azureblobstoragemove](/azureblobstoragemove) - Azure Blob Storage Move: Example of how to handle Azure Blob Storage and move a Blob from a Blob Storage container to another one in an Azure storage account.

**Messaging - Azure Event Grid, Azure Event Hub:**

* [azureeventhubsendevent](/azureeventhubsendevent) - Azure Event Hub send: Example of how to handle an Event Hub and sends events to an event hub event stream.
* [azureeventhubreceiveevent](/azureeventhubreceiveevent) - Azure Blob Storage Move: Example of how to handle an Event Hub and  receives events from an event hub event stream.

## License

This code is released under the MIT License. See LICENSE file.
