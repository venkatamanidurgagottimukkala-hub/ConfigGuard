# ConfigGuard

ConfigGuard is a Python configuration validation tool that validates JSON and YAML configuration files through a command-line interface and a FastAPI REST API.

It provides clear validation errors, fix suggestions, and proper success/failure responses.

## Features

- Supports JSON and YAML configuration files
- Command-line configuration validation
- REST API using FastAPI
- Checks required configuration fields
- Validates data types
- Validates environment values
- Validates port ranges
- Detects configuration syntax errors
- Provides clear error messages and fix hints
- Returns proper success/failure exit codes
- Automated testing using pytest
- Interactive Swagger/OpenAPI documentation
- Deployed as a live web API
- Tested in a WSL2/Linux environment

## Technologies

- Python
- FastAPI
- Pydantic
- JSON
- YAML
- PyYAML
- argparse
- pytest
- Uvicorn
- WSL2
- Git & GitHub
- Render

## Required Configuration

ConfigGuard validates these fields:

| Field | Type | Valid Values |
|---|---|---|
| `app_name` | String | Required |
| `environment` | String | `development`, `testing`, `production` |
| `port` | Integer | `1` – `65535` |

## Installation

Clone the repository:

```bash
git clone https://github.com/venkatamanidurgagottimukkala-hub/ConfigGuard.git
cd ConfigGuard