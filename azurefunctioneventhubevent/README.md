# Azure Function Event Hub event Python example

This folder contains a Python application example that handles Functions on Microsoft Azure.

It handles an Azure Function that responds to an Event Hub event (trigger) when an event is sent to an event hub event stream.

## Requirements

* You must have a [Microsoft Azure](https://azure.microsoft.com/) subscription.

* To develop functions app with Python, you must have the following installed:
  * Python 3
  * Azure CLI
  * Azure Functions Core Tools Version 3.x

* The code was written for:
  * Python 3

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
    func init azurefunctioneventhubevent
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

    Select `Azure Event Hub trigger`.

    Select the name `EventHubTrigger`.

    Then, the function `EventHubTrigger` is created successfully from the `Event Hub trigger` template.

    The `EventHubTrigger` folder content is:

    * `__init__.py` - Code of the function.
    * `function.json` - Configuration of the function.

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

* Configure the Azure Function.

  1. You must configurate the `function.json` file:

      * Defining the `connection` with a variable `MY_EVENT_HUB_IN` for the in binding:

        ```bash
        "connection": "MY_EVENT_HUB_IN"
        ```

      The variable `name`, in the `function.json`, will hold the parameter that receives the event item.

  2. You must configure the connection string for trigger in the `local.settings.json` file when running locally.

      You must define the `MY_EVENT_HUB_IN` variable in the `local.settings.json` file:

      ```bash
      "MY_EVENT_HUB_IN": "Endpoint=sb://<EVENT_HUB_NAMESPACE>.servicebus.windows.net/;SharedAccessKeyName=<EVENT_HUB_SAS_POLICY>;SharedAccessKey=<EVENT_HUB_KEY>",
      ```

      Replace with the proper:

      * `<EVENT_HUB_NAMESPACE>` - Event Hub namespace.
      * `<EVENT_HUB_SAS_POLICY>` - Event Hub SAS Policy.
      * `<EVENT_HUB_KEY>` - Key of the Event Hub.

      You must define the `AzureWebJobsStorage` variable in the `local.settings.json` file:

      ```bash
      "AzureWebJobsStorage": "DefaultEndpointsProtocol=https;AccountName=<STORAGE_ACCOUNT_NAME>;AccountKey=<STORAGE_ACCOUNT_KEY>;EndpointSuffix=core.windows.net",
      ```

      Replace with the proper:

      * `<STORAGE_ACCOUNT_NAME>` - Name of the Storage Account.
      * `<STORAGE_ACCOUNT_KEY>` - Key of the Storage Account.

* Run your function project locally.

  You can run your function locally.
  
  Enter the following command to run your function app:

  ```bash
  func start
  ```

  The runtime will waiting for a Event Hub event (trigger).

  You must send an event to your Event Hub.

  You can use the Python application `sendereh.py` (Event Hub send event). You can get it following this link: [../azureeventhubsendevent/](../azureeventhubsendevent)

  Execute the python application:

  ```bash
  python sendeh.py
  ```

  You should see the next message in the log:
  
  ```bash
  Python EventHub trigger processed an event: <XXXXXXXXXXXXXXXXX>
    EnqueuedTimeUtc = <YYYY-MM-DD HH:MM:SS.XXXXXXXXX>
    SequenceNumber = <XX>
    Offset = <XXXX>
    Metadata: <XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX>
  ```

  To stop debugging, use Ctrl-C in the terminal.

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
      EventHubTrigger - [eventHubTrigger]
  ```

* Configure the connection string for trigger Event Hub in the Function App.

  You must configure the connection strings or secrets for trigger, input map to values in the application settings for the Function App when running in Azure.

  You can make that in two ways:

  * Using the Azure console.

    Go to your Function App.

    Select: `Settings > Configuration > Application settings > + New application setting`

    Set the setting `MY_EVENT_HUB_IN` name to:

    `Endpoint=sb://<EVENT_HUB_NAMESPACE>.servicebus.windows.net/;SharedAccessKeyName=<EVENT_HUB_SAS_POLICY>;SharedAccessKey=<EVENT_HUB_KEY>`

    Select `Save`.

  * Using the Azure CLI.

    ```bash
    az functionapp config appsettings set --name MyFunctionApp --resource-group MyResourceGroup --settings "MY_EVENT_HUB_IN=Endpoint=sb://<EVENT_HUB_NAMESPACE>.servicebus.windows.net/;SharedAccessKeyName=<EVENT_HUB_SAS_POLICY>;SharedAccessKey=<EVENT_HUB_KEY>"
    ```

  In both cases, replace with the proper:

  * `<EVENT_HUB_NAMESPACE>` - Event Hub namespace.
  * `<EVENT_HUB_SAS_POLICY>` - Event Hub SAS Policy.
  * `<EVENT_HUB_KEY>` - Key of the Event Hub.


* Test the function.

  You must send an event to your Event Hub.

  You can use the Python application `sendereh.py` (Event Hub send event). You can get it following this link: [../azureeventhubsendevent/](../azureeventhubsendevent)

  Execute the python application:

  ```bash
  python sendeh.py
  ```

  You should see the next message in the log:
  
  ```bash
  Python EventHub trigger processed an event: <XXXXXXXXXXXXXXXXX>
    EnqueuedTimeUtc = <YYYY-MM-DD HH:MM:SS.XXXXXXXXX>
    SequenceNumber = <XX>
    Offset = <XXXX>
    Metadata: <XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX>
  ```
