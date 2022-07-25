# Prerequisites

- Must have Kubernetes, Helm, Ansible, and Ansible-Galaxy installed in your Python environment
- Install the ansible-galaxy requirements with ```ansible-galaxy install -r requirements.yaml```
- Deployment cluster should be specified in ~/.kube/config and set as the current context
- Set the Image tag you wish to deploy in group_vars

## Example Deployment Commands

- Create a file at ~/.vault_pass.txt with the vault password
- Enter correct Python path for localhost in the inventory file
- Use ```--limit prod``` or ```--limit prod-web``` at the end of the commands to deploy using either the production or development vaults respectively

Deploy all the services (run all tasks, ignore tags)

```bash
ansible-playbook autoreduce.yaml --tags all --vault-password-file ~/.vault_pass.txt --limit prod
```

Deploy all the services using the development vault

```bash
ansible-playbook autoreduce.yaml --tags all --vault-password-file ~/.vault_pass.txt --limit dev
```

Deploy only the webapp services (run frontend, mysql, rest-api - ignore all other tags)

```bash
ansible-playbook autoreduce.yaml --tags webapp --vault-password-file ~/.vault_pass.txt --limit prod
```

Skip the queue-processor service (run all tasks, ignore queue-processor)

```bash
ansible-playbook autoreduce.yaml --skip-tags queue_processor --vault-password-file ~/.vault_pass.txt --limit prod
```
