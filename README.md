# Kubernetes Deployments

Scripts for deploying parts of the Autoreduce service

## Architecture

Namespaces:

- kube-system (Traefik)
- kafka (Strimzi)
- webapp (MYSQL, frontend)
- api (REST API)
- queue-processor (queue processor)
- run-detection (Run Detection)
- monitoring (Elastic, Prometheus + Grafana)
