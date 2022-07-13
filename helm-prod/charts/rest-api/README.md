# Rest-API Helm Chart

This is an overview for the Kubernetes Deployment of the rest-api.

## Containers

There is one container in this chart:
    - autoreduce-rest-api

## Services

There is one service in this chart:
    - rest-api (autoreduce-rest-api)

## IngressRoute

There is one ingress route in this chart:
    - IngressRoute for the rest-api, routing reduce.isis.cclrc.uk/api to the rest-api service
