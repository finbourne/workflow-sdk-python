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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, constr 
from lusid_workflow.models.resource_id import ResourceId
from lusid_workflow.models.task_definition_version import TaskDefinitionVersion

class TaskSummary(BaseModel):
    """
    Summary of a Task created based on a Task Definition  # noqa: E501
    """
    id:  StrictStr = Field(...,alias="id", description="The unique id for this Task") 
    task_definition_id: ResourceId = Field(..., alias="taskDefinitionId")
    task_definition_version: TaskDefinitionVersion = Field(..., alias="taskDefinitionVersion")
    task_definition_display_name:  StrictStr = Field(...,alias="taskDefinitionDisplayName", description="The display name of the Task Definition used by this Task") 
    state:  StrictStr = Field(...,alias="state", description="Current State") 
    __properties = ["id", "taskDefinitionId", "taskDefinitionVersion", "taskDefinitionDisplayName", "state"]

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
    def from_json(cls, json_str: str) -> TaskSummary:
        """Create an instance of TaskSummary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of task_definition_version
        if self.task_definition_version:
            _dict['taskDefinitionVersion'] = self.task_definition_version.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaskSummary:
        """Create an instance of TaskSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TaskSummary.parse_obj(obj)

        _obj = TaskSummary.parse_obj({
            "id": obj.get("id"),
            "task_definition_id": ResourceId.from_dict(obj.get("taskDefinitionId")) if obj.get("taskDefinitionId") is not None else None,
            "task_definition_version": TaskDefinitionVersion.from_dict(obj.get("taskDefinitionVersion")) if obj.get("taskDefinitionVersion") is not None else None,
            "task_definition_display_name": obj.get("taskDefinitionDisplayName"),
            "state": obj.get("state")
        })
        return _obj
