from typing import Union

from pydantic import BaseModel

from aries_cloudcontroller.model.invitation_message import InvitationMessage
from aries_cloudcontroller.util.pydantic_converter import (
    PydanticConverter,
    _PydanticRequestBody,
    _PydanticResponseBody,
)
from tests.model.test_invitation import sample_invitation_message
from tests.util.compare_dicts import equal_dicts


class SampleModel(BaseModel):
    name: str
    age: int


class SampleUnionModel(BaseModel):
    union_field: Union[str, int]


def test_create_request_body_converter():
    converter = PydanticConverter()
    result = converter.create_request_body_converter(SampleModel)
    assert isinstance(result, _PydanticRequestBody)


def test_create_response_body_converter():
    converter = PydanticConverter()
    result = converter.create_response_body_converter(SampleModel)
    assert isinstance(result, _PydanticResponseBody)


def test_create_request_body_converter_with_union_type():
    converter = PydanticConverter()
    result = converter.create_request_body_converter(SampleUnionModel)
    assert isinstance(result, _PydanticRequestBody)


def test_create_response_body_converter_with_union_type():
    converter = PydanticConverter()
    result = converter.create_response_body_converter(SampleUnionModel)
    assert isinstance(result, _PydanticResponseBody)


def test_pydantic_request_body_convert():
    converter = _PydanticRequestBody(SampleModel)
    model_instance = SampleModel(name="Test", age=20)
    result = converter.convert(model_instance)
    assert result == model_instance.dict()


def test_pydantic_response_body_convert(mocker):
    # Mock a response object
    response = mocker.Mock()
    response.json.return_value = {"name": "Test", "age": 20}

    converter = _PydanticResponseBody(SampleModel)
    result = converter.convert(response)

    # Create a SampleModel instance for comparison
    model_instance = SampleModel(name="Test", age=20)

    assert result == model_instance


def test_invitation_message_request():
    # Create an instance of the InvitationMessage model
    invitation_message = InvitationMessage(**sample_invitation_message)

    converter = _PydanticRequestBody(InvitationMessage)

    # Use the converter to convert the InvitationMessage to a dictionary
    invitation_dict = converter.convert(invitation_message)

    # Assert that the converted dictionary matches the original sample_invitation_message
    assert equal_dicts(sample_invitation_message, invitation_dict)


def test_invitation_message_response(mocker):
    # Simulate a response that contains the sample_invitation_message
    response = mocker.Mock()
    response.json.return_value = sample_invitation_message

    converter = _PydanticResponseBody(InvitationMessage)

    # Use the converter to convert the response to an InvitationMessage
    invitation_message = converter.convert(response)

    # Assert that the converted message matches the original sample_invitation_message
    assert equal_dicts(
        sample_invitation_message, invitation_message.dict(by_alias=True)
    )
