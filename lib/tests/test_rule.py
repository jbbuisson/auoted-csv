import pytest
from unittest import mock

from lib.rule import Rule
from lib.columnCountError import ColumnCountError

@mock.patch('lib.rule.csv.reader')
def test_read_rows_column_count_ok(mock_csv_reader):
    expected_read_rows = [
        ['This', 'is', 'the', 'first', 'line'],
        ['This', 'is', 'the', 'second', 'line']
    ]
    mock_csv_reader.return_value = expected_read_rows
    rule = Rule(',', 5)
    actual_read_rows = rule._read_rows('filename.txt', 'mock_csv_input_file')

    assert actual_read_rows == expected_read_rows

@mock.patch('lib.rule.csv.reader')
def test_read_rows_column_count_not_ok(mock_csv_reader):
    mock_csv_reader.return_value = [
        ['This', 'is', 'the', 'first', 'line'],
        ['This', 'is', 'the', 'second', 'line', 'too', 'long']
    ]
    rule = Rule(',', 5)
    with pytest.raises(ColumnCountError) as exception:
        rule._read_rows('filename.txt', 'mock_csv_input_file')

    expected_message = 'filename.txt - line 2 - Expected 5 column(s), but got 7'
    assert str(exception.value) == expected_message
