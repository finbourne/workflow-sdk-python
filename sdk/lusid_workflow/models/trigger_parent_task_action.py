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

class TriggerParentTaskAction(BaseModel):
    """
    Defines a Trigger Parent Task Action  # noqa: E501
    """
    type: constr(strict=True, min_length=1) = Field(..., description="Type name for this Action")
    trigger: constr(strict=True, max_length=1024, min_length=1) = Field(..., description="Trigger on parent task to be invoked")
    __properties = ["type", "trigger"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('TriggerParentTask'):
            raise ValueError("must be one of enum values ('TriggerParentTask')")
        return value

    @validator('trigger')
    def trigger_validate_regular_expression(cls, value):
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
    def from_json(cls, json_str: str) -> TriggerParentTaskAction:
        """Create an instance of TriggerParentTaskAction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TriggerParentTaskAction:
        """Create an instance of TriggerParentTaskAction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TriggerParentTaskAction.parse_obj(obj)

        _obj = TriggerParentTaskAction.parse_obj({
            "type": obj.get("type"),
            "trigger": obj.get("trigger")
        })
        return _obj
