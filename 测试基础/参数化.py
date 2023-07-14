# 参数化设计方法就是将模型中的定量信息变量化，
# 使之成为任意调整的参数对于变量化参数赋予不同数值，
# 就可得到不同大小和形状的零件模型
import pytest

#单参数
search_list=["张三","李四","王五","赵六"]
@pytest.mark.parametrize('name',search_list)
def test_search(name):
    assert name in search_list
#多参数 用例重命名ids
@pytest.mark.parametrize('test_input,expected',
                         [("3+5",8),("2+5",7),("4*4",16)],
                         ids=["number1","number2","number3"])
def test_search(test_input,expected):
    assert eval(test_input)==expected

#笛卡尔积
@pytest.mark.parametrize("wd",["java","pytest","python"])
@pytest.mark.parametrize("code",["gbk","utf-8","base-64"])
def test_dkej(wd,code):
    print(f"wd:{wd},code:{code}")