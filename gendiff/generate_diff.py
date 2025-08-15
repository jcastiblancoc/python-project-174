from .parser import load_file
from .diff_builder import build_diff
from .formatters.stylish import stylish

def generate_diff(file_path1, file_path2, format_name='stylish'):
    dict1 = load_file(file_path1)
    dict2 = load_file(file_path2)
    diff = build_diff(dict1, dict2)

    if format_name == 'stylish':
        return stylish(diff)
    raise ValueError(f"Unknown format: {format_name}")
