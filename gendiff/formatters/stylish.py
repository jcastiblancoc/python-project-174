def stylish(diff, depth=1):
    indent_size = depth * 4
    indent = ' ' * (indent_size - 2)
    closing_indent = ' ' * ((depth - 1) * 4)
    lines = []

    for item in diff:
        key = item['key']
        type_ = item['type']

        if type_ == 'added':
            lines.append(f"{indent}+ {key}: {to_str(item['value'], depth)}")
        elif type_ == 'removed':
            lines.append(f"{indent}- {key}: {to_str(item['value'], depth)}")
        elif type_ == 'unchanged':
            lines.append(f"{indent}  {key}: {to_str(item['value'], depth)}")
        elif type_ == 'changed':
            lines.append(f"{indent}- {key}: {to_str(item['old_value'], depth)}")
            lines.append(f"{indent}+ {key}: {to_str(item['new_value'], depth)}")
        elif type_ == 'nested':
            children = stylish(item['children'], depth + 1)
            lines.append(f"{indent}  {key}: {children}")

    return "{\n" + "\n".join(lines) + "\n" + closing_indent + "}"


def to_str(value, depth):
    if isinstance(value, dict):
        inner_indent_size = depth * 4 + 4
        inner_indent = ' ' * inner_indent_size
        closing_indent = ' ' * (depth * 4)
        lines = [f"{inner_indent}{k}: {to_str(v, depth + 1)}" for k, v in value.items()]
        return "{\n" + "\n".join(lines) + "\n" + closing_indent + "}"

    if isinstance(value, bool):
        return str(value).lower()  # True -> 'true', False -> 'false'

    if value is None:
        return "null"

    return str(value)
