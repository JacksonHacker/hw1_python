# test_with_unittest.py

from unittest import TestCase
from src.main.python.edu.arizona.cs.invertedindex import InvertedIndex

class TryTesting(TestCase):
    docs="src/main/resources/Docs.txt"

    def test_always_passes(self):
        ans_qn5_1=InvertedIndex(self.docs).q5_1()
        assert type(ans_qn5_1) is not None
        assert type(ans_qn5_1) is list
        assert len(ans_qn5_1) >0

        assert (ans_qn5_1[0]) is not None
        assert (type(ans_qn5_1[0])) is str
        assert (ans_qn5_1[0]) == "Doc1"

        assert (ans_qn5_1[1]) is not None
        assert (type(ans_qn5_1[1])) is str
        assert (ans_qn5_1[1]) == "Doc4"



    def test_always_fails(self):
        assert True