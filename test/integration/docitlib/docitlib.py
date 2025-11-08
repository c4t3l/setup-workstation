# docitlib shared test library
"""
Simple library of helper functions for making cleaner tests
"""

import yaml

def read_yaml(file):
    """Reads in a yaml
    and outputs a dict
    """
    with open(file, "r") as f:
        _data = yaml.load(f, yaml.SafeLoader)
    return _data


def read_file(file):
    """Reads in a file
    and outputs a string
    """
    with open(file, "r") as f:
        _data = f.read()
    return _data

