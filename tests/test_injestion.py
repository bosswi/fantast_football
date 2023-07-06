import pytest
from data_injestion.injestion import Injestor

def test_init():
    injest = Injestor()
    assert injest.yahoo_key == "my_key"