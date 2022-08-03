# Prerequisites

- Must have Kubernetes, Helm, Ansible, and Ansible-Galaxy installed in your Python environment
- Install the ansible-galaxy requirements with ```ansible-galaxy install -r requirements.yaml```
- Deployment cluster should be specified in ~/.kube/config and set as the current context
- Set the Image tag you wish to deploy in group_vars

## Example Deployment Commands

- Create a file at ~/.vault_pass.txt with the vault password (_password_ for the dev vault)
- Enter correct Python path for localhost in the inventory file
- If deploying qp-external, use ```--limit qp_external_prod``` or ```--limit qp_external_dev``` at the end of the commands to deploy using either the production or development vaults respectively
- Else use ```--limit prod``` or ```--limit dev``` at the end of the commands to deploy using either the production or development vaults respectively

### Recommended deployment order (kafka, mysql, frontend, rest-api, run-detection, qp_external)

The command below deploys everything apart from qp_external:

```bash
ansible-playbook autoreduce.yaml --tags autoreduce --vault-password-file ~/.vault_pass.txt --limit prod
```

This command deploys qp_external:

```bash
ansible-playbook autoreduce.yaml --tags qp_external --vault-password-file ~/.vault_pass.txt --limit qp_external_prod
```

### Other examples

Deploy all k8s-based services using the development vault

```bash
ansible-playbook autoreduce.yaml --tags autoreduce --vault-password-file ~/.vault_pass.txt --limit dev
```

Deploy only the webapp services (run frontend, mysql, rest-api - ignore all other tags)

```bash
ansible-playbook autoreduce.yaml --tags webapp --vault-password-file ~/.vault_pass.txt --limit prod
```

Deploy only the external queue-processor using the development vault

```bash
ansible-playbook autoreduce.yaml --tags qp_external --vault-password-file ~/.vault_pass.txt --limit qp_external_dev
```

Skip the run-detection when deploying autoreduction (run autoreduction-tagged tasks, ignoring run-detection)

```bash
ansible-playbook autoreduce.yaml --tags autoreduce --skip-tags run_detection --vault-password-file ~/.vault_pass.txt --limit prod
```
