"""简单测试，验证测试框架正常工作"""
import pytest


def test_basic_addition():
    """测试基本加法运算"""
    assert 1 + 1 == 2
    assert 2 + 3 == 5
    assert 10 + (-5) == 5


def test_string_operations():
    """测试字符串操作"""
    s1 = "hello"
    s2 = "world"
    assert s1 + s2 == "helloworld"
    assert len(s1) == 5
    assert s1.upper() == "HELLO"


def test_list_operations():
    """测试列表操作"""
    lst = [1, 2, 3, 4, 5]
    assert len(lst) == 5
    assert lst[0] == 1
    assert lst[-1] == 5
    assert sorted(lst) == [1, 2, 3, 4, 5]


if __name__ == "__main__":
    pytest.main([__file__])