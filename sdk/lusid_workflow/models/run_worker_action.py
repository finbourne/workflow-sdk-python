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
from typing import Any, Dict, List, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictInt, conlist, constr, validator 
from lusid_workflow.models.field_mapping import FieldMapping
from lusid_workflow.models.resource_id import ResourceId
from lusid_workflow.models.resultant_child_task_configuration import ResultantChildTaskConfiguration
from lusid_workflow.models.worker_status_triggers import WorkerStatusTriggers

class RunWorkerAction(BaseModel):
    """
    Defines a Run Worker Action  # noqa: E501
    """
    type:  StrictStr = Field(...,alias="type", description="Type name for this Action") 
    worker_id: ResourceId = Field(..., alias="workerId")
    worker_as_at: Optional[datetime] = Field(None, alias="workerAsAt", description="Worker AsAt")
    worker_parameters: Optional[Dict[str, FieldMapping]] = Field(None, alias="workerParameters", description="Parameters for this Worker")
    worker_status_triggers: Optional[WorkerStatusTriggers] = Field(None, alias="workerStatusTriggers")
    child_task_configurations: Optional[conlist(ResultantChildTaskConfiguration)] = Field(None, alias="childTaskConfigurations", description="Tasks can be generated from run worker results; this is the configuration")
    worker_timeout: Optional[StrictInt] = Field(None, alias="workerTimeout", description="Worker WorkerTimeout in seconds")
    __properties = ["type", "workerId", "workerAsAt", "workerParameters", "workerStatusTriggers", "childTaskConfigurations", "workerTimeout"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""

        # Finbourne have removed enum validation on all models, except for this use case:
        # Workflow and notification application SDK use the property name 'type' as the discriminator on a number of classes.
        # During instantiation, the value of 'type' is checked against the enum values, 
        

        # check it's a class that uses the 'type' property as a discriminator
        # list of classes can be found by searching for 'actual_instance: Union[' in the generated code
        if 'RunWorkerAction' not in [ 
                                    # For notification application classes
                                    'AmazonSqsNotificationType',
                                    'AmazonSqsNotificationTypeResponse',
                                    'AmazonSqsPrincipalAuthNotificationType',
                                    'AmazonSqsPrincipalAuthNotificationTypeResponse',
                                    'AzureServiceBusTypeResponse',
                                    'AzureServiceBusNotificationType',
                                    'EmailNotificationType',
                                    'EmailNotificationTypeResponse',
                                    'SmsNotificationType',
                                    'SmsNotificationTypeResponse',
                                    'WebhookNotificationType',
                                    'WebhookNotificationTypeResponse',
                        
                                    # For workflow application classes
                                    'CreateChildTasksAction', 
                                    'RunWorkerAction', 
                                    'TriggerParentTaskAction',
                                    'CreateChildTasksActionResponse', 
                                    'RunWorkerActionResponse',
                                    'TriggerParentTaskActionResponse',
                                    'CreateNewTaskActivity',
                                    'UpdateMatchingTasksActivity',
                                    'CreateNewTaskActivityResponse', 
                                    'UpdateMatchingTasksActivityResponse',
                                    'Fail', 
                                    'GroupReconciliation', 
                                    'HealthCheck', 
                                    'LuminesceView', 
                                    'SchedulerJob', 
                                    'Sleep',
                                    'FailResponse', 
                                    'GroupReconciliationResponse', 
                                    'HealthCheckResponse', 
                                    'LuminesceViewResponse', 
                                    'SchedulerJobResponse', 
                                    'SleepResponse']:
           return value
        
        # Only validate the 'type' property of the class
        if "type" != "type":
            return value

        if value not in ('RunWorker'):
            raise ValueError("must be one of enum values ('RunWorker')")
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
    def from_json(cls, json_str: str) -> RunWorkerAction:
        """Create an instance of RunWorkerAction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of worker_id
        if self.worker_id:
            _dict['workerId'] = self.worker_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in worker_parameters (dict)
        _field_dict = {}
        if self.worker_parameters:
            for _key in self.worker_parameters:
                if self.worker_parameters[_key]:
                    _field_dict[_key] = self.worker_parameters[_key].to_dict()
            _dict['workerParameters'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of worker_status_triggers
        if self.worker_status_triggers:
            _dict['workerStatusTriggers'] = self.worker_status_triggers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in child_task_configurations (list)
        _items = []
        if self.child_task_configurations:
            for _item in self.child_task_configurations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['childTaskConfigurations'] = _items
        # set to None if worker_as_at (nullable) is None
        # and __fields_set__ contains the field
        if self.worker_as_at is None and "worker_as_at" in self.__fields_set__:
            _dict['workerAsAt'] = None

        # set to None if worker_parameters (nullable) is None
        # and __fields_set__ contains the field
        if self.worker_parameters is None and "worker_parameters" in self.__fields_set__:
            _dict['workerParameters'] = None

        # set to None if child_task_configurations (nullable) is None
        # and __fields_set__ contains the field
        if self.child_task_configurations is None and "child_task_configurations" in self.__fields_set__:
            _dict['childTaskConfigurations'] = None

        # set to None if worker_timeout (nullable) is None
        # and __fields_set__ contains the field
        if self.worker_timeout is None and "worker_timeout" in self.__fields_set__:
            _dict['workerTimeout'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RunWorkerAction:
        """Create an instance of RunWorkerAction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RunWorkerAction.parse_obj(obj)

        _obj = RunWorkerAction.parse_obj({
            "type": obj.get("type"),
            "worker_id": ResourceId.from_dict(obj.get("workerId")) if obj.get("workerId") is not None else None,
            "worker_as_at": obj.get("workerAsAt"),
            "worker_parameters": dict(
                (_k, FieldMapping.from_dict(_v))
                for _k, _v in obj.get("workerParameters").items()
            )
            if obj.get("workerParameters") is not None
            else None,
            "worker_status_triggers": WorkerStatusTriggers.from_dict(obj.get("workerStatusTriggers")) if obj.get("workerStatusTriggers") is not None else None,
            "child_task_configurations": [ResultantChildTaskConfiguration.from_dict(_item) for _item in obj.get("childTaskConfigurations")] if obj.get("childTaskConfigurations") is not None else None,
            "worker_timeout": obj.get("workerTimeout")
        })
        return _obj
