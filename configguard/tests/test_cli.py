import json
import subprocess
import sys


def run_configguard(file_path):
    return subprocess.run(
        [sys.executable, "-m", "configguard.cli", file_path],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )


def test_valid_config():
    result = run_configguard("examples/config.json")

    assert result.returncode == 0
    assert "Configuration is valid!" in result.stdout


def test_missing_field():
    with open("examples/test_missing.json", "w") as file:
        json.dump({
            "app_name": "ConfigGuard",
            "environment": "development"
        }, file)

    result = run_configguard("examples/test_missing.json")

    assert result.returncode == 1
    assert "Missing required field: port" in result.stdout


def test_invalid_port():
    with open("examples/test_invalid_port.json", "w") as file:
        json.dump({
            "app_name": "ConfigGuard",
            "environment": "development",
            "port": "eight-thousand"
        }, file)

    result = run_configguard("examples/test_invalid_port.json")

    assert result.returncode == 1
    assert "Invalid type for port" in result.stdout


def test_invalid_environment():
    with open("examples/test_invalid_environment.json", "w") as file:
        json.dump({
            "app_name": "ConfigGuard",
            "environment": "prod",
            "port": 8000
        }, file)

    result = run_configguard("examples/test_invalid_environment.json")

    assert result.returncode == 1
    assert "Invalid value for environment" in result.stdout


def test_invalid_port_range():
    with open("examples/test_invalid_port_range.json", "w") as file:
        json.dump({
            "app_name": "ConfigGuard",
            "environment": "development",
            "port": 70000
        }, file)

    result = run_configguard("examples/test_invalid_port_range.json")

    assert result.returncode == 1
    assert "Invalid port range" in result.stdout