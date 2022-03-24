```bash
kubectl apply -f https://raw.githubusercontent.com/elastic/cloud-on-k8s/2.1/config/recipes/beats/heartbeat_es_kb_health.yaml
```

Deploys Heartbeat as a single Pod deployment that monitors the health of Elasticsearch and Kibana by TCP probing their Service endpoints. Heartbeat expects that Elasticsearch and Kibana are deployed in the default namespace.

