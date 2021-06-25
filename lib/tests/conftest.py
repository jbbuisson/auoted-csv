from unittest.mock import Mock

from pytest import fixture

@fixture(scope="class")
def data_reader_mock() -> Mock:
    data_reader = Mock(spec=[])
    data_reader = [["This", "is", "the", "first", "line"], ["This", "is", "the", "second", "line"]]
    return data_reader