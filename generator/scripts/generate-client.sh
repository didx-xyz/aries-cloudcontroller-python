#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/../" || exit

# Remove old generated code
rm -rf ../generated/

# Generated client
java -ea -server -Duser.timezone=UTC -jar "$(pwd)/../../openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar" generate -c ./openapi-generator-config.yml --skip-validate-spec

# Copy
cd ..
cp -r ./generated/aries_cloudcontroller/ .

# Remove `# noqa: F401` comment indicating to ignore unused imports
find aries_cloudcontroller -type f -name '*.py' | xargs sed -i 's/# noqa: F401//'

# autoflake to remove unused imports
autoflake aries_cloudcontroller -i -r --remove-all-unused-imports --exclude=__init__.py

# Black format and optimise imports
black aries_cloudcontroller
isort aries_cloudcontroller --profile black

# Apply the patches required
# cd ..

# echo -e "\nApplying patch"
# git apply --verbose generator/data/__init__.patch || {
#     # git apply failed! Warn the user
#     echo -e "$(tput setaf 1)\n\nFailed to apply patch. Client generation INCOMPLETE!\n\nPlease, ensure to fix this before proceeding.\nTake care when committing unpatched code.\n\n"
#     exit 1
# }
# black .
# isort . --profile black
