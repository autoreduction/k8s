# Queue Processor (External)

This role deploys the queue processor as a Docker container to a remote host.

## VM allocation

- Login to the [OpenStack dashboard](https://openstack.stfc.ac.uk/)
- Select *Launch Instance*
- *Details*
  - *Instance Name* = `qp-external`
- *Source* = *ubuntu-focal-20.04-nogui*
- *Flavour* = *c3.large*
- *Key pair*
  - Ensure the public key associated with you in [users.yaml](../../group_vars/all/users.yaml) is added
- Select *Launch Instance*

## Additional Information

- To run as the isisautoreduce user, SSH into the VM with your FED ID and then run the following command:
  ```sudo su - isisautoreduce```
