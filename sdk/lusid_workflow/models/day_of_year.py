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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, conint 

class DayOfYear(BaseModel):
    """
    A day in the year  # noqa: E501
    """
    month: conint(strict=True) = Field(..., description="Month in the year")
    day: conint(strict=True) = Field(..., description="Day in the month")
    __properties = ["month", "day"]

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
    def from_json(cls, json_str: str) -> DayOfYear:
        """Create an instance of DayOfYear from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DayOfYear:
        """Create an instance of DayOfYear from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DayOfYear.parse_obj(obj)

        _obj = DayOfYear.parse_obj({
            "month": obj.get("month"),
            "day": obj.get("day")
        })
        return _obj
