import json


def format_json(diff):
    """Return the diff structure serialized as JSON.
    We pretty-print with indentation for readability and deterministic tests.
    """
    return json.dumps(diff, ensure_ascii=False, indent=2)
