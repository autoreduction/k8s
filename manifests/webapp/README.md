# Autoreduce Webapp Deployment

This repo contains the scripts needed to deploy the frontend of autoreduce.

Traefik ingress to reverse proxy to port 80 of the pod
Nginx sidecar listening infront of Gunicorn on port 80 to serve static content.

## Traefik

Traefik IngressRoutes are used as a reverse proxy for the webapp.
For these to work, Traefik must be installed.

```
kubectl create ns traefik
helm repo add traefik https://helm.traefik.io/traefik
helm repo update
helm install traefik traefik/traefik
```

## Setting Environmental Variables

Firstly, update the values in webapp-secrets to match the credentials for your setup.
Then apply this as a Kubernetes Secret.
```bash
kubectl create secret generic webapp-secret --from-env-file=webapp-secrets
```

Then apply the webapp-configmap:
```bash
kubectl apply -f webapp-configmap.yaml -n webapp
```

## Creating Deployment

Firstly, you need to run the migrations on the database.
This is done by running the django-migrate job:

```bash
kubectl apply -f django-migrate-job.yaml -n webapp
```

The job will delete itself once it has finished successfully.

To then create the deployment of the frontend, run:

```bash
kubectl apply -f deployment.yaml -n webapp
```

## Cert Manager

```
kubectl create ns cert-manager
helm repo add jetstack https://charts.jetstack.io
helm repo update
helm upgrade --install cert-manager --namespace cert-manager --version v1.7.2 jetstack/cert-manager --set installCRDs=true
```

## Prometheus

<https://traefik.io/blog/capture-traefik-metrics-for-apps-on-kubernetes-with-prometheus/>

## Jaeger

<https://traefik.io/blog/application-request-tracing-with-traefik-and-jaeger-on-kubernetes/>

## Debugging

The Traefik Dashboard is not exposed by default, but you can make it accessible using port forwarding:

```bash
kubectl port-forward $(kubectl get pods --selector "app.kubernetes.io/name=traefik" --output=name) 9000:9000
```

Accessible with the url: <http://127.0.0.1:9000/dashboard/>
(note the trailing slash in the URL, which is required)