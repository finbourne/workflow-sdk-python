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
from pydantic.v1 import BaseModel, Field, conlist, constr

class ValueConstraints(BaseModel):
    """
    Constraints that should be applied to a Tasks fields  # noqa: E501
    """
    constraint_type: constr(strict=True, min_length=1) = Field(..., alias="constraintType", description="Whether the constraint is a suggestion or should be enforced via validation (e.g. Suggested, Validated)")
    value_source_type: constr(strict=True, min_length=1) = Field(..., alias="valueSourceType", description="The source of the acceptable values (e.g. AcceptableValues)")
    acceptable_values: conlist(Any) = Field(..., alias="acceptableValues", description="The acceptable values for the field")
    __properties = ["constraintType", "valueSourceType", "acceptableValues"]

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
    def from_json(cls, json_str: str) -> ValueConstraints:
        """Create an instance of ValueConstraints from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ValueConstraints:
        """Create an instance of ValueConstraints from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ValueConstraints.parse_obj(obj)

        _obj = ValueConstraints.parse_obj({
            "constraint_type": obj.get("constraintType"),
            "value_source_type": obj.get("valueSourceType"),
            "acceptable_values": obj.get("acceptableValues")
        })
        return _obj
