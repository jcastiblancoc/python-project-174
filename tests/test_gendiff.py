from gendiff import generate_diff
from pathlib import Path

def read_fixture(filename):
    """Devuelve la ruta completa a un archivo de fixtures"""
    return Path(__file__).parent / "fixtures" / filename

def test_generate_diff_json():
    file1 = str(read_fixture("file1.json"))
    file2 = str(read_fixture("file2.json"))
    expected_output = read_fixture("expected.txt").read_text().strip()

    diff = generate_diff(file1, file2)
    assert diff.strip() == expected_output

def test_generate_diff_yaml():
    file1 = str(read_fixture("file1.yml"))
    file2 = str(read_fixture("file2.yml"))
    expected_output = read_fixture("expected_yaml.txt").read_text().strip()

    diff = generate_diff(file1, file2)
    assert diff.strip() == expected_output


def test_generate_diff_nested_json():
    file1 = str(read_fixture("file1_nested.json"))
    file2 = str(read_fixture("file2_nested.json"))
    expected_output = read_fixture("expected_stylish.txt").read_text().strip()
    diff = generate_diff(file1, file2)
    assert diff.strip() == expected_output


def test_generate_diff_nested_yaml():
    file1 = str(read_fixture("file1_nested.yml"))
    file2 = str(read_fixture("file2_nested.yml"))
    expected_output = read_fixture("expected_stylish.txt").read_text().strip()
    diff = generate_diff(file1, file2)
    assert diff.strip() == expected_output

def test_generate_diff_plain_json():
    file1 = str(read_fixture("file1_nested.json"))
    file2 = str(read_fixture("file2_nested.json"))
    expected_output = read_fixture("expected_plain.txt").read_text().strip()
    diff = generate_diff(file1, file2, 'plain')
    assert diff.strip() == expected_output

def test_generate_diff_plain_yaml():
    file1 = str(read_fixture("file1_nested.yml"))
    file2 = str(read_fixture("file2_nested.yml"))
    expected_output = read_fixture("expected_plain.txt").read_text().strip()
    diff = generate_diff(file1, file2, 'plain')
    assert diff.strip() == expected_output
