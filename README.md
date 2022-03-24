# autoreduce-k8s
Scripts for deploying parts of the Autoreduce service

# Architecture
Namespaces:
    - webapp (MYSQL, frontend)
    - monitoring (elastic, prometheus + grafana)
    - traefik (traefik)
    - kafka (strimzi kafka)
    - cert-manager (cert-manager)