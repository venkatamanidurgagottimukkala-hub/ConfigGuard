import argparse
import io
import json
import sys
import yaml


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

    try:
        if args.file.endswith(".json"):
            with open(args.file, "r") as file:
                config = json.load(file)

        elif args.file.endswith((".yaml", ".yml")):
            with open(args.file, "r") as file:
                config = yaml.safe_load(file)

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
        print(f"💡 Fix: Check the file path: {args.file}")
        sys.exit(1)

    print("Configuration loaded successfully!")

    has_errors = False

    required_fields = ["app_name", "environment", "port"]

    for field in required_fields:
        if field not in config:
            print(f"❌ Missing required field: {field}")
            print(f"💡 Fix: Add '{field}' to your configuration file.")
            has_errors = True

    if "port" in config and not isinstance(config["port"], int):
        print("❌ Invalid type for port.")
        print("💡 Fix: 'port' must be a number, for example 8000.")
        has_errors = True

    print(config)

    if has_errors:
        sys.exit(1)

    print("✅ Configuration is valid!")


if __name__ == "__main__":
    main()