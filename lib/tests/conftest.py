# from unittest.mock import Mock, MagicMock
# import _csv

# from pytest import fixture

# @fixture(scope="class")
# def data_reader_mock() -> Mock:
#     data_reader = Mock(spec=_csv.reader)
#     data_reader.__iter__ = Mock()
#     data_reader.__iter__.side_effect = [["This", "is", "the", "first", "line"], ["This", "is", "the", "second", "line"]]
#     # data_reader = [["This", "is", "the", "first", "line"], ["This", "is", "the", "second", "line"]]
#     return data_reader


# @fixture(scope="class")
# def data_reader_mock_not_ok() -> MagicMock:
#     # data_reader = MagicMock(spec=MyList)
#     data_reader = MagicMock()
#     data_reader.line_num = 1
#     # data_reader = [["This", "is", "the", "first", "line"], ["This", "is", "the", "second", "line"]]
#     # type(data_reader).line_num = PropertyMock(return_value=1)
#     return data_reader