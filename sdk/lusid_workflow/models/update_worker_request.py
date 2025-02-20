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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, constr, validator 

class UpdateWorkerRequest(BaseModel):
    """
    Request to Update a new worker  # noqa: E501
    """
    display_name:  StrictStr = Field(...,alias="displayName", description="Human readable name") 
    description:  Optional[StrictStr] = Field(None,alias="description", description="Human readable description") 
    worker_configuration: Optional[Any] = Field(..., alias="workerConfiguration", description="Information about how the worker should be executed")
    __properties = ["displayName", "description", "workerConfiguration"]

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
    def from_json(cls, json_str: str) -> UpdateWorkerRequest:
        """Create an instance of UpdateWorkerRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if worker_configuration (nullable) is None
        # and __fields_set__ contains the field
        if self.worker_configuration is None and "worker_configuration" in self.__fields_set__:
            _dict['workerConfiguration'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateWorkerRequest:
        """Create an instance of UpdateWorkerRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateWorkerRequest.parse_obj(obj)

        _obj = UpdateWorkerRequest.parse_obj({
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "worker_configuration": obj.get("workerConfiguration")
        })
        return _obj
