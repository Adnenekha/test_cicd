from src.preprocess import Loader
import pytest

# class TestPreprocess:

#     def test_laoding(self):
#         assert Loader("Verrens-Arvey").filter_commune().shape[0] != 0




@pytest.mark.parametrize('value, key', [(2,3),(3,4)], )   
def test_round_down_lesser_half(value, key):
    result = value
    assert result == key - 1



@pytest.fixture
def first_fixture():
    data = {"first_name" : "Ranga",
            "name" : "Gonnage"
    }
    return data

def test_with_first_fxture(first_fixture):
    print(first_fixture)
    assert first_fixture["first_name"] == "Ranga"
    assert first_fixture["name"] == "Gonnage"