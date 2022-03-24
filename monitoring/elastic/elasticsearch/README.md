# Deploy an ElasticSearch cluster
Apply a simple Elasticsearch cluster specification, with one Elasticsearch node:

If your Kubernetes cluster does not have any Kubernetes nodes with at least 2GiB of free memory, the pod will be stuck in Pending state.
```bash
kubectl apply -f elasticsearch-cluster.yaml
```

## Access ElasticSearch from local workstation
https://www.elastic.co/guide/en/cloud-on-k8s/current/k8s-deploy-elasticsearch.html

```bash
kubectl port-forward service/quickstart-es-http 9200
```

A default user called elastic is automatically created.
The password can be obtained with the following command:
```bash
PASSWORD=$(kubectl get secret quickstart-es-elastic-user -o go-template='{{.data.elastic | base64decode}}')
```

Test by requesting localhost:
```
curl -u "elastic:$PASSWORD" -k "https://localhost:9200"
```
