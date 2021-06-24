from unittest import mock

import pytest
from lib.config import PARAMETER_COLUMN_COUNT, PARAMETER_DELIMITER, Config
from lib.rule import Rule


@mock.patch('lib.config.yaml.safe_load')
def test_config_get_standardization_rules_ok(mock_yaml_safe_load):
    filename_patterns = {
        'file_test_1_[0-9]{8}.csv': {'delimiter': ',', 'column_count': 5},
        'file_test_2_[0-9]{8}.csv': {'delimiter': ';', 'column_count': 4}
    }

    mock_yaml_safe_load.return_value = filename_patterns

    actual_rules = Config._get_standardization_rules("mock_config_file")

    assert len(actual_rules.keys()) == 2
    assert actual_rules.keys() == filename_patterns.keys()


def test_check_parameters_ok():
    parameters = {'delimiter': ',', 'column_count': 5}
    
    assert Config._check_parameter(parameters, "mock_config_file", PARAMETER_DELIMITER)
    assert Config._check_parameter(parameters, "mock_config_file", PARAMETER_COLUMN_COUNT)


def test_check_parameters_not_ok():
    parameters = {'delimiter': ','}
    
    assert Config._check_parameter(parameters, "mock_config_file", PARAMETER_DELIMITER)

    with pytest.raises(Exception) as exception:
        Config._check_parameter(parameters, "mock_config_file", PARAMETER_COLUMN_COUNT)

    expected_message = "Config - pattern: mock_config_file - Key column_count missing"
    assert str(exception.value) == expected_message


@mock.patch('lib.config.Config._get_standardization_rules')
def test_get_rule_ok(get_standardization_rules):
    
    expected_rule = Rule(',', 5)
    
    rules = {
        'file_test_1_[0-9]{8}.csv': expected_rule,
        'file_test_2_[0-9]{8}.csv': Rule(';', 4)
    }
    get_standardization_rules.return_value = rules

    config = Config(__file__)

    actual_rule = config.get_rule("file_test_1_20200101.csv")

    vars(actual_rule) == vars(expected_rule)


@mock.patch('lib.config.Config._get_standardization_rules')
def test_get_rule_not_found(get_standardization_rules):
    
    rules = {
        'file_test_1_[0-9]{8}.csv': Rule(',', 5),
        'file_test_2_[0-9]{8}.csv': Rule(';', 4)
    }
    get_standardization_rules.return_value = rules

    config = Config(__file__)

    with pytest.raises(Exception) as exception:
        actual_rule = config.get_rule("file_no_pattern_matching.csv")

    expected_message = "file_no_pattern_matching.csv - No matching rule found"
    assert str(exception.value) == expected_message
