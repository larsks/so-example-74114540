import databases
from starlette.config import Config

config = Config(".env")

# Database configurations
_user = config("DB_USER", cast=str)
_password = config("DB_PASSWORD", cast=str)
_host = config("DB_HOST", cast=str)
_database = config("DB_NAME", cast=str)
_port = config("DB_PORT", cast=int, default=3306)

db = databases.Database(f"mysql://{_user}:{_password}@{_host}/{_database}?port={_port}")
