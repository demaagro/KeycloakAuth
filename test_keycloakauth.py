# test_keycloakauth.py
"""
Tests for KeycloakAuth module.
"""

import unittest
from keycloakauth import KeycloakAuth

class TestKeycloakAuth(unittest.TestCase):
    """Test cases for KeycloakAuth class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = KeycloakAuth()
        self.assertIsInstance(instance, KeycloakAuth)
        
    def test_run_method(self):
        """Test the run method."""
        instance = KeycloakAuth()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
