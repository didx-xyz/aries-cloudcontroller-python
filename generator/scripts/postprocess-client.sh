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

# Fix var_json field in attach_decorator_data.py (Union[str, Any] -> Union[Dict[str, Any], List[Dict[str, Any]]])
sed -i 's/var_json: Optional\[Union\[str, Any\]\] = Field(/var_json: Optional\[Union\[Dict\[str, Any\], List\[Dict\[str, Any\]\]\]\] = Field(/g' aries_cloudcontroller/models/attach_decorator_data.py

# Fix types in filter.py model to accommodate custom schema in ACA-Py (replace `Optional[Union[str, Any]]` with `Optional[Union[str, int, float]]`
sed -i 's/\[Union\[str, Any\]/\[Union\[str, int, float\]/g' aries_cloudcontroller/models/filter.py

# Fix types in credential.py: "Any" type in context and issuer fields, should be a dict
sed -i -e 's/context: List\[Union\[str, Any\]\]/context: List\[Union\[str, Dict\]\]/g' \
    -e 's/issuer: Union\[str, Any\]/issuer: Union\[str, Dict\[str, Any\]\]/g' \
    aries_cloudcontroller/models/credential.py

# Fix type in invitation_message.py: "Any" type in services should be a dict
sed -i 's/services: Optional\[List\[Union\[str, Any\]\]\]/services: Optional\[List\[Union\[str, Dict\]\]\]/g' aries_cloudcontroller/models/invitation_message.py

# Relax the model validation in verify_request (replace SignedDoc with a generic Dict[str, Any]):
sed -i 's/doc: SignedDoc/doc: Dict[str, Any]/' aries_cloudcontroller/models/verify_request.py
# Remove block of code associated with this previous change:
sed -i '/# override the default output from pydantic by calling `to_dict()` of doc/,/self.doc.to_dict()/d' aries_cloudcontroller/models/verify_request.py

# NB:
# There are 3 more models, and 1 API Module, that we are not amending automatically. These should be reviewed manually:
# - MultitenancyAPI has custom method to handle our groups plugin!
# Models:
# - credential_definition.py: `type`, for now, must be Literal["CL"]
# - did.py: key_type, method, and posture each have literals. NB: Also: the validator: `verkey_validate_regular_expression` must include BBS_PATTERN regex

# Additionally, the API Client we modify so that query_params are converted from bool to str, before being submitted to ACA-Py
# This change impacts multiple lines, calling `sanitize_for_serialization`
