from criptografiaAps.vigenere import CHARACTERS
from criptografiaAps.vigenere import Vigenere
from string import ascii_lowercase
from operator import add, sub
import unittest

class VigenereTest(unittest.TestCase):
    def setUp(self):
        self.vigenere = Vigenere()
    
    def test_letter_getter(self):
        self.assertEqual(
            self.vigenere._get_letter(1, 10, add, ascii_lowercase), 
            'l'
        )

        self.assertEqual(
            self.vigenere._get_letter(1, 10, sub,  ascii_lowercase),
            'r'
        )
    
    def test_word_getter(self):
        self.assertEqual(
            self.vigenere._get_word(
                'teste', 'abcde', lambda x,y: x+y, CHARACTERS
            ),
            'tfuwi'
        )

        self.assertEqual(
            self.vigenere._get_word(
                'tfuwi', 'abcde', lambda x,y: x-y, CHARACTERS
            ),
            'teste'
        )
    