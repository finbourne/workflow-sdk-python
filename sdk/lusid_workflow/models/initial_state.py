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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, constr, validator

class InitialState(BaseModel):
    """
    Defines the Initial State of the Task  # noqa: E501
    """
    name: constr(strict=True, max_length=1024, min_length=1) = Field(..., description="The Initial State of the Task")
    required_fields: Optional[conlist(StrictStr)] = Field(None, alias="requiredFields", description="Required input Fields for the Initial State")
    __properties = ["name", "requiredFields"]

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
    def from_json(cls, json_str: str) -> InitialState:
        """Create an instance of InitialState from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if required_fields (nullable) is None
        # and __fields_set__ contains the field
        if self.required_fields is None and "required_fields" in self.__fields_set__:
            _dict['requiredFields'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InitialState:
        """Create an instance of InitialState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InitialState.parse_obj(obj)

        _obj = InitialState.parse_obj({
            "name": obj.get("name"),
            "required_fields": obj.get("requiredFields")
        })
        return _obj
