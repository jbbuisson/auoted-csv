import pytest
from lib.rule import Rule

from lib.columnCountError import ColumnCountError

class TestRule:
    def test_read_rows_column_count_ok(self, data_reader_mock):
        rule = Rule(',', 5)
        actual_read_rows = rule._read_rows("filename.txt", data_reader_mock)

        assert actual_read_rows == data_reader_mock

    def test_read_rows_column_count_not_ok(self, data_reader_mock_not_ok):
        rule = Rule(',', 6)
        with pytest.raises(ColumnCountError) as exception:
            actual_read_rows = rule._read_rows("filename.txt", data_reader_mock_not_ok)

        expected_message = 'filename.txt - line 1 - Expected 6 column(s), but got 5'
        assert str(exception.value) == expected_message
