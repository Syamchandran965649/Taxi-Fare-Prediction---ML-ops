from dataclasses import dataclass

from src.utils.constants import SCHEMA_PATH
from src.utils.common import read_yaml

@dataclass
class DataSchema:
    columns:dict
    target_column:str

def load_schema():
    schema=read_yaml(SCHEMA_PATH)
    return DataSchema(
        columns=schema["columns"],
        target_column=schema['target_column']
    )