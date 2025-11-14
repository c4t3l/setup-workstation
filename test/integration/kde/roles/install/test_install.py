# test_install.py

"""
roles/install/tasks/main.yml
"""

import os
import pytest
import sys

# docitlib path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from docitlib import read_yaml


ROLEPATH = "roles/install"
PKGS = read_yaml(
        f"{ROLEPATH}/tasks/main.yml")[0]["ansible.builtin.dnf"]["name"]

@pytest.mark.parametrize("pkgs", PKGS)
def test_install_core_workstation_packages__package_installed(host, pkgs):
    """ Verify packages are installed """
    assert host.package(pkgs).is_installed
