"""
Скрипт для парсингу введених команд.
"""
from .parse_input_validator import parse_input_validator


@parse_input_validator
def parse_input(cmd_string):
    cmd, *args = cmd_string.split()
    cmd = cmd.strip().lower()
    return cmd, args
