from unittest.mock import MagicMock

from pytest import fixture

@fixture(scope="class")
def data_reader_mock() -> MagicMock:
    data_reader = MagicMock(spec=[])
    data_reader = [["This", "is", "the", "first", "line"], ["This", "is", "the", "second", "line"]]
    return data_reader


@fixture(scope="class")
def data_reader_mock_not_ok() -> MagicMock:
    # data_reader = MagicMock(spec=MyList)
    data_reader = MagicMock()
    data_reader.line_num = 1
    data_reader = [["This", "is", "the", "first", "line"], ["This", "is", "the", "second", "line"]]
    # type(data_reader).line_num = PropertyMock(return_value=1)
    return data_reader