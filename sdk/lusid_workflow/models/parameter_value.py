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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, constr, validator 

class ParameterValue(BaseModel):
    """
    Defines a Parameter Value  # noqa: E501
    """
    name:  StrictStr = Field(...,alias="name", description="Name") 
    value: Optional[Any] = Field(None, description="Value which can be a String, Boolean, Decimal or DateTime (ISO 8601)")
    __properties = ["name", "value"]

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
    def from_json(cls, json_str: str) -> ParameterValue:
        """Create an instance of ParameterValue from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if value (nullable) is None
        # and __fields_set__ contains the field
        if self.value is None and "value" in self.__fields_set__:
            _dict['value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParameterValue:
        """Create an instance of ParameterValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ParameterValue.parse_obj(obj)

        _obj = ParameterValue.parse_obj({
            "name": obj.get("name"),
            "value": obj.get("value")
        })
        return _obj
