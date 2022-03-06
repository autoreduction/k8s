# Strimzi Kafka

## Create a Kafka namespace

```bash
kubectl create namespace kafka
```

## Apply Strimzi installation file

Apply the Strimzi install files, including ClusterRoles, ClusterRoleBindings
and some Custom Resource Definitions (CRDs).

The CRDs define the schemas used for declarative management of the Kafka cluster, Kafka topics and users.

```bash
kubectl create -f 'https://strimzi.io/install/latest?namespace=kafka' -n kafka
```

## Provision the Apache Kafka cluster

```bash
kubectl apply -f deployment/deployment.yaml -n kafka
```
