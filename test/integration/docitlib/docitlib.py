# docitlib shared test library
"""
Simple library of helper functions for making cleaner tests
"""

import subprocess
import shlex
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


def get_secrets(file, secret_key):
    """Returns info encrypted via ansible vault"""
    cmd = f"ansible-vault view --vault-password-file {secret_key} {file}"
    data = subprocess.run(shlex.split(cmd), capture_output=True)
    return yaml.safe_load(data.stdout)
