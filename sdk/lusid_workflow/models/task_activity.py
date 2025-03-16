# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, ValidationError, validator
from lusid_workflow.models.create_new_task_activity import CreateNewTaskActivity
from lusid_workflow.models.update_matching_tasks_activity import UpdateMatchingTasksActivity
from typing import Union, Any, List, TYPE_CHECKING
from pydantic.v1 import StrictStr, Field

TASKACTIVITY_ONE_OF_SCHEMAS = ["CreateNewTaskActivity", "UpdateMatchingTasksActivity"]

class TaskActivity(BaseModel):
    """
    Information about what tasks to create/update when receiving events
    """
    # data type: CreateNewTaskActivity
    oneof_schema_1_validator: Optional[CreateNewTaskActivity] = None
    # data type: UpdateMatchingTasksActivity
    oneof_schema_2_validator: Optional[UpdateMatchingTasksActivity] = None
    if TYPE_CHECKING:
        actual_instance: Union[CreateNewTaskActivity, UpdateMatchingTasksActivity]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(TASKACTIVITY_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = TaskActivity.construct()
        error_messages = []
        match = 0
        matchclass = ""
        # validate data type: CreateNewTaskActivity
        if not isinstance(v, CreateNewTaskActivity):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CreateNewTaskActivity`")
        else:
            match += 1
            matchclass = matchclass + " CreateNewTaskActivity"
        # validate data type: UpdateMatchingTasksActivity
        if not isinstance(v, UpdateMatchingTasksActivity):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateMatchingTasksActivity`")
        else:
            match += 1
            matchclass = matchclass + " UpdateMatchingTasksActivity"
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in TaskActivity with oneOf schemas: CreateNewTaskActivity, UpdateMatchingTasksActivity. Details: Matched classes " + matchclass)
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in TaskActivity with oneOf schemas: CreateNewTaskActivity, UpdateMatchingTasksActivity. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> TaskActivity:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> TaskActivity:
        """Returns the object represented by the json string"""
        instance = TaskActivity.construct()
        error_messages = []
        match = 0
        matchclass = ""
        

        # deserialize data into CreateNewTaskActivity
        try:
            instance.actual_instance = CreateNewTaskActivity.from_json(json_str)
            match += 1
            matchclass =matchclass + " CreateNewTaskActivity"
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateMatchingTasksActivity
        try:
            instance.actual_instance = UpdateMatchingTasksActivity.from_json(json_str)
            match += 1
            matchclass =matchclass + " UpdateMatchingTasksActivity"
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into TaskActivity with oneOf schemas: CreateNewTaskActivity, UpdateMatchingTasksActivity. Matches: "+matchclass+", Details: " + ", ".join(error_messages) + ", JSON: " + json_str)
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into TaskActivity with oneOf schemas: CreateNewTaskActivity, UpdateMatchingTasksActivity. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

        def __str__(self):
            """For `print` and `pprint`"""
            return pprint.pformat(self.dict(by_alias=False))
    
        def __repr__(self):
            """For `print` and `pprint`"""
            return self.to_str()
    
        def to_str(self) -> str:
            """Returns the string representation of the model using alias"""
            return pprint.pformat(self.dict(by_alias=True))
