"""
This is a testing module for the main program convert.py
"""

import excon
from excon import convert
from excon.convert import pdf2csv


def test_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "y")





