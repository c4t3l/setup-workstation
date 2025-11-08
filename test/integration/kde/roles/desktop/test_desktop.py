# test_desktop.py
# Run tests for desktop role


import sys
import os

from docitlib import read_file

KDEDEFAULTDIR = "/usr/share/kde-settings/kde-profile/default/xdg"
SKELDIR = "/etc/skel/.config"

def test_deploy_global_theme_general__file_contains(host):
    """Verify file contains value"""
    assert host.file(f"{KDEDEFAULTDIR}/kdeglobals").contains("BreezeDark")


def test_deploy_global_theme_kde1__file_contains(host):
    """Verify file contains value"""
    assert host.file(f"{KDEDEFAULTDIR}/kdeglobals").contains("org.fedoraproject.fedora.desktop")


def test_deploy_global_theme_kde2__file_contains(host):
    """Verify file contains value"""
    assert host.file(f"{KDEDEFAULTDIR}/kdeglobals").contains("BreezeDark")


def test_create_skeleton_dir__file_exists(host):
    """Verify directory exsits"""
    assert host.file(SKELDIR).is_directory


def test_deploy_skeleton_file__file_exists(host):
    """Verify file exists"""
    assert host.file(f"{SKELDIR}/kdeglobals").exists
