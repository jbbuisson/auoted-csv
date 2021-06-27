import csv
from pathlib import Path
import logging

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
            output_directory:Path) -> None:

        with open(file, "r", encoding='utf-8') as csv_input_file:
            input_rows = self._read_rows(file.name, csv_input_file)

        with open(output_directory / file.name, "w", encoding='utf-8') as csv_output_file:
            self._write_rows(csv_output_file, input_rows)


    def _read_rows(self, filename, csv_input_file) -> list:

        data_reader = csv.reader(csv_input_file, delimiter=self.delimiter)

        input_rows = []
        row_number = 0
        lines_with_errors = []

        for row in data_reader:
            row_number += 1
            if len(row) != self.column_count:
                lines_with_errors.append(row_number)
                logging.error(f"{filename} - line {row_number} - Expected {self.column_count} column(s), but found {len(row)}")


            input_rows.append(row)

        if len(lines_with_errors) > 0:
            raise Exception(f"{filename} - Column count - found {len(lines_with_errors)} error(s)")
            
        return input_rows


    def _write_rows(self, output_csv_file, input_rows):
            csv_writer = csv.writer(output_csv_file,
                                    delimiter=OUTPUT_SEPARATOR,
                                    quoting=csv.QUOTE_ALL)

            csv_writer.writerows(input_rows)
