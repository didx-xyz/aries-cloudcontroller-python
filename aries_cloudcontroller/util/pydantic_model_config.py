from pydantic import ConfigDict

DEFAULT_PYDANTIC_MODEL_CONFIG: ConfigDict = {
    "defer_build": True,
    "populate_by_name": True,
    "validate_assignment": True,
}
