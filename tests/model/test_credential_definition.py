import pydantic
import pytest

from aries_cloudcontroller.models import CredentialDefinition

# Sample data for CredentialDefinition where type is "CL". Other fields optional
valid_credential_definition = {"type": "CL"}

# Sample data for CredentialDefinition where type is not "CL"
invalid_credential_definition_1 = {"type": "SomeOtherType"}

invalid_credential_definition_2 = {"type": 123}


def test_valid_credential_definition():
    """Test a valid CredentialDefinition model."""
    model = CredentialDefinition(**valid_credential_definition)
    assert model.type == "CL"


def test_invalid_credential_definition_1():
    """Test an invalid CredentialDefinition model with an incorrect type value."""
    with pytest.raises(pydantic.ValidationError):
        CredentialDefinition(**invalid_credential_definition_1)


def test_invalid_credential_definition_2():
    """Test an invalid CredentialDefinition model with an incorrect type type."""
    with pytest.raises(pydantic.ValidationError):
        CredentialDefinition(**invalid_credential_definition_2)
