import pytest
from select_helper import SelectOptions


def test_select_text_java():
    obj1 = SelectOptions()
    assert obj1.select_by_text("dropdown","Java"), 'Failed due to text'


def test_select_text_python():
    obj1 = SelectOptions()
    assert obj1.select_by_text("dropdown","Python"), 'Failed due to text'


def test_select_text_react():
    obj1 = SelectOptions()
    assert obj1.select_by_text("dropdown","React"), 'Failed due to text'


def test_select_text_azure():
    obj1 = SelectOptions()
    assert obj1.select_by_text("dropdown","Azure"), 'Failed due to text'


def test_select_index_1():
    obj1 = SelectOptions()
    assert obj1.select_by_index(1), 'Failed due to text'


def test_select_index_2():
    obj1 = SelectOptions()
    assert obj1.select_by_index(2), 'Failed due to text'


def test_select_index_3():
    obj1 = SelectOptions()
    assert obj1.select_by_index(3), 'Failed due to text'


def test_select_index_4():
    obj1 = SelectOptions()
    assert obj1.select_by_index(4), 'Failed due to text'


def test_select_value_1():
    obj1 = SelectOptions()
    assert obj1.select_by_value("1"), 'Failed due to text'


def test_select_value_2():
    obj1 = SelectOptions()
    assert obj1.select_by_value("2"), 'Failed due to text'


def test_select_value_3():
    obj1 = SelectOptions()
    assert obj1.select_by_value("3"), 'Failed due to text'


def test_select_value_4():
    obj1 = SelectOptions()
    assert obj1.select_by_value("4"), 'Failed due to text'


def test_select_value_5():
    obj1 = SelectOptions()
    assert obj1.select_by_value("5"), 'Failed due to text'