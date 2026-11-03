# LuminesceMultiQueryResponse

Readonly configuration for the Luminesce custom multi-query Worker
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | [optional] 
**workspace_key** | **str** | The Workspaces key of the multi-query the worker runs | [optional] 
**drive_location_and_file_name** | **str** | Where in Drive the results are saved, which may contain placeholders | [optional] 
**format** | **str** | The format the results are saved in, csv when not given | [optional] 
**may_overwrite** | **bool** | Whether an existing file of the same name may be overwritten | [optional] 
**drive_template_location** | **str** | The Drive path of the template the results are saved with | [optional] 
**date_time_format** | **str** | The format DateTime values are written in | [optional] 
**when_some_fail** | **bool** | Whether the results of the queries that succeeded are still saved when others did not | [optional] 
**keep_for_seconds** | **int** | How long Luminesce keeps the results once done, in seconds | [optional] 
## Example

```python
from lusid_workflow.models.luminesce_multi_query_response import LuminesceMultiQueryResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: Optional[StrictStr] = "example_type"
workspace_key: Optional[StrictStr] = "example_workspace_key"
drive_location_and_file_name: Optional[StrictStr] = "example_drive_location_and_file_name"
format: Optional[StrictStr] = "example_format"
may_overwrite: Optional[StrictBool] = # Replace with your value
may_overwrite:Optional[StrictBool] = None
drive_template_location: Optional[StrictStr] = "example_drive_template_location"
date_time_format: Optional[StrictStr] = "example_date_time_format"
when_some_fail: Optional[StrictBool] = # Replace with your value
when_some_fail:Optional[StrictBool] = None
keep_for_seconds: Optional[StrictInt] = # Replace with your value
keep_for_seconds: Optional[StrictInt] = None
luminesce_multi_query_response_instance = LuminesceMultiQueryResponse(type=type, workspace_key=workspace_key, drive_location_and_file_name=drive_location_and_file_name, format=format, may_overwrite=may_overwrite, drive_template_location=drive_template_location, date_time_format=date_time_format, when_some_fail=when_some_fail, keep_for_seconds=keep_for_seconds)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

