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
        inputs = [50,75]
        correct = 75
        with mock.patch('builtins.input', side_effect=inputs):
            Prob3.guessing_game(correct)
            captured = capsys.readouterr().out.rstrip()
            assert 'higher' in captured.lower()

    def test_prints_lower_correctly(self, capsys):
        inputs = [50,25]
        correct = 25
        with mock.patch('builtins.input', side_effect=inputs):
            Prob3.guessing_game(correct)
            captured = capsys.readouterr().out.rstrip()
            assert 'lower' in captured.lower()

    def test_prints_proper_score(self, capsys):
        tests = {
                45: [50,25,30,40,45],
                87: [50,75,85,87],
                56: [50,75,75,75,65,55,56],
                1:  [50,25,12,6,3,2,1]
                }
        for c in tests:
            with mock.patch('builtins.input', side_effect=tests[c]):
                Prob3.guessing_game(c)
                captured = capsys.readouterr().out.rstrip()
                assert str(len(tests[c])) in captured.lower(), f"\nFor a correct value of {c}, I guessed {','.join(map(str,tests[c]))}. So the score should have been {len(tests[c])} but that value does not show up in your print out?\n\n"

class Test_Prob4:
    def test_used_while_loop(self):
        with open('Prob4.py', 'r') as f:
            filestr = ''.join(f.readlines())
        assert 'while' in filestr, '\nIt does not look like you used a while loop anywhere in your image.\n'
