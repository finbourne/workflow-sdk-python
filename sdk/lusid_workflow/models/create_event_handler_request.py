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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, constr 
from lusid_workflow.models.event_handler_mapping import EventHandlerMapping
from lusid_workflow.models.event_matching_pattern import EventMatchingPattern
from lusid_workflow.models.resource_id import ResourceId
from lusid_workflow.models.task_activity import TaskActivity

class CreateEventHandlerRequest(BaseModel):
    """
    Contains information for creating an Event Handler  # noqa: E501
    """
    id: ResourceId = Field(...)
    display_name:  StrictStr = Field(...,alias="displayName", description="Human readable name") 
    description:  Optional[StrictStr] = Field(None,alias="description", description="Human readable description") 
    status:  StrictStr = Field(...,alias="status", description="The current status of the event handler") 
    event_matching_pattern: EventMatchingPattern = Field(..., alias="eventMatchingPattern")
    run_as_user_id: EventHandlerMapping = Field(..., alias="runAsUserId")
    task_definition_id: ResourceId = Field(..., alias="taskDefinitionId")
    task_definition_as_at: Optional[datetime] = Field(None, alias="taskDefinitionAsAt", description="AsAt of the required task definition")
    task_activity: TaskActivity = Field(..., alias="taskActivity")
    __properties = ["id", "displayName", "description", "status", "eventMatchingPattern", "runAsUserId", "taskDefinitionId", "taskDefinitionAsAt", "taskActivity"]

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
    def from_json(cls, json_str: str) -> CreateEventHandlerRequest:
        """Create an instance of CreateEventHandlerRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of event_matching_pattern
        if self.event_matching_pattern:
            _dict['eventMatchingPattern'] = self.event_matching_pattern.to_dict()
        # override the default output from pydantic by calling `to_dict()` of run_as_user_id
        if self.run_as_user_id:
            _dict['runAsUserId'] = self.run_as_user_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of task_definition_id
        if self.task_definition_id:
            _dict['taskDefinitionId'] = self.task_definition_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of task_activity
        if self.task_activity:
            _dict['taskActivity'] = self.task_activity.to_dict()
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if task_definition_as_at (nullable) is None
        # and __fields_set__ contains the field
        if self.task_definition_as_at is None and "task_definition_as_at" in self.__fields_set__:
            _dict['taskDefinitionAsAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateEventHandlerRequest:
        """Create an instance of CreateEventHandlerRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateEventHandlerRequest.parse_obj(obj)

        _obj = CreateEventHandlerRequest.parse_obj({
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "status": obj.get("status"),
            "event_matching_pattern": EventMatchingPattern.from_dict(obj.get("eventMatchingPattern")) if obj.get("eventMatchingPattern") is not None else None,
            "run_as_user_id": EventHandlerMapping.from_dict(obj.get("runAsUserId")) if obj.get("runAsUserId") is not None else None,
            "task_definition_id": ResourceId.from_dict(obj.get("taskDefinitionId")) if obj.get("taskDefinitionId") is not None else None,
            "task_definition_as_at": obj.get("taskDefinitionAsAt"),
            "task_activity": TaskActivity.from_dict(obj.get("taskActivity")) if obj.get("taskActivity") is not None else None
        })
        return _obj
