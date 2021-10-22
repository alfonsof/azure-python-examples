# Azure Function Event Grid event Python example

This folder contains a Python application example that handles Functions on Microsoft Azure.

It handles an Azure Function that responds to an Event Grid event (trigger) when an event is sent to an Event Grid topic.

## Requirements

* You must have a [Microsoft Azure](https://azure.microsoft.com/) subscription.

* The code was written for:
  * Python 3

* To develop functions app with Python, you must have the following installed:
  * Python 3
  * Azure CLI
  * Azure Functions Core Tools Version 3.x

* Azure Functions Core Tools Version 3.x

  Azure Functions Core Tools lets you develop and test your functions on your local computer from the command prompt or terminal. Your local functions can connect to live Azure services, and you can debug your functions on your local computer using the full Functions runtime. You can even deploy a function app to your Azure subscription.

  Version 3.x/2.x: Supports either version 3.x or 2.x of the Azure Functions runtime. These versions support Windows, macOS, and Linux and use platform-specific package managers or npm for installation.

  Azure Functions Core Tools currently depends on either the Azure CLI or Azure PowerShell for authenticating with your Azure account. This means that you must install one of these tools to be able to publish to Azure from Azure Functions Core Tools.

  Version 3.x/2.x of the tools uses the Azure Functions runtime that is built on .NET Core. This version is supported on all platforms .NET Core supports, including Windows, macOS, and Linux.

  Install version 3.x of the Core Tools on your local computer:
  
  * For Windows:

    1. Download and run the Core Tools installer, based on your version of Windows:

        * v3.x - Windows 64-bit (Recommended. Visual Studio Code debugging requires 64-bit.)
        * v3.x - Windows 32-bit

    2. If you don't plan to use extension bundles, install the .NET Core 3.x SDK for Windows.

  * For MacOS:

    1. Install Homebrew, if it's not already installed.
    2. Install the Core Tools package:

       ```bash
       brew tap azure/functions
       brew install azure-functions-core-tools@3
       # if upgrading on a machine that has 2.x installed
       brew link --overwrite azure-functions-core-tools@3
       ```

    3. If you don't plan to use extension bundles, install the .NET Core 3.x SDK for macOS.

## Using the code

* Create the Azure Funtion project and the Azure Function (Boilerplate code).

  *This step is only necessary when you want to create an Azure Function from scratch.*

  The Azure Functions Core Tools help you to create the boilerplate code for the Azure Funtion project and the Azure Function:

  * Create an Azure Functions project.

    In the terminal window or from a command prompt, navigate to an empty folder for your project, and run the following command:

    ```bash
    func init azurefunctioneventgridevent
    ```

    In version 3.x/2.x, when you run the command you must choose a runtime for your project.

    Select `python`.

    Then, the project is created with these files:

    * `host.json` - JSON configuration file for the Function App.
    * `local.settings.json` - It stores app settings, connection strings, and settings used by local development tools. Settings in the local.settings.json file are used only when you are running projects locally.
    * `requirements.txt` - File with python dependencies.

    *Because `local.settings.json` can contain secrets downloaded from Azure, the file is excluded from source control by default in the `.gitignore` file.*

  * Create the Azure Function.

      In the terminal window or from a command prompt, move to the folder for your project, and run the following command:

      ```bash
      func new
      ```

      Select `Azure Event Grid trigger`.

      Select the name `EventGridTrigger`.

      Then, the function `EventGridTrigger` is created successfully from the `Event Grid trigger` template.

      The `EventGridTrigger` folder content is:

      * `__init__.py` - Code of the function.
      * `function.json` - Configuration of the function.

* Create an Event Grid Topic.

  An Event Grid topic provides a user-defined endpoint that you post your events to.

  You must create the Event Grid Topic, using the Azure console, do the following actions:

  1. Select `Create a resource` and chose `Event Grid Topic`.

  2. On the Event Grid Topics page, select `Create`.

  3. Choose the `Subscription`, `Resource group`, `Name` and `Region` for your Event Grid Topic.

  4. Select `Create`.

* Configure the Azure Function.

  The `function.json` file is configurated.

  The variable `name`, in the `function.json`, will hold the parameter that receives the event data.

* Create the Function App.

  1. You must create a Storage Account for the Function App, using the Azure console.

  2. You must create the Function App. You can create it in two ways:

      * Using the Azure console.

      * Using the Azure CLI tool:

        You create the Azure Function App by executing the command:

        ```bash
        az functionapp create --functions-version 3 --resource-group <RESOURCE_GROUP> --os-type Linux --consumption-plan-location westeurope --runtime python --name <FUNCTION_APP> --storage-account <STORAGE_ACCOUNT>
        ```

        In the previous command, replace with the proper:

        * `<RESOURCE_GROUP>` - Resource group name.
        * `<FUNCTION_APP>` - Function App name.
        * `<STORAGE_ACCOUNT>`- Storage Account name.

* Deploy the Azure Function to Azure.

  The deploy process to Azure Functions uses account credentials from the Azure CLI. Log in with the Azure CLI before continuing.

  ```bash
  az login
  ```

  To publish your local code to a function app in Azure, use the publish command:

  ```bash
  func azure functionapp publish <FUNCTION_APP>
  ```

  When the deploy is complete, you see the URL that you can use to access your Azure Function App:

  ```bash
  Deployment successful.
  Remote build succeeded!
  Syncing triggers...
  Functions in <FUNCTION_APP>:
      EventGridTrigger - [eventGridTrigger]
  ```

* Subscribe to an Event Subscription.

  You subscribe to an event grid topic to tell Event Grid which events you want to track, and where to send the events.

  You must subscribe to custom topic by creating an Event Subscription, using the Azure console, do the following actions:

  1. Go to your Event Grid Topic resource.

  2. Select `+ Event Subscription`.

  3. Enter a `Name` for the event subscription.

  4. Select `Azure Function` for the `Endpoint Type`.

  5. Choose `Select an endpoint`.

  6. For the function endpoint, select the Azure `Subscription` and `Resource group` your Function App is in and then select the `Function App` and `Function` you created earlier. Select `Confirm Selection`.
  
  7. Select `Create`.
  
* Test the function.

  You must send an event to your topic.

  In the Azure portal, select Cloud Shell. You use the Azure CLI and the `curl` command:

  1. Select Bash in the top-left corner of the Cloud Shell window.

  2. Run the following command to get the endpoint for the topic: After you copy and paste the command, update the `<TOPIC_NAME>` and `<RESOURCE_GROUP_NAME>` before you run the command.

      ```bash
      endpoint=$(az eventgrid topic show --name <TOPIC_NAME> -g <RESOURCE_GROUP_NAME> --query "endpoint" --output tsv)
      ```

  3. Run the following command to get the key for the custom topic: After you copy and paste the command, update the `<TOPIC_NAME>` and `<RESOURCE_GROUP_NAME>` before you run the command.

      ```bash
      key=$(az eventgrid topic key list --name <TOPIC_NAME> -g <RESOURCE_GROUP_NAME> --query "key1" --output tsv)
      ```

  4. Copy the following statement with the event definition, and press ENTER.

      ```bash
      event='[ {"id": "'"$RANDOM"'", "eventType": "recordInserted", "subject": "myapp/vehicles/motocycles", "eventTime": "'`date +%Y-%m-%dT%H:%M:%S%z`'", "data":{ "make": "Ducati", "model": "Monster"},"dataVersion": "1.0"} ]'
      ```

  5. Run the following `curl` command to post the event:

      ```bash
      curl -X POST -H "aeg-sas-key: $key" -d "$event" $endpoint
      ```

  You should see the next message in the log:
  
  ```bash
  Python EventGrid trigger processed an event: {"id": "<EVENT_ID>", "data": {"make": "Ducati", "model": "Monster"}, "topic": "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP_NAME>/providers/Microsoft.EventGrid/topics/<EVENT_GRID_TOPIC>", "subject": "myapp/vehicles/motocycles", "event_type": "recordInserted"}
  ```
