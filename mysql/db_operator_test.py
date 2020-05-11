import pytest
from db_operator import DbOperator

x = DbOperator()

class TestDbOperator:
    def test_get_record(self):
        result = x.get_record(111)
        assert True == result


