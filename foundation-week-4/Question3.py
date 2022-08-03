

import unittest
from Question2 import ATM 


class TestClassATM(unittest.TestCase):

    def test_account_amount_set(self):
        atm = ATM('aaaa',200)
        test_result = atm.account_balance
        self.assertEqual(test_result, 200,'They are equal')


