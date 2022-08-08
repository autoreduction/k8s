# Kubernetes Deployments

This repo contains Kubernetes YAML manifests charts for Autoreduce components, using Ansible for deployment.

## Architecture

Namespaces:

- traefik (Traefik)
- kafka (Strimzi)
- webapp (MySQL, Frontend, REST API)
- queue-processor (Queue processor)
- run-detection (Run Detection)

Additional services:

- Longhorn (for storing persistent data)
- Linkerd (Serivce Mesh)

## Contributing setup

This repository has a pre-commit config availiable to assist with development, run this command with pre-commit on your terminal to install pre-commit hooks, so it runs when you commit to a branch:
`pre-commit install`
