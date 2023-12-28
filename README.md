## Azure Deployments

- Add these variables to the app services configration

  - DJANGO_SECRET_KEY = secret-value
  - DJANGO_ENV = production
  - DJANGO_ALLOWED_HOSTNAME = <azure-webapp-host>
  - SCM_DO_BUILD_DURING_DEPLOYMENT = true

- Disable secure database client connections in Mysql server parameters
  - require_secure_transport = OFF

## Dockerizing Django

- YT: https://www.youtube.com/watch?v=BoM-7VMdo7s
- Docker Django samples: https://docs.docker.com/samples/django/
- Docker/awesome-composer: https://github.com/docker/awesome-compose

## Deployment Strategy 1

- Description: Deploy app to an app service and database (without redis cache) connected to GH with a staging deployment slot

1. Create a resource group and deploy a web app + database
2. Add the below application settings to the web app as deployment slot settings

- DJANGO_SECRET_KEY = secret-value
- DJANGO_ENV = production
- DJANGO_ALLOWED_HOSTNAME = <azure-webapp-host>

3. Turn file system application logging ON in `App Service Logs` on the web app
4. Turn `require_secure_transport` OFF in the database server parameters
5. In `Deployment Center`, connect the web app to this repo for the initial production deployment

- Authentication type: User-assigned identity

6. Once deployed, ssh into the web app and run the database migrations
7. Next, disconnect GH from the production web app and delete any old GH secrets that were previously added by Azure for the production slot

- AZUREAPPSERVICE-CLIENTID-\*
- AZUREAPPSERVICE-SUBSCRIPTIONID-\*
- AZUREAPPSERVICE-TENANTID-\*

8. Create a `Staging` deployment slot. Update the application settings as needed

- DJANGO_ENV = staging
- etc

8. Turn file system application logging ON in `App Service Logs` on the Staging web app
9. Create a new mysql database that uses the same VNet/subnet as the production database and update the Staging slots AZURE-MYSQL-\* application setting values to point to this instance

- Create the staging database in this instance
- Ssh and run the database migrations

10. Connect the Staging slot to GH.

- Update the created managed identitys' GH federated credential to use the `Staging` environment
- Give access to the managed identity to the production web app resource

10. Now that the GH workflow deploys to the staging slot, push some new code and naviate to the staging slots host url to confirm the deployment

11. Perform a swap with preview

- `az webapp deployment slot swap --slot Staging --action preview --ids $webappid`
- Confirm all is good in staging
- `az webapp deployment slot swap --slot Staging --action swap --ids $webappid`
