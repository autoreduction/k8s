# Autoreduce API Deployment

## Setting Environmental Variables

Firstly, update the values in api-secrets to match the credentials for your setup.
Then apply this as a Kubernetes Secret.
```bash
kubectl create secret generic webapp-secret --from-env-file=api-secrets -n api
```

Then apply the api-configmap:
```bash
kubectl apply -f api-configmap.yaml -n api
```

## Creating Deployment

To create the deployment of the REST API, run:

```bash
kubectl apply -f deployment.yaml -n api
```