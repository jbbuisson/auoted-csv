from pathlib import Path
import logging

from lib.config import Config
from lib.rule import Rule

INPUT_DIRECTORY = './dataDropArea/'
OUTPUT_DIRECTORY = './output/'
RULES_FILE = './param/config.yaml'

logging.basicConfig(format='LOG - %(levelname)s - %(message)s')

def standardize():
    config = Config(RULES_FILE)
    output_directory = Path(OUTPUT_DIRECTORY)

    files = Path(INPUT_DIRECTORY).glob('*')
    for file in files:
        if not file.is_file():
            continue

        try:
            rule = config.get_rule(file.name)

            print(rule)

            standardize_file(file.name, rule, output_directory)
        except KeyError:
            logging.error(f"No matching rule found for {file.name}")

def standardize_file(
    filename: str,
    rule: Rule,
    output_directory: Path
):
    pass

if __name__ == "__main__":
    standardize()