# -*- coding: utf-8 -*-

"""Tests for Bio2BEL miRBase."""

import unittest

from bio2bel_mirbase import get_version


class TestMeta(unittest.TestCase):
    """Test metadata from Bio2BEL miRBase."""

    def test_get_version(self):
        """Test the get_version function."""
        self.assertIsInstance(get_version(), str)
