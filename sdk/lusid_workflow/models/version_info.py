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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictInt, StrictStr 

class VersionInfo(BaseModel):
    """
    The version metadata.  # noqa: E501
    """
    as_at_created: Optional[datetime] = Field(None, alias="asAtCreated", description="The asAt datetime at which this entity was first created.")
    user_id_created:  Optional[StrictStr] = Field(None,alias="userIdCreated", description="The unique id of the user who created this entity.") 
    request_id_created:  Optional[StrictStr] = Field(None,alias="requestIdCreated", description="The request id of the request that created this entity.") 
    as_at_modified: Optional[datetime] = Field(None, alias="asAtModified", description="The asAt datetime at which this entity was last updated.")
    user_id_modified:  Optional[StrictStr] = Field(None,alias="userIdModified", description="The unique id of the user who last updated this entity.") 
    request_id_modified:  Optional[StrictStr] = Field(None,alias="requestIdModified", description="The request id of the request that last updated this entity.") 
    as_at_version_number: Optional[StrictInt] = Field(None, alias="asAtVersionNumber", description="The integer version number for this entity (the entity was created at version 1).")
    __properties = ["asAtCreated", "userIdCreated", "requestIdCreated", "asAtModified", "userIdModified", "requestIdModified", "asAtVersionNumber"]

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
    def from_json(cls, json_str: str) -> VersionInfo:
        """Create an instance of VersionInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if as_at_created (nullable) is None
        # and __fields_set__ contains the field
        if self.as_at_created is None and "as_at_created" in self.__fields_set__:
            _dict['asAtCreated'] = None

        # set to None if user_id_created (nullable) is None
        # and __fields_set__ contains the field
        if self.user_id_created is None and "user_id_created" in self.__fields_set__:
            _dict['userIdCreated'] = None

        # set to None if request_id_created (nullable) is None
        # and __fields_set__ contains the field
        if self.request_id_created is None and "request_id_created" in self.__fields_set__:
            _dict['requestIdCreated'] = None

        # set to None if as_at_modified (nullable) is None
        # and __fields_set__ contains the field
        if self.as_at_modified is None and "as_at_modified" in self.__fields_set__:
            _dict['asAtModified'] = None

        # set to None if user_id_modified (nullable) is None
        # and __fields_set__ contains the field
        if self.user_id_modified is None and "user_id_modified" in self.__fields_set__:
            _dict['userIdModified'] = None

        # set to None if request_id_modified (nullable) is None
        # and __fields_set__ contains the field
        if self.request_id_modified is None and "request_id_modified" in self.__fields_set__:
            _dict['requestIdModified'] = None

        # set to None if as_at_version_number (nullable) is None
        # and __fields_set__ contains the field
        if self.as_at_version_number is None and "as_at_version_number" in self.__fields_set__:
            _dict['asAtVersionNumber'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VersionInfo:
        """Create an instance of VersionInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VersionInfo.parse_obj(obj)

        _obj = VersionInfo.parse_obj({
            "as_at_created": obj.get("asAtCreated"),
            "user_id_created": obj.get("userIdCreated"),
            "request_id_created": obj.get("requestIdCreated"),
            "as_at_modified": obj.get("asAtModified"),
            "user_id_modified": obj.get("userIdModified"),
            "request_id_modified": obj.get("requestIdModified"),
            "as_at_version_number": obj.get("asAtVersionNumber")
        })
        return _obj
