from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]

CONFIG_PATH = ROOT_DIR / "configs" / "config.yaml"

PARAMS_PATH = ROOT_DIR / "configs" / "params.yaml"

SCHEMA_PATH = ROOT_DIR / "configs" / "schema.yaml"

RAW_DATA_PATH = ROOT_DIR / "data" / "raw" / "uber.csv"

INTERIM_DATA_PATH = ROOT_DIR / "data" / "interim"

PROCESSED_DATA_PATH = ROOT_DIR / "data" / "processed"

MODEL_DIR = ROOT_DIR / "models"

ARTIFACT_DIR = ROOT_DIR / "artifacts"

LOG_DIR = ROOT_DIR / "logs"