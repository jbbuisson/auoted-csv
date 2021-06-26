import pytest
from lib.config import Config
from unittest import mock

@mock.patch('lib.config.yaml.safe_load')
def test_config_get_standardization_rules_ok(mock_yaml_safe_load):
    filename_patterns = {
        'file_test_1_[0-9]{8}.csv': {'delimiter': ',', 'column_count': 5},
        'file_test_2_[0-9]{8}.csv': {'delimiter': ';', 'column_count': 4}
    }

    mock_yaml_safe_load.return_value = filename_patterns

    actual_rules = Config._get_standardization_rules("mock_config_file")

    assert(len(actual_rules.keys()) == 2)
    assert(actual_rules.keys() == filename_patterns.keys())


@mock.patch('lib.config.yaml.safe_load')
def test_config_get_standardization_rules_parameter_delimiter_missing(mock_yaml_safe_load):
    filename_patterns = {
        'file_test_1_[0-9]{8}.csv': {'column_count': 5},
        'file_test_2_[0-9]{8}.csv': {'delimiter': ';', 'column_count': 4}
    }

    mock_yaml_safe_load.return_value = filename_patterns

    with pytest.raises(Exception) as exception:
        actual_rules = Config._get_standardization_rules("mock_config_file")

    expected_message = 'Config - pattern: file_test_1_[0-9]{8}.csv - Key delimiter missing'
    assert str(exception.value) == expected_message

@mock.patch('lib.config.yaml.safe_load')
def test_config_get_standardization_rules_parameter_column_count_missing(mock_yaml_safe_load):
    filename_patterns = {
        'file_test_1_[0-9]{8}.csv': {'delimiter': ',', 'column_count': 5},
        'file_test_2_[0-9]{8}.csv': {'delimiter': ';'}
    }

    mock_yaml_safe_load.return_value = filename_patterns

    with pytest.raises(Exception) as exception:
        actual_rules = Config._get_standardization_rules("mock_config_file")

    expected_message = 'Config - pattern: file_test_2_[0-9]{8}.csv - Key column_count missing'
    assert str(exception.value) == expected_message


def test_get_rules():
    pass