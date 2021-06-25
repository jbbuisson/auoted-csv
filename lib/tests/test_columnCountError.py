from pathlib import Path

from lib.columnCountError import ColumnCountError


class TestColumnCountError:
    def test_init(self):

        file = Path('./myFile.csv')
        exception = ColumnCountError(
            file,
            123,
            111,
            10)

        expected_message = 'myFile.csv - line 123 - Expected 111 column(s), but got 10'
        assert(exception.message == expected_message)