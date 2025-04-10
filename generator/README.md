# Generating the client

Currently to generate the client you need to use the DIDx fork of OpenAPI generator and build the JAR yourself.

## Prerequisites

```sh
# Clone projects
git clone https://github.com/didx-xyz/aries-cloudcontroller-python

git clone https://github.com/OpenAPITools/openapi-generator

# Build OpenAPI generator JAR
cd openapi-generator
git checkout v7.9.0  # A tag of the openapi-generator version used to generate cloudcontroller

mvn -B --no-snapshot-updates clean package -DskipTests=true -Dmaven.javadoc.skip=true -Djacoco.skip=true
```

## Generate the CloudController client

```sh
cd aries-cloudcontroller-python
pip install -r requirements.txt -r requirements.dev.txt --upgrade

./generator/scripts/generate-client.sh 1.1.0 # Or other ACA-Py version
```
