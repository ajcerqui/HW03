# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import pytest
import os

import Prob1
import Prob2
import Prob3

def numcheck(num, ans, tol=0.02):
    return (ans*(1-tol) < num < ans*(1+tol))

class Test_Prob1:
    def test_prints_something(self, capsys):
        Prob1.hailstone(4)
        captured = capsys.readouterr().out.rstrip()
        assert len(captured) > 0, "It seems nothing is being printed. Are you sure you are printing out the needed lines?"

    def test_returns_nothing(self, capsys):
        student = Prob1.hailstone(5)
        assert student is None, "You are not supposed to be returning anything from this function, and yet it seems you are?"

    def test_check_start_17(self, capsys):
        steps = [46,23,70,35,106,53,160,80,40,20,10,5,16,8,4,2,1]
        Prob1.hailstone(17)
        captured = capsys.readouterr().out.rstrip()
        str_by_line = captured.split('\n')
        assert len(str_by_line) == steps + 1, "Are you printing each step out on its own line? Or have you forgotten to print out the number of steps at the end?"
        for line, step in zip(str_by_line[:-1], steps):
            assert step in line, f"The value {step} was expected to show up, but didn't in line: '{line}'"

    def test_check_start_15(self, capsys):
        steps = [52,26,13,40,20,10,5,16,8,4,2,1]
        Prob1.hailstone(15)
        captured = capsys.readouterr().out.rstrip()
        str_by_line = captured.split('\n')
        assert len(str_by_line) == steps + 1, "Are you printing each step out on its own line? Or have you forgotten to print out the number of steps at the end?"
        for line, step in zip(str_by_line[:-1], steps):
            assert step in line, f"The value {step} was expected to show up, but didn't in line: '{line}'"

    def test_check_steps_taken_printed(self, capsys):
        Prob1.hailstone(27)
        captured = capsys.readouterr().out.rstrip()
        str_by_line = captured.split("\n")
        assert str(111) in str_by_line[-1], "Did you remember to print out the number of steps take in the last line? For hailstone(27) that should have been 111 but that number is not apparent in your last line."

class Test_Prob3:
    def test_used_a_loop(self):
        with open('Prob3.py', 'r') as f:
            filestr = ''.join(f.readlines())
        assert 'while' in filestr or 'for' in filestr, '\nIt does not look like you used a loop anywhere in your image.\n'
