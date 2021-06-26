from lib.config import Config
from unittest import mock

@mock.patch('lib.config.yaml.safe_load')
def test_config_get_standardization_rules(mock_yaml_safe_load):
    filename_patterns = {
        'file_test_1_[0-9]{8}.csv': {'delimiter': ',', 'column_count': 5},
        'file_test_2_[0-9]{8}.csv': {'delimiter': ';', 'column_count': 4}
    }

    mock_yaml_safe_load.return_value = filename_patterns

    actual_rules = Config._get_standardization_rules("mock_config_file")

    assert(len(actual_rules.keys()) == 2)
