# Frontend Helm Chart

This is an overview for the Kubernetes Deployment of the frontend.

## Containers

There are 2 containers in this chart:
    - autoreduce-frontend
    - nginx-sidecar

The autoreduce-frontend container is responsible for serving the frontend application via gunicorn.
The nginx container is responsible for serving serving static files.

In addition, there is also an initContainer, which is responsible for running Django's "collectstatic"
command, placing the content in a shared volume with the nginx-sidecar

## Services

There are 2 services in this chart:
    - frontend-gunicorn (autoreduce-frontend)
    - frontend-nginx (nginx-sidecar)

## IngressRoute

There are 2 ingress routes in this chart:
    - IngressRoute for the frontend, routing reduce.isis.cclrc.uk to the frontend service
    - IngressRoute for the frontend, routing reduce.isis.cclrc.uk/static to the nginx-sidecar service
