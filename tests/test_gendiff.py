from gendiff import generate_diff
from pathlib import Path

def read_fixture(filename):
    return Path(__file__).parent / "fixtures" / filename

def test_generate_diff():
    file1 = read_fixture("file1.json")
    file2 = read_fixture("file2.json")
    expected_output = Path(read_fixture("expected.txt")).read_text().strip()

    diff = generate_diff(file1, file2)
    assert diff.strip() == expected_output
