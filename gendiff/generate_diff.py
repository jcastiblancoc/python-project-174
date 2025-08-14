from .parser import load_file
from pathlib import Path

def format_value(value, is_yaml=False):
    """Convierte valores a la representación esperada en el diff"""
    if isinstance(value, bool):
        return str(value).lower() if is_yaml else str(value)
    return value

def generate_diff(file1, file2):
    data1 = load_file(file1)
    data2 = load_file(file2)

    is_yaml = Path(file1).suffix.lower() in ['.yml', '.yaml']

    result = []
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in all_keys:
        if key in data1 and key not in data2:
            result.append(f"  - {key}: {format_value(data1[key], is_yaml)}")
        elif key not in data1 and key in data2:
            result.append(f"  + {key}: {format_value(data2[key], is_yaml)}")
        elif data1[key] != data2[key]:
            result.append(f"  - {key}: {format_value(data1[key], is_yaml)}")
            result.append(f"  + {key}: {format_value(data2[key], is_yaml)}")
        else:
            result.append(f"    {key}: {format_value(data1[key], is_yaml)}")

    return "{\n" + "\n".join(result) + "\n}"
