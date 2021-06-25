from lib.rule import Rule

class TestRule:
    def test_read_rows(data_reader_mock):
        rule = Rule(',', 5)
        actual_read_rows = rule._read_rows("filename.txt", data_reader_mock)

        assert actual_read_rows == data_reader_mock
