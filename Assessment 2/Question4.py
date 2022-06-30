
import unittest
import Question3
class TestPalidrome(unittest.TestCase):
    #This is the case when it is a palindrome
    def test_palindrome(self):
        test_word='aba'
        self.assertTrue(Question3.valid_palindrome(test_word))

    #This is the case when we have empty string
    def test_palindrome_empty(self):
        test_word=''
        self.assertTrue(Question3.valid_palindrome(test_word))

    #This is the case when it is not a palindrome
    def test_palindrome_same(self):
        test_word='aab'
        self.assertFalse(Question3.valid_palindrome(test_word))