from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="ConfigGuard API",
    description="API for validating configuration files",
    version="1.0.0"
)


class ConfigRequest(BaseModel):
    app_name: str
    environment: str
    port: int


@app.get("/")
def home():
    return {
        "message": "ConfigGuard API is running"
    }


@app.post("/validate")
def validate_config(config: ConfigRequest):

    errors = []

    if config.environment not in [
        "development",
        "testing",
        "production"
    ]:
        errors.append({
            "error": "Invalid value for environment",
            "fix": "Use development, testing, or production."
        })

    if not 1 <= config.port <= 65535:
        errors.append({
            "error": "Invalid port range",
            "fix": "Port must be between 1 and 65535."
        })

    if errors:
        return {
            "valid": False,
            "errors": errors
        }

    return {
        "valid": True,
        "message": "Configuration is valid!"
    }