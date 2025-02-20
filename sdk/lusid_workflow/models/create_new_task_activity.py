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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, conlist, constr, validator 
from lusid_workflow.models.event_handler_mapping import EventHandlerMapping
from lusid_workflow.models.field_mapping import FieldMapping

class CreateNewTaskActivity(BaseModel):
    """
    Define a Task Activity that creates a new task  # noqa: E501
    """
    initial_trigger:  Optional[StrictStr] = Field(None,alias="initialTrigger", description="Trigger to supply to all tasks to be made") 
    type:  StrictStr = Field(...,alias="type", description="The type of task activity") 
    correlation_ids: Optional[conlist(EventHandlerMapping)] = Field(None, alias="correlationIds", description="The event to correlation ID mappings")
    task_fields: Optional[Dict[str, FieldMapping]] = Field(None, alias="taskFields", description="The event to task field mappings")
    __properties = ["initialTrigger", "type", "correlationIds", "taskFields"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('CreateNewTask', 'UpdateMatchingTasks'):
            raise ValueError("must be one of enum values ('CreateNewTask', 'UpdateMatchingTasks')")
        return value

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
    def from_json(cls, json_str: str) -> CreateNewTaskActivity:
        """Create an instance of CreateNewTaskActivity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in correlation_ids (list)
        _items = []
        if self.correlation_ids:
            for _item in self.correlation_ids:
                if _item:
                    _items.append(_item.to_dict())
            _dict['correlationIds'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in task_fields (dict)
        _field_dict = {}
        if self.task_fields:
            for _key in self.task_fields:
                if self.task_fields[_key]:
                    _field_dict[_key] = self.task_fields[_key].to_dict()
            _dict['taskFields'] = _field_dict
        # set to None if initial_trigger (nullable) is None
        # and __fields_set__ contains the field
        if self.initial_trigger is None and "initial_trigger" in self.__fields_set__:
            _dict['initialTrigger'] = None

        # set to None if correlation_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.correlation_ids is None and "correlation_ids" in self.__fields_set__:
            _dict['correlationIds'] = None

        # set to None if task_fields (nullable) is None
        # and __fields_set__ contains the field
        if self.task_fields is None and "task_fields" in self.__fields_set__:
            _dict['taskFields'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateNewTaskActivity:
        """Create an instance of CreateNewTaskActivity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateNewTaskActivity.parse_obj(obj)

        _obj = CreateNewTaskActivity.parse_obj({
            "initial_trigger": obj.get("initialTrigger"),
            "type": obj.get("type"),
            "correlation_ids": [EventHandlerMapping.from_dict(_item) for _item in obj.get("correlationIds")] if obj.get("correlationIds") is not None else None,
            "task_fields": dict(
                (_k, FieldMapping.from_dict(_v))
                for _k, _v in obj.get("taskFields").items()
            )
            if obj.get("taskFields") is not None
            else None
        })
        return _obj
