# Generating the client

Currently to generate the client you need to use the DIDx fork of OpenAPI generator and build the JAR yourself.

```sh
# Clone projects
git clone https://github.com/didx-xyz/openapi-generator
git clone https://github.com/didx-xyz/aries-cloudcontroller-python

# Build openapi generator JAR
cd openapi-generator
git checkout feature/new-uplink-generator
mvn -B --no-snapshot-updates clean package -DskipTests=true -Dmaven.javadoc.skip=true -Djacoco.skip=true

# Generate client
cd aries-cloudcontroller-python
pip install -r requirements.txt
cd generator
./scripts/generate-client.sh
```

## Updating the OpenAPI

Updating the OpenAPI is only needed when a new version of ACA-Py is released. The process of updating the OpenAPI is mostly automated, you only need to run a few scripts. First determine the version you want for OpenAPI spec from the `hyperledger/aries-cloudagent-python` docker images (https://github.com/hyperledger/aries-cloudagent-python/blob/main/ContainerImagesAndGithubActions.md). Currently the default for the `retrieve-openapi.sh` script is "py3.9-0.9.0".

After that you can run the following commands to update the `data/openapi.yml` file. This file should be committed.

```sh
cd aries-cloudcontroller-python/generator

# Retrieve the open api file. Change `py3.9-0.9.0` if you want another version. See 
# <https://github.com/hyperledger/aries-cloudagent-python/blob/main/ContainerImagesAndGithubActions.md#tags> for tags
./scripts/retrieve-openapi.sh py3.9-0.9.0

# transform to OpenAPI V3
./scripts/convert-to-openapi3-local.sh

# If the transform script is not working (e.g. does't work on M1 macs), you can also use an online converter
# This will upload the content to the cloud however
# ./scripts/convert-to-openapi3-remote.sh

# Fix the openapi file (add missing operation ids from data/operation-id-map.yml)
./scripts/process-openapi.sh

# Apply manual patches to the openapi file
./scripts/apply-patch.sh
```

## Updating the patch file

1. Make changes to the OpenAPI file and then run:

```sh
cd aries-cloudcontroller-python/generator

./scripts/create-patch.sh
```
