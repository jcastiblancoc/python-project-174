# gendiff/parser.py
import json
import yaml
from pathlib import Path


def load_file(filepath):
    path = Path(filepath)
    ext = path.suffix.lower()

    with open(path, 'r') as f:
        if ext == '.json':
            return json.load(f)
        elif ext in ['.yml', '.yaml']:
            return yaml.safe_load(f)
        else:
            raise ValueError(f'Unsupported file format: {ext}')
