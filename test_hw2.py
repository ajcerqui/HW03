# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import mock
import pytest
import os

import Prob3
import Prob4
import CodeLibrary

def numcheck(num, ans, tol=0.02):
    return (ans*(1-tol) < num < ans*(1+tol))

class Test_WrittenWork:
    def test_pdf_present(self):
        assert os.path.isfile('HW2.pdf') == True


class Test_Prob4:
    def test_prints_correct_password(self, capsys):
        CodeLibrary.SEED = 10
        code = CodeLibrary.generate_code(seed=CodeLibrary.SEED)
        Prob4.password_finder()
        captured = capsys.readouterr()
        assert captured.out.rstrip() == code

    def test_prints_a_password(self, capsys):
        Prob4.password_finder()
        captured = capsys.readouterr()
        captured = captured.out.rstrip()
        assert (type(captured)==str and len(captured) == 3)

