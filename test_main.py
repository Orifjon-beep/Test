import pytest


@pytest.fixture()
def befor_after():
    print("Befor test")
    yield None
    print("\nAfter test")


def test_demo1():
    assert 1 == 1

def test_demo2(befor_after):
    assert 2 == 2