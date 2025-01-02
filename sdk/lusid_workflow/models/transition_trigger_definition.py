# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator
from lusid_workflow.models.trigger_schema import TriggerSchema

class TransitionTriggerDefinition(BaseModel):
    """
    State changes happen in response to Triggers  # noqa: E501
    """
    name: constr(strict=True, max_length=1024, min_length=1) = Field(..., description="The key/Name of this Trigger")
    trigger: TriggerSchema = Field(...)
    __properties = ["name", "trigger"]

    @validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TransitionTriggerDefinition:
        """Create an instance of TransitionTriggerDefinition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of trigger
        if self.trigger:
            _dict['trigger'] = self.trigger.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransitionTriggerDefinition:
        """Create an instance of TransitionTriggerDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransitionTriggerDefinition.parse_obj(obj)

        _obj = TransitionTriggerDefinition.parse_obj({
            "name": obj.get("name"),
            "trigger": TriggerSchema.from_dict(obj.get("trigger")) if obj.get("trigger") is not None else None
        })
        return _obj
