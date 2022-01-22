# Azure Event Hub send event Python example

This folder contains a Python application example that handles Event Hubs on Microsoft Azure.

It handles an Event Hub and send events to an event hub event stream.

## Requirements

* You must have a [Microsoft Azure](https://azure.microsoft.com/) subscription.

* You must have the following installed:
  * Python 3
  * Azure CLI

* The code was written for:
  * Python 3
  * Azure SDK for Python: New Client Libraries (Azure Event Hub library v5)

* You install individual Azure library packages on a per-project basis depending on your needs. It is recommended using Python virtual environments for each project. There is no standalone "SDK" installer for Python.

* Install the specified python packages.

  ```bash
  pip install -r requirements.txt
  ```

## Using the code

* Sign in Azure (Interactively).

  The Azure CLI's default authentication method for logins uses a web browser and access token to sign in.

  1. Run the Azure CLI login command.

      ```bash
      az login
      ```

      If the CLI can open your default browser, it will do so and load an Azure sign-in page.

      Otherwise, open a browser page at https://aka.ms/devicelogin and enter the authorization code displayed in your terminal.

      If no web browser is available or the web browser fails to open, use device code flow with az login --use-device-code.

  2. Sign in with your account credentials in the browser.

  Make sure you select your subscription by:

  ```bash
  az account set --subscription <name or id>
  ```

* Create an Event Hubs Namespace and an Event Hub.

  1. Create an Event Hubs Namespace.

     An Event Hubs namespace provides a unique scoping container, in which you create one or more event hubs.

     To create a namespace in your resource group using the portal, do the following actions:

     1. You must create the Event Hubs Namespace, using the Azure console.

     2. Select the your data for: Suscription, Resource group, Namespace name and Location.

     3. Choose Basic for the pricing tier.

  2. Create an Event Hub.

     You must create the Event Hub, using the Azure console.

     To create an event hub within the namespace, do the following actions:

     1. On the Event Hubs Namespace page, select `Event Hubs` in the left menu.

     2. At the top of the window, select `+ Event Hub`.

     3. Type a name for your event hub, then select `Create`.

  3. Create a SAS Policy.

     You must create the SAS Policy, using the Azure console.

     1. On the Event Hubs page for the Event Hub created, select `Shared access policies` in the left menu.

     2. At the top of the window, select `+ Add`.

     3. Type a name for your Policy, select `Manage`, that includes `Send` and `Listen`, then select `Create`.

* Configure your application.

  We store the configuration information in a config file (`app.cfg`). The file content is:

  ```bash
  [Configuration]
  EventHubConnectionString=<EVENT_HUB_CONNECTION_STRING>
  EventHubName=<EVENT_HUB_NAME>
  ```

  You only need to edit the file `app.cfg` and modify the values of:
  
  * `<EVENT_HUB_CONNECTION_STRING>` by the Connection string to the Event Hub.
  * `<EVENT_HUB_NAME>` by the name to the Event Hub.
  
  The application uses this information for accessing your Event Hub.

* Run the code.

  Execute the python application:

  ```bash
  python sendereh.py
  ```

  You should see the next message:
  
  ```bash
  Preparing batch of events
  Sending batch of events
  Sent
  ```

* Test the application.

  The events should be in the Event Hub.
