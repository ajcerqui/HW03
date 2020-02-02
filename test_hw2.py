# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import mock
import pytest
import os
import random

import Prob2
import Prob3
import Prob4

def numcheck(num, ans, tol=0.02):
    return (ans*(1-tol) < num < ans*(1+tol))

class Test_WrittenWork:
    def test_pdf_present(self):
        assert os.path.isfile('HW2.pdf') == True

class Test_Prob2:
    def test_prints_something(self, capsys):
        inputs = ['zebra']
        with mock.patch('builtins.input', side_effect=inputs):
            Prob2.pigify()
            captured = capsys.readouterr().out.rstrip()
            assert len(captured) > 0

    def test_word_zebra(self, capsys):
        inputs = ['zebra']
        with mock.patch('builtins.input', side_effect=inputs):
            Prob2.pigify()
            captured = capsys.readouterr().out.rstrip()
            assert captured == 'ebrazay'

    def test_word_iguana(self, capsys):
        inputs = ['iguana']
        with mock.patch('builtins.input', side_effect=inputs):
            Prob2.pigify()
            captured = capsys.readouterr().out.rstrip()
            assert captured == 'iguanahay'

    def test_word_radish(self, capsys):
        inputs = ['radish']
        with mock.patch('builtins.input', side_effect=inputs):
            Prob2.pigify()
            captured = capsys.readouterr().out.rstrip()
            assert captured == 'adishray'

    def test_word_ugly(self, capsys):
        inputs = ['ugly']
        with mock.patch('builtins.input', side_effect=inputs):
            Prob2.pigify()
            captured = capsys.readouterr().out.rstrip()
            assert captured == 'uglyhay'

class Test_Prob3:
    def test_prints_something(self, capsys):
        inputs = [50]
        correct = 50
        with mock.patch('builtins.input', side_effect=inputs):
            Prob3.guessing_game(correct)
            captured = capsys.readouterr().out.rstrip()
            assert len(captured) > 0

    def test_prints_higher_correctly(self, capsys):
        inputs = [50]
        correct = 75
        with mock.patch('builtins.input', side_effect=inputs):
            Prob3.guessing_game(correct)
            captured = capsys.readouterr().out.rstrip()
            assert captured.lower() == 'the unknown number is higher!'
