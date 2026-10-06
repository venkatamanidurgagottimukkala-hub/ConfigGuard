import argparse
import json
import io
import sys

import yaml


def load_config(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            if file_path.endswith(".json"):
                return json.load(file)

            elif file_path.endswith((".yaml", ".yml")):
                return yaml.safe_load(file)

            else:
                print("❌ Unsupported file format.")
                print("💡 Fix: Use a .json, .yaml, or .yml file.")
                sys.exit(1)

    except (json.JSONDecodeError, yaml.YAMLError):
        print("❌ Configuration syntax error.")
        print("💡 Fix: Check your JSON/YAML formatting.")
        sys.exit(1)

    except FileNotFoundError:
        print("❌ Configuration file not found.")
        print("💡 Fix: Check the file path and try again.")
        sys.exit(1)


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    parser = argparse.ArgumentParser(
        description="Validate JSON and YAML configuration files."
    )

    parser.add_argument(
        "file",
        help="Path to the configuration file"
    )

    args = parser.parse_args()

    config = load_config(args.file)

    print("Configuration loaded successfully!")

    has_errors = False

    required_fields = ["app_name", "environment", "port"]

    for field in required_fields:
        if field not in config:
            print(f"❌ Missing required field: {field}")
            print(f"💡 Fix: Add '{field}' to your configuration file.")
            has_errors = True

    if "environment" in config and config["environment"] not in [
        "development",
        "testing",
        "production"
    ]:
        print("❌ Invalid value for environment.")
        print("💡 Fix: Use development, testing, or production.")
        has_errors = True

    if "port" in config and not isinstance(config["port"], int):
        print("❌ Invalid type for port.")
        print("💡 Fix: 'port' must be a number, for example 8000.")
        has_errors = True

    if "port" in config and isinstance(config["port"], int) and not 1 <= config["port"] <= 65535:
        print("❌ Invalid port range.")
        print("💡 Fix: 'port' must be between 1 and 65535.")
        has_errors = True

    print(config)

    if has_errors:
        sys.exit(1)

    print("✅ Configuration is valid!")


if __name__ == "__main__":
    main()
