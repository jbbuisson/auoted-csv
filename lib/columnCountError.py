from pathlib import Path


class ColumnCountError(Exception):
    """Exception raised when input data does not have the correct number of columns.

    Attributes:
        filename -- Name of the file being read
        line_number -- line where the error was found
        expected_column_count -- expected number of columns
        actual_column_count -- actual number of columns
    """

    def __init__(
            self,
            filename:str,
            line_number:int,
            expected_column_count:int,
            actual_column_count:int):
        self.message = f"{filename} - line {line_number} - Expected {expected_column_count} column(s), but got {actual_column_count}"
        super().__init__(self.message)
