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

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field 

class TaskDefinitionVersion(BaseModel):
    """
    The version of the Task Definition used by this Task  # noqa: E501
    """
    as_at_modified: Optional[datetime] = Field(None, alias="asAtModified", description="The asAt datetime of the Task Definition used by this Task")
    __properties = ["asAtModified"]

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
    def from_json(cls, json_str: str) -> TaskDefinitionVersion:
        """Create an instance of TaskDefinitionVersion from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaskDefinitionVersion:
        """Create an instance of TaskDefinitionVersion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TaskDefinitionVersion.parse_obj(obj)

        _obj = TaskDefinitionVersion.parse_obj({
            "as_at_modified": obj.get("asAtModified")
        })
        return _obj
