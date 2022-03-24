kubectl apply -f prometheus-rules.yaml
kubectl apply -f strimzi-pod-monitor.yaml
kubectl apply -f prometheus-additional.yaml

https://strimzi.io/docs/operators/latest/deploying.html#assembly-metrics-config-files-str
