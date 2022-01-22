# Azure Blob Storage Upload Python example

This folder contains a Python application example that handles Blob storage on Microsoft Azure.

Upload a local file to a Blob Storage container in an Azure storage account.

## Requirements

* You must have a [Microsoft Azure](https://azure.microsoft.com/) subscription.

* You must have the following installed:
  * Python 3
  * Azure CLI

* The code was written for:
  * Python 3
  * Azure SDK for Python: New Client Libraries (Azure Blob Storage library v12)

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
    3. Select `Access keys` and you can see your Storage account connection string.

  The connection string looks like this:

  ```bash
  DefaultEndpointsProtocol=https;AccountName=<ACCOUNT_NAME>;AccountKey=<ACCOUNT_KEY>;EndpointSuffix=core.windows.net
  ```
  
  The application configuration is stored in the `app.cfg` file. The file content is:

  ```bash
  [Configuration]
  StorageAccountConnectionString=<STORAGE_ACCOUNT_CONNECTION_STRING>
  ```

  You must edit the `app.cfg` file and replace the value of:
  
  * `<STORAGE_ACCOUNT_CONNECTION_STRING>` by the connection string of your storage account.
  
  The application uses this information for accessing your Azure storage account.

* Run the code.

  You must provide 3 parameters, replace the values of:

  * `<CONTAINER_NAME>`  by name of the container.
  * `<BLOB_NAME>`       by blob name in the container.
  * `<LOCAL_FILE_NAME>` by local file name.

  Run application:

  ```bash
  python blobstorageupload.py <CONTAINER_NAME> <BLOB_NAME> <LOCAL_FILE_NAME>
  ```

* Test the application.

  You should see the new created blob in the Blob Storage container in an Azure storage account.
