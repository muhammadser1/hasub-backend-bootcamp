import json
import pytest
from utils.file_operations import load_json, write_json


def test_load_valid_json():
    db_path = "tests/test_data/test_check_valid.json"
    data = {'key': 'value'}
    with open(db_path, 'w') as f:
        json.dump(data, f)
    result = load_json(db_path)
    assert result == data


def test_load_data_not_dict():
    db_path = "tests/test_data/test_check_valid.json"
    data = []
    with open(db_path, 'w') as f:
        json.dump(data, f)
    with pytest.raises(ValueError):
        load_json(db_path)


def test_load_filepath_not_found():
    db_path = "tests/test_data/test_filepath_not_found.json"
    with pytest.raises(FileNotFoundError):
        load_json(db_path)


def test_valid_write_to_file():
    data = {"123": 1}
    db_path = "tests/test_data/test_check_valid2.json"
    write_json(data, db_path)
    data_db = load_json(db_path)
    assert data_db == data
