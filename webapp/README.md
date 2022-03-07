# Port forwarding
Command below will make service accessible outside of Minikube.

```bash
kubectl port-forward svc/frontend-service 32001:80 -n autoreduce
```

Can then be accessed from <http://localhost:32001/>
