# Kubernetes Deployments

This repo contains Helm charts for Autoreduce components, using Ansible for deployment.

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
