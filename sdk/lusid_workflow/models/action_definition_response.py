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
from pydantic import BaseModel, Field, StrictStr
from lusid_workflow.models.action_details_response import ActionDetailsResponse

class ActionDefinitionResponse(BaseModel):
    """
    Defines the Actions for a Task in a read-only form  # noqa: E501
    """
    name: Optional[StrictStr] = Field(None, description="The Name of this Action")
    run_as_user_id: Optional[StrictStr] = Field(None, alias="runAsUserId", description="The ID of the user that this action will be performed by. If not specified, the actions will be performed by the \"current user\".")
    action_details: Optional[ActionDetailsResponse] = Field(None, alias="actionDetails")
    __properties = ["name", "runAsUserId", "actionDetails"]

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
    def from_json(cls, json_str: str) -> ActionDefinitionResponse:
        """Create an instance of ActionDefinitionResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of action_details
        if self.action_details:
            _dict['actionDetails'] = self.action_details.to_dict()
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if run_as_user_id (nullable) is None
        # and __fields_set__ contains the field
        if self.run_as_user_id is None and "run_as_user_id" in self.__fields_set__:
            _dict['runAsUserId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ActionDefinitionResponse:
        """Create an instance of ActionDefinitionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ActionDefinitionResponse.parse_obj(obj)

        _obj = ActionDefinitionResponse.parse_obj({
            "name": obj.get("name"),
            "run_as_user_id": obj.get("runAsUserId"),
            "action_details": ActionDetailsResponse.from_dict(obj.get("actionDetails")) if obj.get("actionDetails") is not None else None
        })
        return _obj
