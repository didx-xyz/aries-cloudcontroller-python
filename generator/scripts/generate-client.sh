#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/../" || exit

# Remove old generated code
rm -rf ../generated/

# Read ACA_PY_VERSION from input arg or default to 1.2.1-20250228
ACA_PY_VERSION=${1:-"1.2.1-20250228"}

export ACA_PY_VERSION # Set env for openapi-config-template'

echo "*** Generating client for ACA-Py version: ${ACA_PY_VERSION} ***"

# Generate config from template (with env var filled)
envsubst <openapi-config-template.yml >openapi-generator-config.yml

# Fetch spec, convert, and pre-process
./scripts/retrieve-openapi.sh
./scripts/convert-to-openapi3-local.sh
./scripts/process-openapi.sh

# Generate client
java -ea -server -Duser.timezone=UTC -jar "$(pwd)/../../openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar" generate -c ./openapi-generator-config.yml --skip-validate-spec

# Make automated changes to generated client
./scripts/postprocess-client.sh

# Copy
cd ..
cp -r ./generated/aries_cloudcontroller/ .

# autoflake again to remove newly unused imports
autoflake aries_cloudcontroller -i -r --remove-all-unused-imports --ignore-init-module-imports
# Black format and optimise imports
black aries_cloudcontroller
isort aries_cloudcontroller --profile black
