from subprocess import check_output
from unittest import TestCase

from shear import (
    shear,
    SINGLE_QUOTE,
    DOUBLE_QUOTE,
    BACKTICK
)

class Base(TestCase):
    def check_cli(self, string):
        if BACKTICK in string: string = string.replace(BACKTICK, "\\`")
        if SINGLE_QUOTE in string and DOUBLE_QUOTE not in string: string = DOUBLE_QUOTE + string + DOUBLE_QUOTE
        if DOUBLE_QUOTE in string and SINGLE_QUOTE not in string: string = SINGLE_QUOTE + string + SINGLE_QUOTE

        cmd = "printf $(./shear/__init__.py " + string + ")"
        try:
            self.check_result(check_output(cmd, shell=True, text=True))
        except Exception as e:
            print("cmd:", [cmd])
            raise e

    def check_py(self, string):
        self.check_result(shear(string))

    def check_result(self, result):
        self.assertEqual(result, 'Sheep')

class TestBasicPythonCases(Base):
    def test_single_quote(self):
        self.check_py("'Sheep'")

    def test_double_quote(self):
        self.check_py('"Sheep"')

    def test_triple_single_quote(self):
        self.check_py("'''Sheep'''")

    def test_triple_double_quote(self):
        self.check_py('"""Sheep"""')

    def test_backticks(self):
        self.check_py('`Sheep`')

    def test_byte_marker_quoting(self):
        self.check_py("b'Sheep'")

class TestAdvancedPythonCases(Base):
    def test_unbalanced_single_quote(self):
        self.assertEqual(shear("Sheep'"), "Sheep'")

    def test_repetitive_quoting(self):
        self.check_py("'`Sheep`'")

class TestBasicShellCases(Base):
    def test_single_quote(self):
        self.check_cli("'Sheep'")

    def test_double_quote(self):
        self.check_cli('"Sheep"')

    def test_triple_single_quote(self):
        self.check_cli("'''Sheep'''")

    def test_triple_double_quote(self):
        self.check_cli('"""Sheep"""')

    def test_backticks(self):
        self.check_cli('`Sheep`')

    def test_byte_marker_quoting(self):
        self.check_cli("b'Sheep'")

class TestAdvancedShellCases(Base):
    def test_unbalanced_single_quote(self):
        self.assertEqual(shear("Sheep'"), "Sheep'")

    def test_repetitive_quoting(self):
        self.check_cli("'`Sheep`'")