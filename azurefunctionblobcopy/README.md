# Azure Function Blob Storage copy Python example

This folder contains a Python application example that handles Functions on Microsoft Azure.

It handles an Azure Function that responds to a Blob Storage event (trigger) and copy the blob when it appears in a blob container to another Blob container.

## Requirements

* You must have a [Microsoft Azure](https://azure.microsoft.com/) subscription.

* The code was written for:
  * Python 3

* To develop functions app with Python, you must have the following installed:
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

* Create the Azure Funtion project and the Azure Function (Boilerplate code)

  The Azure Functions Core Tools help you to create the boilerplate code for the Azure Funtion project and the Azure Function:

  * Create an Azure Functions project

    In the terminal window or from a command prompt, navigate to an empty folder for your project, and run the following command:

    ```bash
    func init azurefunctionblobcopy
    ```

    In version 3.x/2.x, when you run the command you must choose a runtime for your project.

    Select `python`

    Then, the project is created with these files:

    * `host.json` - JSON configuration file for the Function App.
    * `local.settings.json` - It stores app settings, connection strings, and settings used by local development tools. Settings in the local.settings.json file are used only when you are running projects locally.
    * `requirements.txt` - File with python dependencies.

    *Because `local.settings.json` can contain secrets downloaded from Azure, the file is excluded from source control by default in the `.gitignore` file.*

  * Create the Azure Function

    In the terminal window or from a command prompt, move to the folder for your project, and run the following command:

    ```bash
    func new
    ```

    Select `Azure Blob Storage trigger`

    Select the name `BlobTrigger`.

    Then, the function `BlobTrigger` is created successfully from the `Blob trigger` template.

    The `BlobTrigger` folder content is:

    * `__init__.py` - Code of the function.
    * `function.json` - Configuration of the function.

* Create the Function App

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

* Create a Storage Account for the input source
  
  You must create the Storage Account, using the Azure console.
  The storage account must be a StorageV2 (general purpose v2) account kind.
  Create a blob container with the `samples-workitems` name in this Storage Account.

* Create a Storage Account for the ouput target
  
  You must create the Storage Account, using the Azure console.
  The storage account must be a StorageV2 (general purpose v2) account kind.
  Create a blob container with the `samples-workitems` name in this Storage Account.

* Configure the Azure Function

  1. You must configurate the `function.json` file:

      * Defining the `connection` with a variable `MY_STORAGE_IN` for the in binding:

        ```bash
        "connection": "MY_STORAGE_IN"
        ```

      * Defining the `connection` with a variable `MY_STORAGE_OUT` for the out binding:

        ```bash
        "connection": "MY_STORAGE_OUT"
        ```

      The `name` variable, in the `function.json` file, will hold the name of the file found in the blob container, while `inputblob` variable will hold the actual contents of the file, and the `outputblob` variable will hold the output file.

  2. You must configure the connection strings or secrets for trigger, input sources and output target map to values in:
  
      * The `local.settings.json` file when running locally.

        You must define the `MY_STORAGE_IN` and `MY_STORAGE_OUT` variables in the `local.settings.json` file:

        ```bash
        "MY_STORAGE_IN": "DefaultEndpointsProtocol=https;AccountName=<STORAGE_ACCOUNT_IN>;AccountKey=<ACCOUNT_KEY_IN>;EndpointSuffix=core.windows.net",

        "MY_STORAGE_OUT": "DefaultEndpointsProtocol=https;AccountName=<STORAGE_ACCOUNT_OUT>;AccountKey=<ACCOUNT_KEY_OUT>;EndpointSuffix=core.windows.net"
        ```

        Replace with the proper:

        * `<STORAGE_ACCOUNT_IN>` - Storage Account name for input source.
        * `<ACCOUNT_KEY_IN>` - Account Key of the Storage Account for input source.
        * `<STORAGE_ACCOUNT_OUT>`- Storage Account name for output target.
        * `<ACCOUNT_KEY_OUT>` - Account Key of the Storage Account for output target.

      * The application settings for the Function App when running in Azure.

        You can make that in two ways:

        * Using the Azure console.

          Go to your Function App
          Select: Settings > Configuration > Application settings

          Set the setting `MY_STORAGE_IN` name to:
          `DefaultEndpointsProtocol=https;AccountName=<STORAGE_ACCOUNT_IN>;AccountKey=<ACCOUNT_KEY_IN>;EndpointSuffix=core.windows.net`

          Set the setting `MY_STORAGE_OUT` name to:
          `DefaultEndpointsProtocol=https;AccountName=<STORAGE_ACCOUNT_OUT>;AccountKey=<ACCOUNT_KEY_OUT>;EndpointSuffix=core.windows.net`

        * Using the Azure CLI

          ```bash
          az functionapp config appsettings set --name MyFunctionApp --resource-group MyResourceGroup --settings "MY_STORAGE_IN=DefaultEndpointsProtocol=https;AccountName=<STORAGE_ACCOUNT_IN>;AccountKey=<ACCOUNT_KEY_IN>;EndpointSuffix=core.windows.net"
          ```

          ```bash
          az functionapp config appsettings set --name MyFunctionApp --resource-group MyResourceGroup --settings "MY_STORAGE_OUT=DefaultEndpointsProtocol=https;AccountName=<STORAGE_ACCOUNT_OUT>;AccountKey=<ACCOUNT_KEY_OUT>;EndpointSuffix=core.windows.net"
          ```

        In both cases, replace with the proper:

        * `<STORAGE_ACCOUNT_IN>`- Storage Account name for input source.
        * `<ACCOUNT_KEY_IN>` - Account Key of the Storage Account for input source.
        * `<STORAGE_ACCOUNT_OUT>`- Storage Account name for output target.
        * `<ACCOUNT_KEY_OUT>` - Account Key of the Storage Account for output target.

* Run your function project locally

  You can run your function locally.
  
  Enter the following command to run your function app:

  ```bash
  func start
  ```

  The runtime will waiting for a blob event (trigger).

  You can upload a file to the container and you will get the message with the result.

  Example:
  
  ```bash
  Python blob trigger function processed blob
  Name: samples-workitems/<FILE_NAME>
  Blob Size: <XX> bytes
  Full Blob URI: https://<STORAGE_ACCOUNT_IN>.blob.core.windows.net/samples-workitems/<FILE_NAME>
  Trigger function processed <XX> bytes
  Copied
  ```

  To stop debugging, use Ctrl-C in the terminal.

* Deploy the function to Azure

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
      BlobTrigger - [blobTrigger]
  ```

* Test the function.

  Upload a file to the source blob storage container in the storage account.

  The file from the source blob storage container should be copied to the target blob storage container.

  You should see the next message in the log:
  
  ```bash
  Python blob trigger function processed blob
  Name: samples-workitems/<FILE_NAME>
  Blob Size: <XX> bytes
  Full Blob URI: https://<STORAGE_ACCOUNT_IN>.blob.core.windows.net/samples-workitems/<FILE_NAME>
  Trigger function processed <XX> bytes
  Copied
  ```
