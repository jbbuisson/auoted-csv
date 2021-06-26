import re
from pathlib import Path

from io import TextIOBase
import yaml

from lib.rule import Rule

PARAMETER_DELIMITER = "delimiter"
PARAMETER_COLUMN_COUNT = "column_count"

class Config:
    rules = {}

    def __init__(
        self,
        config_file:Path):

        with open(config_file, 'r') as file:
            self.rules = Config._get_standardization_rules(file)


    def get_rule(self, filename: str) -> Rule:
        """
        Get the rule corresponding to filename
        Raise KeyError when filename does not match any rule
        """
        for rule in self.rules:
            match = re.match(rule, filename)
            if match:
                return self.rules[rule]
        
        raise KeyError


    def _get_standardization_rules(config_file: TextIOBase) -> dict:
        
        filename_patterns = yaml.safe_load(config_file)

        rules = {}

        for filename_pattern, parameters in filename_patterns.items():
            if parameters.get(PARAMETER_DELIMITER) is None:
                raise Exception(f'Config - pattern: {filename_pattern} - Key {PARAMETER_DELIMITER} missing')

            if parameters.get(PARAMETER_COLUMN_COUNT) is None:
                raise Exception(f'Config - pattern: {filename_pattern} - Key {PARAMETER_COLUMN_COUNT} missing')

            rule = Rule(
                filename_patterns[filename_pattern][PARAMETER_DELIMITER],
                filename_patterns[filename_pattern][PARAMETER_COLUMN_COUNT])

            rules[filename_pattern] = rule
        return rules

#TODO parametres entree
#TODO simplifier _get_standardization_rules
#TODO verifier typage parametres
#TODO ajouter string doc