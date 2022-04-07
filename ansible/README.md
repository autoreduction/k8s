# Prerequisites

- Must have Kubernetes, Ansible, and Ansible-Galaxy installed in your Python environment
- Must have kubernetes.core installed ```ansible-galaxy collection install kubernetes.core```

## Example frontend deployment

- Add either prod vault or dev vault password to ~/.vault_pass.txt
- Make sure either prod or dev vault is in group_vars/all

```bash
ansible-playbook playbooks/frontend/deploy.yaml -K --vault-password-file ~/.vault_pass.txt
```
