# Kubernetes Deployments

Scripts for deploying parts of the Autoreduce service

## Architecture

Namespaces:

- traefik (Traefik)
- kafka (Strimzi)
- webapp (MYSQL, frontend, REST API)
- queue-processor (queue processor)
- run-detection (Run Detection)
- monitoring (Elastic, Prometheus + Grafana)

Additional services:

- Longhorn (for storing persistent data)
- Linkerd (Serivce Mesh)
