from subprocess import check_output
from unittest import TestCase

from __init__ import shear

class TestBasicCases(TestCase):
    def test_single_quote(self):
        result = shear("'Sheep'")
        self.assertEqual(result, 'Sheep')

    def test_double_quote(self):
        result = shear('"Sheep"')
        self.assertEqual(result, 'Sheep')

    def test_triple_single_quote(self):
        result = shear("'''Sheep'''")
        self.assertEqual(result, 'Sheep')

    def test_triple_double_quote(self):
        result = shear('"""Sheep"""')
        self.assertEqual(result, 'Sheep')

    def test_backticks(self):
        result = shear('`Sheep`')
        self.assertEqual(result, 'Sheep')

    def test_byte_marker_quoting(self):
        result = shear("b'Sheep'")
        self.assertEqual(result, "Sheep")

class TestAdvancedCases(TestCase):
    def test_unbalanced_single_quote(self):
        result = shear("Sheep'")
        self.assertEqual(result, "Sheep'")

    def test_repetitive_quoting(self):
        result = shear("'`Sheep`'")
        self.assertEqual(result, "Sheep")
