# test_local.py
# Run tests for desktop role

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from docitlib import get_secrets
from docitlib import read_file


PLAYPATH = "roles/desktop"
USER = get_secrets("vars/desktop.yml", ".ansible-password.txt")['user']


##### Deploy konsolerc config #################################################
def test_deploy_konsolerc_config__file_exists(host):
    """Verify file exists"""
    assert host.file(f"/home/{USER['username']}/.config/konsolerc").exists


def test_deploy_konsolerc_config__file_owner(host):
    """Verify file owner"""
    assert host.file(
            f"/home/{USER['username']}/.config/konsolerc"
            ).user == USER['username']


def test_deploy_konsolerc_config__file_group(host):
    """Verify file group"""
    assert host.file(
            f"/home/{USER['username']}/.config/konsolerc"
            ).group == USER['username']


def test_create_konsole_config_dir__file_dir(host):
    """Verify directory exists"""
    assert host.file(
            f"/home/{USER['username']}/.local/share/konsole").is_directory


def test_create_konsole_config_dir__file_owner(host):
    """Verify directory owner"""
    assert host.file(
            f"/home/{USER['username']}/.local/share/konsole"
            ).user == USER['username']


def test_create_konsole_config_dir__file_group(host):
    """Verify directory group"""
    assert host.file(
            f"/home/{USER['username']}/.local/share/konsole"
            ).group == USER['username']


##### Deploy konsole profile ##################################################
def test_deploy_konsole_profile__file_exists(host):
    """Verify file exists"""
    assert host.file(
            f"/home/{USER['username']}/.local/share/konsole/green.profile"
            ).exists


def test_deploy_konsole_profile__file_owner(host):
    """Verify file owner"""
    assert host.file(
            f"/home/{USER['username']}/.local/share/konsole/green.profile"
            ).user == USER['username']


def test_deploy_konsole_profile__file_group(host):
    """Verify file group"""
    assert host.file(
            f"/home/{USER['username']}/.local/share/konsole/green.profile"
            ).group == USER['username']


##### Download omz installer ##################################################
def test_download_omz_installer__file_exists(host):
    """Verify file exists"""
    assert host.file("/tmp/install_ohmyzsh.sh").exists


def test_install_omz__file_exists(host):
    """Verify file exists"""
    assert host.file(f"/home/{USER['username']}/.oh-my-zsh").exists


##### Deploy zshrc ############################################################
def test_deploy_zshrc__file_exists(host):
    """Verify file exists"""
    assert host.file(f"/home/{USER['username']}/.zshrc").exists


def test_deploy_zshrc__file_owner(host):
    """Verify file owner"""
    assert host.file(
            f"/home/{USER['username']}/.zshrc").user == USER['username']


def test_deploy_zshrc__file_group(host):
    """Verify file group"""
    assert host.file(
            f"/home/{USER['username']}/.zshrc").group == USER['username']


def test_deploy_zshrc__file_contents(host):
    """Verify file contents"""
    assert host.file(
            f"/home/{USER['username']}/.zshrc"
            ).content_string == read_file(f"{PLAYPATH}/files/zsh/zshrc")


##### Create zsh_home dir #####################################################
def test_create_zsh_home_dir__is_directory(host):
    """Verify directory exists"""
    assert host.file(f"/home/{USER['username']}/.zsh_home").is_directory


def test_create_zsh_home_dir__owner(host):
    """Verify directory owner"""
    assert host.file(
            f"/home/{USER['username']}/.zsh_home").user == USER['username']


def test_create_zsh_home_dir__group(host):
    """Verify directory group"""
    assert host.file(
            f"/home/{USER['username']}/.zsh_home").group == USER['username']


##### Deploy home_zsh #########################################################
def test_deploy_home_zsh__file_exists(host):
    """Verify file exists"""
    assert host.file(f"/home/{USER['username']}/.zsh_home/home.zsh").exists


def test_deploy_home_zsh__file_owner(host):
    """Verify file owner"""
    assert host.file(
            f"/home/{USER['username']}/.zsh_home/home.zsh"
            ).user == USER['username']


def test_deploy_home_zsh__file_group(host):
    """Verify file group"""
    assert host.file(
            f"/home/{USER['username']}/.zsh_home/home.zsh"
            ).group == USER['username']


def test_deploy_home_zsh__file_content(host):
    """Verify file content"""
    assert host.file(
            f"/home/{USER['username']}/.zsh_home/home.zsh"
            ).content_string == read_file(f"{PLAYPATH}/files/zsh/home.zsh")
