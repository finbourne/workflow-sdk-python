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


from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator
from lusid_workflow.models.read_only_states import ReadOnlyStates
from lusid_workflow.models.value_constraints import ValueConstraints

class TaskFieldDefinition(BaseModel):
    """
    Defines a Task Definition Field  # noqa: E501
    """
    name: constr(strict=True, max_length=1024, min_length=1) = Field(..., description="The name of this Field")
    type: constr(strict=True, min_length=1) = Field(..., description="The value type for the field. Available values are: \"String\", \"Decimal\", \"DateTime\", \"Boolean\")")
    read_only_states: Optional[ReadOnlyStates] = Field(None, alias="readOnlyStates")
    value_constraints: Optional[ValueConstraints] = Field(None, alias="valueConstraints")
    __properties = ["name", "type", "readOnlyStates", "valueConstraints"]

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

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TaskFieldDefinition:
        """Create an instance of TaskFieldDefinition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of read_only_states
        if self.read_only_states:
            _dict['readOnlyStates'] = self.read_only_states.to_dict()
        # override the default output from pydantic by calling `to_dict()` of value_constraints
        if self.value_constraints:
            _dict['valueConstraints'] = self.value_constraints.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaskFieldDefinition:
        """Create an instance of TaskFieldDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TaskFieldDefinition.parse_obj(obj)

        _obj = TaskFieldDefinition.parse_obj({
            "name": obj.get("name"),
            "type": obj.get("type"),
            "read_only_states": ReadOnlyStates.from_dict(obj.get("readOnlyStates")) if obj.get("readOnlyStates") is not None else None,
            "value_constraints": ValueConstraints.from_dict(obj.get("valueConstraints")) if obj.get("valueConstraints") is not None else None
        })
        return _obj
