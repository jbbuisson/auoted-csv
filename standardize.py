from pathlib import Path
import argparse
import logging

from lib.columnCountError import ColumnCountError
from lib.config import Config
from lib.rule import Rule

def standardize(
    input_directory: Path,
    configuration_file: Path,
    output_directory: Path
):
    logging.basicConfig(format='LOG - %(levelname)s - %(message)s')

    config = Config(configuration_file)
    output_directory.mkdir(parents=True, exist_ok=True)

    files = input_directory.glob('*')
    for file in files:
        if not file.is_file():
            continue

        try:
            rule = config.get_rule(file.name)
            rule.standardize_file(file, output_directory)

        except KeyError:
            logging.error(f"{file.name} - No matching rule found")

        except ColumnCountError as column_count_exception:
            logging.error(column_count_exception.message)

        except Exception as e:
            logging.error(e.message)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("input_directory", help="Input directory containing the raw input files", type=Path)
    parser.add_argument("configuration_file", help="Configuration file containing the rules that the raw input files have to follow", type=Path)
    parser.add_argument("output_directory", help="Output directory containing the standardized files", type=Path)
    args = parser.parse_args()


    standardize(
        args.input_directory,
        args.configuration_file,
        args.output_directory
    )