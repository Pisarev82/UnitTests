import pytest

from sem_6 import NumsLists


@pytest.fixture
def list1():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def list2():
    return [5, 6, 7, 8, 9]

def test_averages(list1, list2):
    list_ = NumsLists(list1, list2)
    assert list_.get_lists_averages() == (3, 7)


def test_first_more(list1, list2, capfd):
    list_ = NumsLists(list2, list1)
    list_.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Первый список большее'


def test_second_more(list1, list2, capfd):
    list_ = NumsLists(list1, list2)
    list_.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Второй список большее'


def test_equal(list1, capfd):
    list_ = NumsLists(list1, list1)
    list_.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'списки равны'