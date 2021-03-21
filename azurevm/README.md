# Azure Virtual Machines Python example

This folder contains a Python application example that handles Virtual Machines on Microsoft Azure.

## Requirements

* You must have a [Microsoft Azure](https://azure.microsoft.com/) subscription.
* The code was written for:
  * Python 3
  * Azure SDKs for Python
* Install the Azure SDKs for Python.

  Install the latest stable version (supports Python 2.7 and 3.x) via pip:

  ```bash
  pip install azure
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
