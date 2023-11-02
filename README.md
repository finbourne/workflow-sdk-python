# LUSID<sup>®</sup> Workflow Python SDK
This is the Python Preview SDK for the Workflow API for [LUSID by FINBOURNE](https://www.finbourne.com/lusid-technology), a bi-temporal investment management data platform with portfolio accounting capabilities. To use it you'll need a LUSID account. [Sign up for free at lusid.com](https://www.lusid.com/app/signup)

<a href="https://www.lusid.com/app/signup"><img src="https://content.finbourne.com/LUSID_repo.png" alt="LUSID_by_Finbourne"></a>

| branch | status |
| --- | --- |
| `main` |  ![PyPI](https://img.shields.io/pypi/v/lusid-workflow-sdk?color=blue)

## Installation

The PyPi package for the LUSID Workflow SDK can installed using the following:

```
pip install lusid-workflow-sdk finbourne-sdk-utilities
```

## Usage

```
import lusid_workflow
from fbnsdkutilities import ApiClientFactory

scheduler_factory = ApiClientFactory(lusid_workflow, api_secrets_filename="/path/to/secrets.json")
workers_api = scheduler_factory.build(lusid_workflow.api.WorkersApi)

workers_api.list_workers()
```
