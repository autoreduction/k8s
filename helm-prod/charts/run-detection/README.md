# Frontend Helm Chart

This is an overview for the Kubernetes CronJob of the run-detection package.

This is slightly different than the frontend, rest-api etc. due to this being a CronJob
instead of a Deployment. Therefore, this will run on a schedule, similarly to cron tasks in Unix.

## Containers

There is one container in this chart:
    - autoreduce-run-detection
