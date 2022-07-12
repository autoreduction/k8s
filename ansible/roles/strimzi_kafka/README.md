Strimzi
=========

Ansible role to deploy Strimzi, create a Kafka cluster, and a KafkaUser.

Requirements
------------

By default, creating a KafkaUser resource will generate a random SCRAM-SHA-256 password. The user_secret.yaml.j2 template file creates a Secret containing the password. The Strimzi UserOperator will use this password to create the KafkaUser.
