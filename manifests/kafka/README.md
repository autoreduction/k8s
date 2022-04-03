# Strimzi Kafka

## Deploying the Cluster Operator

Apply the Strimzi install files, including ClusterRoles, ClusterRoleBindings
and some Custom Resource Definitions (CRDs).

The CRDs define the schemas used for declarative management of the Kafka cluster, Kafka topics and users.

```
kubectl create namespace kafka
helm repo add strimzi https://strimzi.io/charts/
helm install my-release --set watchAnyNamespace=true strimzi/strimzi-kafka-operator -n kafka
```

## Deploy the Kafka Cluster

```
kubectl apply -f deployment/deployment.yaml -n kafka
```

## Create the data_ready topic

```
kubectl apply -f deployment/topic.yaml -n kafka
```
