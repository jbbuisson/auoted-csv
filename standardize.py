from pathlib import Path
import logging

from lib.columnCountError import ColumnCountError
from lib.config import Config
from lib.rule import Rule

INPUT_DIRECTORY = './dataDropArea/'
OUTPUT_DIRECTORY = './output/'
RULES_FILE = './param/config.yaml'

logging.basicConfig(format='LOG - %(levelname)s - %(message)s')


def standardize():
    config = Config(Path(RULES_FILE))
    output_directory = Path(OUTPUT_DIRECTORY)
    output_directory.mkdir(parents=True, exist_ok=True)

    files = Path(INPUT_DIRECTORY).glob('*')
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
    standardize()