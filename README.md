# Kubernetes Deployments

This repo contains Kubernetes YAML manifests charts for Autoreduce components, using Ansible for deployment.

## Architecture

Namespaces:

- traefik (Traefik)
- kafka (Strimzi)
- webapp (MySQL, Frontend, REST API)
- queue-processor (Queue processor) (Currently not used - see below)
- run-detection (Run Detection)

Additional services:

- Longhorn (for storing persistent data)
- Linkerd (Service Mesh)

### Note on Queue Processor

The queue processor is currently being deployed as a seperate service on an external VM (using the `qp_external` role).
This is because the queue-processor uses Docker to run the reduction, and Docker is not available on the Kubernetes cluster.

## Contributing setup

This repository has a pre-commit config availiable to assist with development, run this command with pre-commit on your terminal to install pre-commit hooks, so it runs when you commit to a branch:
`pre-commit install`
