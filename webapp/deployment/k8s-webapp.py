"""
Manage objects in a declarative way and operate on object configuration files
(stored locally along the Python code source) like we usually do with the kubectl command.

Python code should only be a simple execution backend to trigger Kubernetes operations,
and business logic, so to speak, should be concentrated in manifest files.

Creates a Kubernetes deployment from a manifest file.
"""
import os
import logging
import yaml
from kubernetes import client, config, utils

logging.basicConfig(level=logging.INFO)


# https://dev.to/stack-labs/my-journey-with-spark-on-kubernetes-in-python-3-3-536e
def main():
    """
    Create a Kubernetes deployment from a manifest file.
    This is the equivalent in Python of kubectl create -f deployment.yaml.
    """

    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()

    with open(os.path.join(os.path.dirname(__file__), "deployment.yaml"),
              encoding="utf-8") as deployment_file:
        dep = yaml.safe_load(deployment_file)
        k8s_client = client.ApiClient()
        resp = utils.create_from_dict(k8s_client, dep)
        logging.info("Deployment created. status=%s", resp[0].metadata.name)


if __name__ == '__main__':
    main()
