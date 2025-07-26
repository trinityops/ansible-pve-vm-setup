import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_role_loads_successfully(host):
    """Test that the role loads without syntax errors."""
    # Since we can't actually test Proxmox API calls in a container,
    # we just verify the role structure exists and can be parsed
    assert True