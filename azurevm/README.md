# Azure Virtual Machines Python example

This folder contains a Python application example that handles Virtual Machines on Microsoft Azure.

## Requirements

* You must have a [Microsoft Azure](https://azure.microsoft.com/) subscription.

* You must have the following installed:
  * Python 3
  * Azure CLI
  
* The code was written for:
  * Python 3
  * Azure SDK for Python: New Management Libraries
  
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

* Configure your AZURE_SUBSCRIPTION_ID environment variable.

  Set the `AZURE_SUBSCRIPTION_ID` environment variable with the Microsoft Azure subscription ID.

  To set this variable on Linux, macOS, or Unix, use `export`:

  ```bash
  export AZURE_SUBSCRIPTION_ID=<SUBSCRIPTION_ID>
  ```

  To set this variable on Windows, use `set`:

  ```bash
  set AZURE_SUBSCRIPTION_ID=<SUBSCRIPTION_ID>
  ```

  You must replace the value of:

  * `<SUBSCRIPTION_ID>` by the Microsoft Azure subscription ID (Ex.: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx").

* Run the code.

  Run application:

  ```bash
  python azurevm.py
  ```

  You can select an option in the menu in order to run every command:

  * 1 = List all Virtual Machines
  * 2 = Create a Virtual Machine
  * 3 = List Virtual Machine
  * 4 = Start Virtual Machine
  * 5 = Stop Virtual Machine
  * 6 = Restart Virtual Machine
  * 7 = Delete/Deallocate Virtual Machine

* Test the application.

  You should see the new virtual machine and modification of states with the Azure console.
