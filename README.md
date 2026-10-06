# ConfigGuard

ConfigGuard is a Python command-line tool that validates JSON and YAML configuration files and provides clear error messages with fix suggestions.

## Features

- Supports JSON and YAML configuration files
- Checks required configuration fields
- Validates data types
- Validates environment values
- Validates port ranges
- Detects configuration syntax errors
- Provides clear error messages and fix hints
- Returns proper success/failure exit codes
- Includes automated tests using pytest
- Tested in a WSL2/Linux environment

## Technologies

- Python
- JSON
- YAML
- PyYAML
- argparse
- pytest
- WSL2
- Git & GitHub

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