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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, conlist 
from lusid_workflow.models.resource_id import ResourceId
from lusid_workflow.models.task_instance_field import TaskInstanceField

class CreateTaskRequest(BaseModel):
    """
    Contains required info to create a new Task  # noqa: E501
    """
    task_definition_id: ResourceId = Field(..., alias="taskDefinitionId")
    correlation_ids: Optional[conlist(StrictStr)] = Field(None, alias="correlationIds", description="A set of guid identifiers that allow correlation across the application tier")
    fields: Optional[conlist(TaskInstanceField)] = Field(None, description="Fields and their initial values - should correspond with the Task Definition field schema")
    stacking_key:  Optional[StrictStr] = Field(None,alias="stackingKey", description="The key for the Stack that this Task should be added to") 
    __properties = ["taskDefinitionId", "correlationIds", "fields", "stackingKey"]

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
    def from_json(cls, json_str: str) -> CreateTaskRequest:
        """Create an instance of CreateTaskRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of task_definition_id
        if self.task_definition_id:
            _dict['taskDefinitionId'] = self.task_definition_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item in self.fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fields'] = _items
        # set to None if correlation_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.correlation_ids is None and "correlation_ids" in self.__fields_set__:
            _dict['correlationIds'] = None

        # set to None if fields (nullable) is None
        # and __fields_set__ contains the field
        if self.fields is None and "fields" in self.__fields_set__:
            _dict['fields'] = None

        # set to None if stacking_key (nullable) is None
        # and __fields_set__ contains the field
        if self.stacking_key is None and "stacking_key" in self.__fields_set__:
            _dict['stackingKey'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateTaskRequest:
        """Create an instance of CreateTaskRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateTaskRequest.parse_obj(obj)

        _obj = CreateTaskRequest.parse_obj({
            "task_definition_id": ResourceId.from_dict(obj.get("taskDefinitionId")) if obj.get("taskDefinitionId") is not None else None,
            "correlation_ids": obj.get("correlationIds"),
            "fields": [TaskInstanceField.from_dict(_item) for _item in obj.get("fields")] if obj.get("fields") is not None else None,
            "stacking_key": obj.get("stackingKey")
        })
        return _obj
