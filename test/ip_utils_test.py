import os
import sys
import unittest

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
sys.path.append(os.path.abspath(os.path.join(PROJECT_DIR, "src", "cyberyozh_utils")))

from ip_utils import get_public_ip, get_own_ip


class TestIpUtils(unittest.TestCase):

    def test_config(self):
        """
        Test reading from Mock config file
        """
        public_ip = get_public_ip()
        own_ip = get_own_ip()
        print(f"Public IP: {public_ip}")
        print(f"Own IP: {own_ip}")
        self.assertTrue(isinstance(public_ip, str))
        self.assertTrue(isinstance(own_ip, str))


if __name__ == "__main__":
    unittest.main()
