import unittest

from get_github_keys import get_ssh_keys


class TestSuccess(unittest.TestCase):
    def test_my_own_user(self):
        test = get_ssh_keys("bkenez")
        my_pubkeys = [{'type': 'ssh-ed25519', 'key': 'AAAAC3NzaC1lZDI1NTE5AAAAIMCoH3Mazh49vQNT/5yEXcIQ++FFIYJJb14j4PAzYD06'}]
        assert test[0] == my_pubkeys
        assert test[1] == 200


class TestFailure(unittest.TestCase):
    def test_nonexisting_user(self):
        test = get_ssh_keys("bkenéz")
        assert test[0] == {"error": "GitHub user does not exist"}
        assert test[1] == 404
