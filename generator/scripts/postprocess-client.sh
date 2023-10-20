#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/../../generated/" || exit # Move to /generated folder

# Remove `# noqa: F401` comment indicating to ignore unused imports, for autoflake
find aries_cloudcontroller -type f -name '*.py' | xargs sed -i 's/# noqa: F401//'

# autoflake to remove unused imports
autoflake aries_cloudcontroller -i -r --remove-all-unused-imports --ignore-init-module-imports

# Cleanup generated models
for file in aries_cloudcontroller/models/*.py; do
    # Replace the model config with DEFAULT_PYDANTIC_MODEL_CONFIG
    sed -i '/model_config = {/,/}/c\    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG' "$file"

    # Add import statement for this default config, and re-add ClassVar, List imports, as autoflake mistakenly removes them
    sed -i '/try:$/N;/try:\n    from typing import Self/i \
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG\
from typing import ClassVar, List' "$file"

    # Replace the TODO lines
    sed -i '/# TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead/N; s/# TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead\n        return json.dumps(self.to_dict())/return self.model_dump_json(by_alias=True, exclude_unset=True)/' "$file"

    # Fix autogeneration of very long number
    sed -i 's/Field(le=-1,/Field(le=18446744073709551615,/g' "$file"
done

# Deduplication for __init__.py -- just helps get SonarCloud duplication report to be under threshold!
sed -i -E 's/from aries_cloudcontroller\.(\w+)\.\w+ /from aries_cloudcontroller.\1 /g' aries_cloudcontroller/__init__.py

# Append custom models to our init file:
{
    echo "from aries_cloudcontroller.models.wallet_list_with_groups import WalletListWithGroups"
    echo "from aries_cloudcontroller.models.wallet_record_with_groups import WalletRecordWithGroups"
} >>aries_cloudcontroller/models/__init__.py
{
    echo "from aries_cloudcontroller.acapy_client import AcaPyClient"
    echo "from aries_cloudcontroller.models import WalletListWithGroups, WalletRecordWithGroups"
    echo "from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG"
} >>aries_cloudcontroller/__init__.py

# Fix timestamp

# Black format and optimise imports
black aries_cloudcontroller
isort aries_cloudcontroller --profile black
