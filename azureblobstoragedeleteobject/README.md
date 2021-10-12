# Azure Blob Storage Delete Object Python example

This folder contains a Python application example that handles Blob storage on Microsoft Azure.

Delete a Blob in a Blob Storage container in an Azure storage account.

## Requirements

* You must have a [Microsoft Azure](https://azure.microsoft.com/) subscription.

* You must have an Azure storage account.

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

* Create a storage account.

  An Azure storage account contains all of your Azure Storage data objects: blobs, file shares, queues, tables, and disks. The storage account provides a unique namespace for your Azure Storage data that's accessible from anywhere in the world over HTTP or HTTPS. Data in your storage account is durable and highly available, secure, and massively scalable.
  
  An storage account can content containers and every container can content blobs.

  ```bash
  Storage Account
              ├── Container_1/
              │   ├── Blob_1_1/
              │   └── Blob_1_2/
              │
              └── Container_2/
                  ├── Blob_2_1/
                  ├── Blob_2_2/
                  └── Blob_2_3/
  ```

  Create a storage account using the Azure portal:
  
  1. Select the `Storage account` option and choose `Create`.
  2. Select the `Subscription` in which you want to create the new storage account.
  3. Select the `Resource Group` for your storage account.
  4. Enter a `name` for your storage account.
  5. Select the `Region` for your storage account. 
  6. Select the `Performance` to be used.
  7. Select the `Redundancy` to be used.
  8. Click `Create` to create the storage account.

* Configure your application.

  A connection string includes the authentication information required for your application to access data in an Azure Storage account at runtime.

  Your application needs to access the connection string at runtime to authorize requests made to Azure Storage.

  You can find your storage account's connection strings in the Azure portal:
  
    1. Navigate to `Storage Account`.
    2. Select your storage account.
    3. Select `Access keys` and you can see your Storage account name, connection strings and account keys.

  The connection string looks like this:

    ```bash
    DefaultEndpointsProtocol=https;AccountName=<ACCOUNT_NAME>;AccountKey=<ACCOUNT_KEY>;EndpointSuffix=core.windows.net
    ```
  
  The application configuration is stored in the `app.cfg` file. The file content is:

  ```bash
  [StorageAuthentication]
  AccountName=<ACCOUNT_NAME>
  AccountKey=<ACCOUNT_KEY>
  ```

  You must edit the `app.cfg` file and replace the values of:
  
  * `<ACCOUNT_NAME>` by the account name of your storage account.
  * `<ACCOUNT_KEY>` by the account key of your storage account.
  
  The application uses this information for accessing your Azure storage account.

* Run the code.

  You must provide 2 parameters:

  * `<CONTAINER_NAME>` = Name of the container
  * `<BLOB_NAME>` = Name of the Blob

  Run application:

  ```bash
  python blobstoragedeleteobject.py container-example blob-example
  ```

* Test the application.

  You should not see the blob deleted in an Azure storage account.
