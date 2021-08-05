# Azure Function HTTP Request Python example

This folder contains a Python application example that handles Functions on Microsoft Azure.

It handles an Azure Function that responds to an HTTP request.

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

* Create an Azure Functions project
  
  In the terminal window or from a command prompt, navigate to an empty folder for your project, and run the following command:

  ```bash
  func init azurefunctionhttprequest
  ```

  In version 3.x/2.x, when you run the command you must choose a runtime for your project.

  Select `python`

  Then, the project is created with these files:

  * `host.json` - JSON configuration file.
  * `local.settings.json` - It stores app settings, connection strings, and settings used by local development tools. Settings in the local.settings.json file are used only when you're running projects locally.
  * `requirements.txt` - File with python dependencies.

  Because `local.settings.json` can contain secrets downloaded from Azure, the file is excluded from source control by default in the `.gitignore` file.

* Create the Azure Function
  
  In the terminal window or from a command prompt, move to the folder for your project, and run the following command:

  ```bash
  func new
  ```

  Select `HTTP trigger`

  Select the name `HttpTrigger`.
  
  Then, the function `HttpTrigger` is created successfully from the `HTTP trigger` template.

  The `HttpTrigger` folder content is:
  * `__init__.py` - Code of the function.
  * `function.json` - Configuration of the function.

* Run your function project locally

  You can run your function locally.
  
  Enter the following command to run your function app:

  ```bash
  func start
  ```

  The runtime will output a URL for any HTTP functions, which can be copied and run in your browser's address bar.
  
  ```bash
  http://localhost:7071/api/HttpTrigger
  ```

  And you have to add the parameter `name`:

  ```bash
  http://localhost:7071/api/HttpTrigger?name=Peter
  ```

  To stop debugging, use Ctrl-C in the terminal.

* Create the Function App

  You must create an Storage Account for the Function App, using the Azure console.

  You must create the Function App. You can create it in two ways:

  * Using the Azure console.

  * Using the Azure CLI:
  
    You create the Azure Function App by executing the command:

    ```bash
    az functionapp create --functions-version 3 --resource-group <RESOURCE_GROUP> --os-type Linux --consumption-plan-location westeurope --runtime python --name <FUNCTION_APP> --storage-account <STORAGE_ACCOUNT>
    ```

    Select the proper:

    * `<RESOURCE_GROUP>` - Resource group name.
    * `<FUNCTION_APP>` - Function App name.
    * `<STORAGE_ACCOUNT>`- Storage Account name.

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
  ..................
  Remote build succeeded!
  Syncing triggers...
  Functions in <FUNCTION_APP>:
      HttpTrigger - [httpTrigger]
          Invoke url: https://<FUNCTION_APP>.azurewebsites.net/api/httptrigger?code=<FUNCTION_KEY>
  ```

* Run the code.

  You can use the url that you got before, or using the Azure console, you can get:

  * The function URL: URL field

  * The function key: Functions menu > select function `HttpTrigger` > Function keys > `default` value

  Run the function:

  Your HTTP request normally looks like the following URL:

  ```bash
  https://<functionapp>.azurewebsites.net/api/<function>?code=<ApiKey>
  ```

  To run the code, you need to use the parameter `name`:

  ```bash
  https://<FUNCTION_APP>.azurewebsites.net/api/HttpTrigger?code=<FUNCTION_KEY>&name=PETER
  ```

* Test the function.

  Go to the URL: `https://<FUNCTION_APP>.azurewebsites.net/api/HttpTrigger?code=<FUNCTION_KEY>&name=PETER` using a browser.

  You should see the response:

  ```bash
  Hello, PETER. This HTTP triggered function executed successfully.
  ```
