from .parser import load_file
from pathlib import Path
from .parser import load_file
from .diff_builder import build_diff
from .formatters.stylish import stylish

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



def generate_diff(file_path1, file_path2, format_name='stylish'):
    dict1 = load_file(file_path1)
    dict2 = load_file(file_path2)
    diff = build_diff(dict1, dict2)

    if format_name == 'stylish':
        return stylish(diff)
    raise ValueError(f"Unknown format: {format_name}")

