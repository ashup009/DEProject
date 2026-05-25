from deproject.main import add, mul


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_mul():
    assert mul(1, 2) == 2
    assert mul(-1, 1) == -1
    assert mul(-1, -1) == 1