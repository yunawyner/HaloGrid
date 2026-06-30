# test_halogrid.py
"""
Tests for HaloGrid module.
"""

import unittest
from halogrid import HaloGrid

class TestHaloGrid(unittest.TestCase):
    """Test cases for HaloGrid class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HaloGrid()
        self.assertIsInstance(instance, HaloGrid)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HaloGrid()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
