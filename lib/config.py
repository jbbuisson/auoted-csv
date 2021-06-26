import re
from pathlib import Path

from io import TextIOBase
import yaml

from lib.rule import Rule


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

        for filename_pattern in filename_patterns:
            rule = Rule(
                filename_patterns[filename_pattern]["delimiter"],
                filename_patterns[filename_pattern]["column_count"])

            rules[filename_pattern] = rule
        return rules
