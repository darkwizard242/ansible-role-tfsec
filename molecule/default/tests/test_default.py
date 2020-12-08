import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE_BINARY = '/usr/local/bin/tfsec'


def test_tfsec_binary_exists(host):
    """
    Tests if tfsec binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_tfsec_binary_file(host):
    """
    Tests if tfsec binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_tfsec_binary_which(host):
    """
    Tests the output to confirm tfsec's binary location.
    """
    assert host.check_output('which tfsec') == PACKAGE_BINARY
