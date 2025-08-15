def format_value(value):
    if isinstance(value, dict) or isinstance(value, list):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def build_plain(diff, path_prefix=""):
    lines = []
    for item in diff:
        key = item["key"]
        type_ = item["type"]
        prop = f"{path_prefix}{key}"

        if type_ == "nested":
            lines.extend(build_plain(item["children"], f"{prop}."))
        elif type_ == "added":
            val = format_value(item["value"])
            lines.append(f"Property '{prop}' was added with value: {val}")
        elif type_ == "removed":
            lines.append(f"Property '{prop}' was removed")
        elif type_ == "changed":
            old_v = format_value(item["old_value"])
            new_v = format_value(item["new_value"])
            lines.append(
                f"Property '{prop}' was updated. From {old_v} to {new_v}"
            )
        # unchanged -> no output
    return lines


def plain(diff):
    return "\n".join(build_plain(diff))
