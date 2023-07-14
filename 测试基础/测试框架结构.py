# 类型                                        规则
# setup_module/teardown_module              全局模块级  只被调用一次
# setup_class/teardown_class                类级，只在类中前后运行一次
# setup_function/teardown_function          函数级，在类外
# setup_method/teardown_methond             方法级，类中的每个方法执行前后
# setup/teardown                            在类中，运行在调用方法的前后 (重点)
def setup_module():
    print("模块准备：setup module")
def teardown_module():
    print("模块销毁：teardown module")
def test_case1():
    print("case1")

def setup_function():
    print("方法准备：setup function")

def teardown_function():
    print("方法销毁：teardown function")