# Azure Event Grid send event Python example

This folder contains a Python application example that handles Event Grids on Microsoft Azure.

It handles an Event Grid and sends events to an Event Grid Topic.

## Requirements

* You must have a [Microsoft Azure](https://azure.microsoft.com/) subscription.

* The code was written for:
  * Python 3
  * Azure SDKs for Python

* You install individual Azure library packages on a per-project basis depending on your needs. It is recommended using Python virtual environments for each project. There is no standalone "SDK" installer for Python.

* Install the specified python packages.

  ```bash
  pip install -r requirements.txt
  ```

## Using the code

* Configure your Azure access.

  You must create an Azure AD service principal in order to enable application to connect resources into Azure. The service principal grants your application to manage resources in your Azure subscription.

  The Azure SDKs Libraries for Java allow you to use several authentication schemes.

  The application uses an authentication file for authenticating.

  The credentials are taken from `AZURE_AUTH_LOCATION` environment variable.

  You can create a service principal and generate this file using Azure CLI 2.0 or using the Azure cloud shell.

  * Make sure you select your subscription by:

    ```bash
    az account set --subscription <name or id>
    ```

    and you have the privileges to create service principals.

  * Execute the following command for creating the service principal and the authentication file:
  
    ```bash
    az ad sp create-for-rbac --sdk-auth > my.azureauth
    ```
  
  * Set the `AZURE_AUTH_LOCATION` environment variable in your Operating System with the path of your authentication file.

    ```bash
    AZURE_AUTH_LOCATION = /path/to/my.azureauth
    ```

* Create an Event Grid Topic.

  An Event Grid topic provides a user-defined endpoint that you post your events to.

  You must create the Event Grid Topic, using the Azure console, do the following actions:

  1. Select `Create a resource` and chose `Event Grid Topic`.

  2. On the Event Grid Topics page, select `Create`.

  3. Choose the `Subscription`, `Resource group`, `Name` and `Region` for your Event Grid Topic.

  4. Select `Create`.

  You need the `Topic Key` and the `Topic Endpoint`. You can find these within the Event Grid Topic resource on the Azure portal.

* Configure your application.

  We store the configuration information in a config file (`app.cfg`). The file content is:

  ```bash
  [Configuration]
  EventGridTopicKey=<EVENT_GRID_TOPIC_KEY>
  EventGridTopicEndpoint=<EVENT_GRID_TOPIC_ENDPOINT>
  ```

  You only need to edit the file `app.cfg` and replace the values of:
  
  * `<EVENT_GRID_TOPIC_KEY>` by the key of the Event Grid Topic.
  * `<EVENT_GRID_TOPIC_ENDPOINT>` by the topic endpoint in the Event Grid.

    You can find the topic endpoint within the Event Grid Topic resource on the Azure portal.

    `https://<EVENT_GRID_TOPIC_NAME>.<REGION_NAME>.eventgrid.azure.net/api/events`
  
  The application uses this information for accessing your Event Grid Topic.

* Run the code.

  Execute the sender application:

  ```bash
  python sendereg.py
  ```

  You should see the next message:
  
  ```bash
  Sending event to Event Grid Topic ...
  Sent
  ```

* Test the application.

  The event should be in the Event Grid Topic.
