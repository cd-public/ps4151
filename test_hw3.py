# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import mock
import pytest
import os
import random
import math

import Prob2
import Prob3
import Prob4

def numcheck(num, ans, tol=0.02):
    return (ans*(1-tol) < num < ans*(1+tol))

class Test_WrittenWork:
    def test_pdf_present(self):
        assert os.path.isfile('HW3.pdf') == True


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
    def test_Example1(self, capsys):
        inputs = ['1000','0.10','12']
        with mock.patch('builtins.input', side_effect=inputs):
            Prob3.calc_savings()
            captured = capsys.readouterr().out.rstrip()
            _, cap_num = captured.split(':')
            assert numcheck(float(cap_num.strip()), 1216.64, 0.001)

    def test_Example2(self, capsys):
        inputs = ['1500','0.25','24']
        with mock.patch('builtins.input', side_effect=inputs):
            Prob3.calc_savings()
            captured = capsys.readouterr().out.rstrip()
            _, cap_num = captured.split(':')
            assert numcheck(float(cap_num.strip()), 9263.56, 0.001)

    def test_3000_005_24(self, capsys):
        inputs = ['3000','0.05','24']
        with mock.patch('builtins.input', side_effect=inputs):
            Prob3.calc_savings()
            captured = capsys.readouterr().out.rstrip()
            _, cap_num = captured.split(':')
            assert numcheck(float(cap_num.strip()), 3705.42, 0.001)

    def test_Output_String_Format(self, capsys):
        inputs = ['1500','0.25','24']
        with mock.patch('builtins.input', side_effect=inputs):
            Prob3.calc_savings()
            captured = capsys.readouterr().out.rstrip()
            assert "Amount in savings:" in captured

    def test_Proper_Rounding(self, capsys):
        inputs = ['1500','0.25','24']
        with mock.patch('builtins.input', side_effect=inputs):
            Prob3.calc_savings()
            captured = capsys.readouterr().out.rstrip()
            _, decimal = captured.split('.')
            assert len(decimal) == 2

class Test_Prob4:
    def test_print_rate_and_steps(self, capsys):
        inputs = ['1000','12','5000']
        with mock.patch('builtins.input', side_effect=inputs):
            Prob4.calc_savings_rate()
            captured = capsys.readouterr().out.rstrip()
            Rate, Steps = captured.split('\n')
            assert ('Necessary savings rate is:' in Rate and 'Steps taken to find solution:' in Steps)

    def test_Example1(self, capsys):
        income = 1000
        months = 12
        des_savings = 5000
        inputs = [str(income),str(months), str(des_savings)]
        with mock.patch('builtins.input', side_effect=inputs):
            Prob4.calc_savings_rate()
            captured = capsys.readouterr().out.rstrip()
            Rate, Steps = captured.split('\n')
            _, s_rate = Rate.split(':')
            s_rate = float(s_rate)
            i_rate = 0.03/12
            calc_savings = s_rate * income / i_rate * (math.exp(i_rate * months)-1)
            assert abs(calc_savings - des_savings) <= 30 

    def test_Example2(self, capsys):
        income = 1500
        months = 18
        des_savings = 6000
        inputs = [str(income),str(months), str(des_savings)]
        with mock.patch('builtins.input', side_effect=inputs):
            Prob4.calc_savings_rate()
            captured = capsys.readouterr().out.rstrip()
            Rate, Steps = captured.split('\n')
            _, s_rate = Rate.split(':')
            s_rate = float(s_rate)
            i_rate = 0.03/12
            calc_savings = s_rate * income / i_rate * (math.exp(i_rate * months)-1)
            assert abs(calc_savings - des_savings) <= 30

    def test_Example3(self, capsys):
        income = 1000
        months = 12
        des_savings = 25000
        inputs = [str(income),str(months), str(des_savings)]
        with mock.patch('builtins.input', side_effect=inputs):
            Prob4.calc_savings_rate()
            captured = capsys.readouterr().out.rstrip()
            Rate, Steps = captured.split('\n')
            _, s_rate = Rate.split(':')
            assert s_rate.strip() == 'Impossible'

    def test_3000_24_10000(self, capsys):
        income = 3000
        months = 24
        des_savings = 15000
        inputs = [str(income),str(months), str(des_savings)]
        with mock.patch('builtins.input', side_effect=inputs):
            Prob4.calc_savings_rate()
            captured = capsys.readouterr().out.rstrip()
            Rate, Steps = captured.split('\n')
            _, s_rate = Rate.split(':')
            s_rate = float(s_rate)
            i_rate = 0.03/12
            calc_savings = s_rate * income / i_rate * (math.exp(i_rate * months)-1)
            assert abs(calc_savings - des_savings) <= 100
