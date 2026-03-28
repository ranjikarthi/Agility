from app import add

def test_add():
    result = add(2, 3)
    print(result)
    assert result == 5
