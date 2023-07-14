import sys

def test_a():
    assert True

def test_b():
    assert 'abc' in 'abcd'

def test_c():
    assert ('win' in sys.platform),"该段代码只能在Windows系统下运行"
