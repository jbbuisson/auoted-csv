import csv
from pathlib import Path

from lib.columnCountError import ColumnCountError

OUTPUT_SEPARATOR = ','

class Rule:
    def __init__(
            self,
            delimiter:str,
            column_count:int):

        self.delimiter = delimiter
        self.column_count = column_count


    def standardize_file(
            self,
            file:Path,
            output_directory:Path):

        input_rows = self._read_rows(file)
        self._write_rows(file, output_directory, input_rows)


    def _read_rows(self, file):
        input_rows = []

        with open(file, "r", encoding='utf-8') as csv_file:
            data_reader = csv.reader(csv_file, delimiter=self.delimiter)

            for row in data_reader:
                if len(row) != self.column_count:
                    raise ColumnCountError(
                        file,
                        data_reader.line_num,
                        self.column_count,
                        len(row))

                input_rows.append(row)
        return input_rows


    def _write_rows(self, file, output_directory, input_rows):
        with open(output_directory / file.name, "w", encoding='utf-8') as output_csv_file:
            csv_writer = csv.writer(output_csv_file,
                                    delimiter=OUTPUT_SEPARATOR,
                                    quoting=csv.QUOTE_ALL)

            csv_writer.writerows(input_rows)
