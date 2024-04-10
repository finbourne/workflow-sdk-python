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

class FieldMapping(BaseModel):
    """
    Defines a single Field map  # noqa: E501
    """
    map_from: Optional[constr(strict=True, max_length=1024, min_length=1)] = Field(None, alias="mapFrom", description="The field to map from")
    set_to: Optional[Any] = Field(None, alias="setTo", description="The (constant) value to set")
    __properties = ["mapFrom", "setTo"]

    @validator('map_from')
    def map_from_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

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
    def from_json(cls, json_str: str) -> FieldMapping:
        """Create an instance of FieldMapping from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if map_from (nullable) is None
        # and __fields_set__ contains the field
        if self.map_from is None and "map_from" in self.__fields_set__:
            _dict['mapFrom'] = None

        # set to None if set_to (nullable) is None
        # and __fields_set__ contains the field
        if self.set_to is None and "set_to" in self.__fields_set__:
            _dict['setTo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FieldMapping:
        """Create an instance of FieldMapping from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FieldMapping.parse_obj(obj)

        _obj = FieldMapping.parse_obj({
            "map_from": obj.get("mapFrom"),
            "set_to": obj.get("setTo")
        })
        return _obj
