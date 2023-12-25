## Azure Deployment

- Add these variables to the app services configration

  - DJANGO_SECRET_KEY = secret-value
  - DJANGO_ENV = production
  - SCM_DO_BUILD_DURING_DEPLOYMENT = true

- Disable secure database client connections in Mysql server parameters
  - require_secure_transport = OFF

## Dockerizing Django

- YT: https://www.youtube.com/watch?v=BoM-7VMdo7s
- Docker Django samples: https://docs.docker.com/samples/django/
- Docker/awesome-composer: https://github.com/docker/awesome-compose
