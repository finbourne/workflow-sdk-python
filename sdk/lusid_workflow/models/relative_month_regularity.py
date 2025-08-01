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


from typing import Any, Dict, List
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, conint, conlist, constr 

class RelativeMonthRegularity(BaseModel):
    """
    Relative Month Regularity  # noqa: E501
    """
    frequency: conint(strict=True) = Field(..., description="The frequency of the Relative Month Regularity")
    days_of_week: conlist(StrictStr) = Field(..., alias="daysOfWeek", description="Days of the week")
    index:  StrictStr = Field(...,alias="index", description="Relative index in the month") 
    type:  StrictStr = Field(...,alias="type", description="The type of Date Regularity") 
    __properties = ["frequency", "daysOfWeek", "index", "type"]

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
    def from_json(cls, json_str: str) -> RelativeMonthRegularity:
        """Create an instance of RelativeMonthRegularity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RelativeMonthRegularity:
        """Create an instance of RelativeMonthRegularity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RelativeMonthRegularity.parse_obj(obj)

        _obj = RelativeMonthRegularity.parse_obj({
            "frequency": obj.get("frequency"),
            "days_of_week": obj.get("daysOfWeek"),
            "index": obj.get("index"),
            "type": obj.get("type")
        })
        return _obj
