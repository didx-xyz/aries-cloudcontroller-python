import pydantic
import pytest

from aries_cloudcontroller.models import AttachDecoratorData

# Sample AttachDecoratorData with dict type var_json
sample_attach_decorator_dict = {
    "json": {"key": "value", "another_key": "another_value"}
}

# Sample AttachDecoratorData with list of dict type var_json
sample_attach_decorator_list = {"json": [{"key": "value"}, {"list_key": "list_value"}]}

# Invalid AttachDecoratorData where var_json is neither dict nor list of dict
invalid_attach_decorator = {"json": "This is a string which should be invalid"}


# The `json` field in AttachDecoratorData has a custom Marshmallow field definition in ACA-Py,
# called `DictOrDictListField`, intended to only accept a Dict or a list of Dict.
# The auto-generated models requires a manual change, so this test asserts the expected behavior
def test_valid_dict():
    model = AttachDecoratorData(**sample_attach_decorator_dict)
    assert model.var_json == sample_attach_decorator_dict["json"]


def test_valid_list():
    model = AttachDecoratorData(**sample_attach_decorator_list)
    assert model.var_json == sample_attach_decorator_list["json"]


def test_invalid():
    with pytest.raises(pydantic.ValidationError):
        AttachDecoratorData(**invalid_attach_decorator)
