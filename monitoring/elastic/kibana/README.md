# Specify Kibana instance, associate with elastic cluster
```bash
kubectl apply -f kibana.yaml
```

## Access kibana from local workstation
```bash
kubectl port-forward service/quickstart-kb-http 5601
```
Open https://localhost:5601 in your browser

Login as the elastic user. The password can be obtained with the following command:
```bash
kubectl get secret quickstart-es-elastic-user -o=jsonpath='{.data.elastic}' | base64 --decode; echo
```
