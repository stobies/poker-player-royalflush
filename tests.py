from hand import *
from card import *

def test_hand():

    flush = [Card(2, "D"), Card(5, "D"), Card(3, "D"), Card(4, "D"), Card(8, "D"), Card(9, "H"), Card(8, "H")]
    assert Hand.get_flush(flush) != ''

test_hand()