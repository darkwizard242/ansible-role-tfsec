import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_tfsec_binary_exists(host):
    assert host.file('/usr/local/bin/tfsec').exists


def test_tfsec_binary_file(host):
    assert host.file('/usr/local/bin/tfsec').is_file


def test_tfsec_binary_which(host):
    assert host.check_output('which tfsec') == '/usr/local/bin/tfsec'
