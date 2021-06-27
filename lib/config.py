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
        
        raise Exception(f"{filename} - No matching rule found")

    @staticmethod
    def _check_parameters(parameters: dict, filename_pattern: str) -> bool:
        if (Config._check_parameter(parameters, filename_pattern, PARAMETER_DELIMITER)
            and Config._check_parameter(parameters, filename_pattern, PARAMETER_COLUMN_COUNT)):
            return True


    @staticmethod
    def _check_parameter(parameters: dict, filename_pattern: str, key: str) -> bool:
        if key not in parameters:
            raise Exception(f'Config - pattern: {filename_pattern} - Key {key} missing')
        return True

    @staticmethod
    def _get_standardization_rules(config_file: TextIOBase) -> dict:
        
        filename_patterns = yaml.safe_load(config_file)

        rules = {}

        for filename_pattern, parameters in filename_patterns.items():

            parameters = filename_patterns[filename_pattern]
            Config._check_parameters(parameters, filename_pattern)
            rule = Rule(
                filename_patterns[filename_pattern][PARAMETER_DELIMITER],
                filename_patterns[filename_pattern][PARAMETER_COLUMN_COUNT])

            rules[filename_pattern] = rule
        return rules

#TODO verifier typage parametres
#TODO ajouter string doc