## Make sure Helm is installed
https://helm.sh/docs/intro/

## Traefik
helm repo add traefik https://helm.traefik.io/traefik
helm repo update
helm install traefik traefik/traefik -n kube-system -f ./traefik-values.yaml

## Run deployment
```bash
kubectl apply -f deployment.yaml
```

## Prometheus
https://traefik.io/blog/capture-traefik-metrics-for-apps-on-kubernetes-with-prometheus/

## Jaeger
https://traefik.io/blog/application-request-tracing-with-traefik-and-jaeger-on-kubernetes/

## Debugging
The Traefik Dashboard is not exposed by default, but you can make it accessible using port forwarding:
```bash
kubectl port-forward $(kubectl get pods --selector "app.kubernetes.io/name=traefik" --output=name) 9000:9000
```
Accessible with the url: http://127.0.0.1:9000/dashboard/
(note the trailing slash in the URL, which is required)
