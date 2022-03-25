# Kubernetes Deployments

Scripts for deploying parts of the Autoreduce service

## Architecture

Namespaces:

- webapp (MYSQL, frontend)
- monitoring (Elastic, Prometheus + Grafana)
- kube-system (Traefik)
- kafka (Strimzi)
- cert-manager (cert-manager)
