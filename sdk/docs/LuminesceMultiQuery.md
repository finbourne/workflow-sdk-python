# LuminesceMultiQuery

Configuration for a Worker that runs a Luminesce custom multi-query saved in Workspaces, saving its results to Drive as one file. Its parameters are the multi-query's scalar parameters, and the export settings below, which a task may override through the worker's `export-*` parameters.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of worker | 
**workspace_key** | **str** | The Workspaces key of the multi-query, e.g. &#x60;shared/SomeWorkspace/items/sets/SomeSet&#x60;, read as each run starts. An item of a personal workspace can only be read by the user who saved it, so only runs as that user can use it. | 
**drive_location_and_file_name** | **str** | Where in Drive to save the results. May contain the placeholders &#x60;{executionId}&#x60;, &#x60;{date:format}&#x60; (when the queries started, UTC) and &#x60;{param:name}&#x60; (a scalar parameter&#39;s value); the extension comes from the format. | 
**format** | **str** | The format to save in: csv (the default), pipe, excel, json, jsonProper, jsonProperWithLineage, jsonProperByTable, xml, parquet, sqlite or pdf. Several results are one worksheet each for excel, one table each for sqlite, one key each for jsonProperByTable, and otherwise one file each within a zip. | [optional] 
**may_overwrite** | **bool** | Whether an existing file of the same name may be overwritten, rather than the run failing. False by default. | [optional] 
**drive_template_location** | **str** | The Drive path and file name of a template to save with. Only excel and pdf support templates. | [optional] 
**date_time_format** | **str** | The format to write DateTime values in, Luminesce&#39;s default (&#x60;yyyy-MM-dd HH:mm:ss.fff&#x60;) when not given. | [optional] 
**when_some_fail** | **bool** | Whether the results of the queries that succeeded are still saved when others did not, the worker then completing with the status PartiallyCompleted. False by default, the worker then failing with nothing saved. | [optional] 
**keep_for_seconds** | **int** | How long Luminesce keeps the results once done, e.g. to look into a run or save them again: 2 hours by default, at most 31 days. | [optional] 
## Example

```python
from lusid_workflow.models.luminesce_multi_query import LuminesceMultiQuery
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
workspace_key: StrictStr = "example_workspace_key"
drive_location_and_file_name: StrictStr = "example_drive_location_and_file_name"
format: Optional[StrictStr] = "example_format"
may_overwrite: Optional[StrictBool] = # Replace with your value
may_overwrite:Optional[StrictBool] = None
drive_template_location: Optional[StrictStr] = "example_drive_template_location"
date_time_format: Optional[StrictStr] = "example_date_time_format"
when_some_fail: Optional[StrictBool] = # Replace with your value
when_some_fail:Optional[StrictBool] = None
keep_for_seconds: Optional[StrictInt] = # Replace with your value
keep_for_seconds: Optional[StrictInt] = None
luminesce_multi_query_instance = LuminesceMultiQuery(type=type, workspace_key=workspace_key, drive_location_and_file_name=drive_location_and_file_name, format=format, may_overwrite=may_overwrite, drive_template_location=drive_template_location, date_time_format=date_time_format, when_some_fail=when_some_fail, keep_for_seconds=keep_for_seconds)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

