# test_local.py
# Run tests for desktop role


from docitlib import get_secrets


PLAYPATH = "roles/desktop"
USER = get_secrets("vars/desktop.yml", ".ansible-password.txt")['user']


def test_deploy_konsolerc_config__file_exists(host):
    """Verify file exists"""
    assert host.file(f"/home/{USER['username']}/.config/konsolerc").exists


def test_deploy_konsolerc_config__file_owner(host):
    """Verify file owner"""
    assert host.file(f"/home/{USER['username']}/.config/konsolerc").user == USER['username']


def test_deploy_konsolerc_config__file_group(host):
    """Verify file group"""
    assert host.file(f"/home/{USER['username']}/.config/konsolerc").group == USER['username']


def test_create_konsole_config_dir__file_dir(host):
    """Verify directory exists"""
    assert host.file(f"/home/{USER['username']}/.local/share/konsole").is_directory


def test_create_konsole_config_dir__file_owner(host):
    """Verify directory owner"""
    assert host.file(f"/home/{USER['username']}/.local/share/konsole").user == USER['username']


def test_create_konsole_config_dir__file_group(host):
    """Verify directory group"""
    assert host.file(f"/home/{USER['username']}/.local/share/konsole").group == USER['username']


def test_deploy_konsole_profile__file_exists(host):
    """Verify file exists"""
    assert host.file(f"/home/{USER['username']}/.local/share/konsole/green.profile").exists


def test_deploy_konsole_profile__file_owner(host):
    """Verify file owner"""
    assert host.file(f"/home/{USER['username']}/.local/share/konsole/green.profile").user == USER['username']


def test_deploy_konsole_profile__file_group(host):
    """Verify file group"""
    assert host.file(f"/home/{USER['username']}/.local/share/konsole/green.profile").group == USER['username']
