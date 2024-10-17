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
from pydantic.v1 import BaseModel, Field, StrictStr, constr

class ActionLogOrigin(BaseModel):
    """
    The Action Log Origin contains information about how the Action was created  # noqa: E501
    """
    task_id: Optional[StrictStr] = Field(None, alias="taskId", description="The Id of the Task that created this Action")
    request_id: constr(strict=True, min_length=1) = Field(..., alias="requestId", description="The request Id of the request that caused this Action to be triggered.  This could be the original request that caused a sequence of Actions that resulted in this Action")
    __properties = ["taskId", "requestId"]

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
    def from_json(cls, json_str: str) -> ActionLogOrigin:
        """Create an instance of ActionLogOrigin from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if task_id (nullable) is None
        # and __fields_set__ contains the field
        if self.task_id is None and "task_id" in self.__fields_set__:
            _dict['taskId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ActionLogOrigin:
        """Create an instance of ActionLogOrigin from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ActionLogOrigin.parse_obj(obj)

        _obj = ActionLogOrigin.parse_obj({
            "task_id": obj.get("taskId"),
            "request_id": obj.get("requestId")
        })
        return _obj