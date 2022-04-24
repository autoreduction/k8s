# Prerequisites

- Must have Kubernetes, Ansible, and Ansible-Galaxy installed in your Python environment
- Must have kubernetes.core installed ```ansible-galaxy collection install kubernetes.core```
- Deployment cluster should be specified in ~/.kube/config and set as the current context

## Example Deployment Commands

- Create a file at ~/.vault_pass.txt with the vault password
- Enter correct Python path for localhost in the inventory file

Deploy all the services (run all tasks, ignore tags)

```bash
ansible-playbook autoreduce.yaml --tags all --vault-password-file ~/.vault_pass.txt
```

Deploy only the webapp services (run frontend, mysql, rest-api - ignore all other tags)

```bash
ansible-playbook autoreduce.yaml --tags webapp --vault-password-file ~/.vault_pass.txt
```

Skip the queue-processor service (run all tasks, ignore queue-processor)

```bash
ansible-playbook autoreduce.yaml --skip-tags queue-processor --vault-password-file ~/.vault_pass.txt
```