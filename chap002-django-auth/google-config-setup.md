# Google Configuration Setup
In this document, we are going to setup Google configuration which is required to
use google as an authenticator in our Django App. Google Cloud provides this service.

## Create a New Project
To create a new project:
- Navigate to [Project Create](https://console.cloud.google.com/projectcreate?previousPage=%2Fwelcome%2Fnew&organizationId=0)
- Provide `Project name` and `Project ID` and click on create
![google-project-creation](images/google-project-create.png)

## Generating Credentials for Django App
- Search for `Credentials` in google cloud search box and open `credentials` (product: Google Workspace)
- Click on `Credentials in APIs and services` which is inside `credential` tab
- Complete the OAuth Consent which is inside `OAuth consent screen` with the information you know. With this consent Google displays a consent screen to the user including a summary of your project and its policies and the requested scopes of access.
- Once you complete OAuth Consent, move to `credential` and click on `+ CREATE CREDENTIALS` and select `OAuth client ID`. 
- Select application type as "Web Application"
- Give `Name` anything you want
- For **Authorized JavaScript origins**, add the following URIs:
  - http://localhost:8000
  - http://127.0.0.1:8000
- Under **Authorized redirect URIs**, add the following URIs:
  - http://127.0.0.1:8000/accounts/google/login/callback/
  - http://localhost:8000/accounts/google/login/callback/
- Click “Create” and note down your “Client ID” and “Client Secret.” We’ll use these later.