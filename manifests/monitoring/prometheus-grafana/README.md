# Deploy the Prometheus Stack

This stack includes Prometheus Metrics server, Grafana, Alert Manager, and Metrics Exporter
https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack

```
kubectl create ns monitoring
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus-stack prometheus-community/kube-prometheus-stack -n monitoring
```

## Debug
Port forward to check if setup successfully.

```
kubectl port-forward svc/prometheus-stack-grafana 8080:80 -n monitoring
kubectl port-forward svc/prometheus-stack-kube-prom-prometheus 9090 -n monitoring
kubectl port-forward svc/prometheus-stack-kube-prometheus-alertmanager 9093 -n monitoring
```

This will make Grafana accessible on <http://localhost:8080>, Prometheus on <http://localhost:9090> and Alert Manager
on <http://localhost:9093>

You'll see that Grafana is already configured with lots of useful dashboards and Prometheus is configured with Rules to send alerts for pretty much everything you need to monitor in a production cluster.

# Traefik
All we need to do to get Prometheus scraping Traefik is add a Prometheus Operator ServiceMonitor resource which tells it the details of the existing service to scrape.
Note: Ensure selector and namespaceSelector are correct.

```
kubectl apply -f traefik-service-monitor.yaml
```

You can verify that Prometheus is now scraping Traefik for metrics at <http://localhost:9090/targets>

# Grafana
Previously you deployed Grafana using the kube-prometheus-stack Helm chart.
You'll need to forward port 80 from the Grafana service to a local port.

```
kubectl port-forward svc/prometheus-stack-grafana 8080:80
```

In a web browser, access the Grafana login screen using the URL <http://localhost:8080>
Default username: admin
Default password: prom-operator

# Notes
Inspiration taken from:
https://github.com/cablespaghetti/k3s-monitoring
