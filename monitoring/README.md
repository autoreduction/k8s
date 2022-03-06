# Getting Prometheus Operator

```bash
curl -s https://raw.githubusercontent.com/coreos/prometheus-operator/master/bundle.yaml | sed -e '/[[:space:]]*namespace: [a-zA-Z0-9-]*$/s/namespace:[[:space:]]*[a-zA-Z0-9-]*$/namespace: monitoring/' > prometheus-operator-deployment.yaml
```

## Install Order

```bash
kubectl create namespace monitoring
kubectl create -f prometheus-operator-deployment.yaml -n monitoring
kubectl apply -f prometheus-additional.yaml -n monitoring
kubectl apply -f strimzi-pod-monitor.yaml -n monitoring
kubectl apply -f prometheus-rules.yaml -n monitoring
kubectl apply -f prometheus.yaml -n monitoring
kubectl apply -f grafana.yaml -n monitoring
```

## Grafana Dashboard

Use port forwarding to access Grafana user interface:

```bash
kubectl port-forward svc/grafana 3000:3000 -n monitoring
```

In a web browser, access the Grafana login screen using the URL <http://localhost:3000>
Default username: admin
Default password: admin

In Configuration > Data Sources, add Prometheus as a data source.
    - Specify a name
    - Add Prometheus as the type
    - Specify a Prometheus server URL (<http://prometheus-operated:9090>)

### Importing a Dashboard

- Click the + icon and then click Import.
- Copy the json of the dashboard you want to import from the grafana-dashboards folder.
- Paste the JSON into the text box, and then click Load.
