"""
This is a testing module for the main program convert.py
"""

from excon import convert


def test_input1(capsys):
    input_values = ['xxx', 'false', 'xxx', 'true']

    def mock_input(s):
        return input_values.pop(0)
    convert.input = mock_input

    convert.pdf2csv()

    out, err = capsys.readouterr()

    assert out == "".join(['Please try again.\n',
                           'Please try again.\n'])

    assert err == ''


def test_input2(capsys):
    input_values = ['t', 'f']

    def mock_input(s):
        return input_values.pop(0)
    convert.input = mock_input

    convert.pdf2csv()

    out, err = capsys.readouterr()

    assert out == ""

    assert err == ''


def test_input3(capsys):
    input_values = [23, 'TRUE', '', 'FaLSe']

    def mock_input(s):
        return input_values.pop(0)
    convert.input = mock_input

    convert.pdf2csv()

    out, err = capsys.readouterr()

    assert out == "".join(['Please try again.\n',
                           'Please try again.\n'])

    assert err == ''
