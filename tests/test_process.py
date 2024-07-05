import sys
sys.path.insert(0, '../')

from src.preprocess import Loader

class TestPreprocess:

    def test_laoding(self):
        assert Loader("Verrens-Arvey").filter_commune().shape[0] != 0

