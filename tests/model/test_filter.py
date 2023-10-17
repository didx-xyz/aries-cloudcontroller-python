import pydantic
import pytest

from aries_cloudcontroller.models import Filter

# Sample data for Filter. These have custom types in ACA-Py. They can be str, int, or float
valid_filter_data_str = {
    "const": "someValue",
    "enum": ["value1"],
    "exclusive_maximum": "maximumValue",
    "exclusive_minimum": "10",
    "minimum": "5",
    "maximum": "50.5",
}

valid_filter_data_int = {
    "const": 1,
    "enum": [2],
    "exclusive_maximum": 3,
    "exclusive_minimum": 4,
    "minimum": 5,
    "maximum": 6,
}

valid_filter_data_float = {
    "const": 1.5,
    "enum": [2.5],
    "exclusive_maximum": 3.5,
    "exclusive_minimum": 4.5,
    "minimum": 5.5,
    "maximum": 6.5,
}

# Sample data for Filter where each field is incorrectly filled
invalid_filter_data = {
    "const": [12345],  # should be a str, int, or float, not a list
    "enum": ["value1", [123], {"key": "value"}],  # list contains dict
    "exclusive_maximum": {"key": "value"},  # should be a str, int, or float
    "exclusive_minimum": {"key": "value"},  # should be a str, int, or float
    "maximum": {"key": "value"},  # should be a str, int, or float
    "minimum": {"key": "value"},  # should be a str, int, or float
}


def test_valid_filter_str():
    """Test a valid Filter model with str fields."""
    model = Filter(**valid_filter_data_str)
    assert model.const == valid_filter_data_str["const"]
    assert model.enum == valid_filter_data_str["enum"]
    assert model.exclusive_maximum == valid_filter_data_str["exclusive_maximum"]
    assert model.exclusive_minimum == valid_filter_data_str["exclusive_minimum"]
    assert model.maximum == valid_filter_data_str["maximum"]
    assert model.minimum == valid_filter_data_str["minimum"]


def test_valid_filter_int():
    """Test a valid Filter model with int fields."""
    model = Filter(**valid_filter_data_int)
    assert model.const == valid_filter_data_int["const"]
    assert model.enum == valid_filter_data_int["enum"]
    assert model.exclusive_maximum == valid_filter_data_int["exclusive_maximum"]
    assert model.exclusive_minimum == valid_filter_data_int["exclusive_minimum"]
    assert model.maximum == valid_filter_data_int["maximum"]
    assert model.minimum == valid_filter_data_int["minimum"]


def test_valid_filter_float():
    """Test a valid Filter model with float fields."""
    model = Filter(**valid_filter_data_float)
    assert model.const == valid_filter_data_float["const"]
    assert model.enum == valid_filter_data_float["enum"]
    assert model.exclusive_maximum == valid_filter_data_float["exclusive_maximum"]
    assert model.exclusive_minimum == valid_filter_data_float["exclusive_minimum"]
    assert model.maximum == valid_filter_data_float["maximum"]
    assert model.minimum == valid_filter_data_float["minimum"]


def test_invalid_filter():
    """Test an invalid Filter model."""
    for key, value in invalid_filter_data.items():
        with pytest.raises(pydantic.ValidationError):
            Filter(**{key: value})
