import unittest

from get_github_keys import get_ssh_keys


class TestSuccess(unittest.TestCase):
    def test_my_own_user(self):
        test = get_ssh_keys("bkenez")
        my_pubkeys = [{'type': 'ssh-rsa', 'key': 'AAAAB3NzaC1yc2EAAAABJQAAAQEAso3tMbAY4fpGNMW40nKhEJ8NGJ7mE8TMLxlQfa+Rg2DPNZ4kE6AvqYfRnsG4/um60Qmer6OO6aU8+EgQ1+j5vBtcBwygLI+CIh+P1XCw5pHhFwjDAB8P5ilucIjCVime3/J5UMiT88twBabxaxCEWe95/Fr5kvS8yefuyF7mhd/eFb54dZLbTX67tyBSDwg+EUxPkY9ns9z+eayD6kj/if82ZRtsXr4k2YRr+IKGN+TIIpU2ptabTurnI5ZtzaZ7ueRlnv+4t9HD1Gb/SDPIzsUu/1gMl/zjdGZgYz+VZFr2jIFj5PyEWm/dP9aTby7V0YZpXjjlQZ+CJHkb7+xa8w=='}, {'type': 'ssh-rsa', 'key': 'AAAAB3NzaC1yc2EAAAADAQABAAABAQC22jWWHDCbxnhx0tltqowxgtK+GC6e5SZY2VezHeBbhmfyWesqLGN2GkrviBIoNKfSglSwWh6ANXVSCLzNZRRlLx9Bi5BxjvXGKAY06gu5NWCKqWYCywiqKSDwYa4Ukz8GCobGrDN/9G9S5lCjPgD7ICLCZECPBzykotl30aH45TUP6vLggewmOz/jmS7jAPLcT5A4o9q+XH6vyHOdSaDsOEK8/ygYbJ+YaNhRYbpGQS9nybfd2YE3hh8FB7YtOOnLfC/4N7Oz5V2noIM3VFDeix9EfM7kUCQulIHdoyuumCs7VkN4HfPoP7rStj8+x5Gb+ZDTCEJ8mhQbAqt/Idzv'}]
        assert test[0] == my_pubkeys
        assert test[1] == 200


class TestFailure(unittest.TestCase):
    def test_nonexisting_user(self):
        test = get_ssh_keys("bkenéz")
        assert test[0] == {"error": "GitHub user does not exist"}
        assert test[1] == 404
