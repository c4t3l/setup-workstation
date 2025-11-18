# test_user.py
# Run test for user role

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from docitlib import read_yaml
import pytest

USER = read_yaml("vars/desktop.yml")["user"]
HOME = f"/home/{USER['username']}"
PDIRS = [
        "devel",
        "formulas",
        "os_images",
        "personal",
        "playbooks",
        "presentations",
        "rpms"
        ]
RPMDIRS = [
        "centos-scm",
        "copr",
        "fedora-review",
        "fedora-scm",
        ]

##### Create main user account ################################################
def test_create_main_user_account__user_exists(host):
    """Verify user exists"""
    assert host.user(USER["username"]).exists


def test_create_main_user_account__user_home(host):
    """Verify user home"""
    assert host.user(USER["username"]).home == HOME


def test_create_main_user_account__user_group(host):
    """Verify user group"""
    assert host.user(USER["username"]).groups == [
            USER["username"], "wheel", "mock"
            ]


##### Create productivity dirs ################################################
@pytest.mark.parametrize("mydir", PDIRS)
def test_create_productivity_dirs__file_directory(host, mydir):
    """Verify directory exists"""
    assert host.file(f"{HOME}/Documents/{mydir}").is_directory


@pytest.mark.parametrize("mydir", PDIRS)
def test_create_productivity_dirs__file_user(host, mydir):
    """Verify directory user"""
    assert host.file(f"{HOME}/Documents/{mydir}").user == USER["username"]


@pytest.mark.parametrize("mydir", PDIRS)
def test_create_productivity_dirs__file_group(host, mydir):
    """Verify directory group"""
    assert host.file(f"{HOME}/Documents/{mydir}").group == USER["username"]


##### Create rpm dirs##########################################################
@pytest.mark.parametrize("mydir", RPMDIRS)
def test_create_rpm_dirs__file_directory(host, mydir):
    """Verify directory exists"""
    assert host.file(f"{HOME}/Documents/rpms/{mydir}").exists


@pytest.mark.parametrize("mydir", RPMDIRS)
def test_create_rpm_dirs__file_user(host, mydir):
    """Verify directory user"""
    assert host.file(f"{HOME}/Documents/rpms/{mydir}").user == USER["username"]


@pytest.mark.parametrize("mydir", RPMDIRS)
def test_create_rpm_dirs__file_group(host, mydir):
    """Verify directory group"""
    assert host.file(f"{HOME}/Documents/rpms/{mydir}").group == USER["username"]
