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
from pydantic import BaseModel, Field, constr, validator

class LuminesceView(BaseModel):
    """
    Configuration for a Worker that calls a Luminesce view  # noqa: E501
    """
    type: constr(strict=True, min_length=1) = Field(..., description="The type of worker")
    name: constr(strict=True, max_length=512, min_length=1) = Field(..., description="Name of the view in Luminesce")
    __properties = ["type", "name"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('LuminesceView'):
            raise ValueError("must be one of enum values ('LuminesceView')")
        return value

    @validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
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
    def from_json(cls, json_str: str) -> LuminesceView:
        """Create an instance of LuminesceView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LuminesceView:
        """Create an instance of LuminesceView from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LuminesceView.parse_obj(obj)

        _obj = LuminesceView.parse_obj({
            "type": obj.get("type"),
            "name": obj.get("name")
        })
        return _obj
