# Prerequisites

- Must have Kubernetes, Helm, Ansible, and Ansible-Galaxy installed in your Python environment
- Install the ansible-galaxy requirements with ```ansible-galaxy install -r requirements.yaml```
- Deployment cluster kubeconfig should be specified in either ~/.kube/config, or the path to the config should be set as KUBECONFIG environmental variable in the shell. To get the kubeconfig, follow the instructions in the [README](https://github.com/autoreduction/k8s-infra) on the k8s-infra repo.
- Set the Image tags you wish to deploy in group_vars [vars.yaml](./group_vars/all/vars.yaml)
- Set the node IP address in group_vars [vars.yaml](./group_vars/all/vars.yaml) - it can be any node in the cluster
- Ensure the SSH keys of the users you wish to have access to the external queue-processor are in [users.yaml](./group_vars/all/users.yaml)
- When prompted by the playbook, enter in your FED ID password and the vault pass

## Tags

Be aware that tags use underscore ( _ ) instead of hyphens ( - ). E.g. To deploy rest-api, use the tag ```rest_api```

The main three tags that you will be using are:

- ```autoreduce``` tag deploys traefik, kafka, mysql, frontend, rest-api, run-detection.
- ```queue_processor``` tag deploys the external queue-processor.
- ```webapp``` tag deploys frontend, rest-api, run-detection.

Specific roles can be run by calling on their tags:

- ```traefik``` tag deploys Traefik
- ```strimzi_kafka``` tag deploys Strimzi Kafka
- ```mysql``` tag deploys MySQL
- ```frontend``` tag deploys Frontend
- ```rest_api``` tag deploys Rest-API
- ```run_detection``` tag deploys Run Detection

## Vaults

- Password for the development vault is _password_
- If deploying anything apart from qp-external, use ```--limit prod``` or ```--limit dev``` at the end of the commands to deploy using either the production or development vaults respectively
- If deploying qp-external, use ```--limit qp_external_prod``` or ```--limit qp_external_dev``` at the end of the commands to deploy using either the production or development vaults respectively

## Full Deployment

To deploy the whole autoreduction service, run these two commands:

```bash
ansible-playbook autoreduce.yaml --tags autoreduce --ask-vault-pass --limit prod
ansible-playbook autoreduce.yaml -K --tags qp_external --ask-vault-pass --limit qp_external_prod -e system_reboot=true
```

### Other examples

Deploy all k8s-based services using the development vault

```bash
ansible-playbook autoreduce.yaml --tags autoreduce --ask-vault-pass --limit dev
```

Deploy only the webapp services (run frontend, mysql, rest-api - ignore all other tags)

```bash
ansible-playbook autoreduce.yaml --tags webapp --ask-vault-pass --limit prod
```

Deploy only the external queue-processor using the development vault

```bash
ansible-playbook autoreduce.yaml -K --tags qp_external --ask-vault-pass --limit qp_external_dev
```

Skip the run-detection when deploying autoreduction (run autoreduction-tagged tasks, ignoring run-detection)

```bash
ansible-playbook autoreduce.yaml --tags autoreduce --skip-tags run_detection --ask-vault-pass --limit prod
```
