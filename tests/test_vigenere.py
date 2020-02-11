from criptografiaAps import Vigenere
import unittest

class VigenereTest(unittest.TestCase):
    def setUp(self):
        self.vigenere = Vigenere()
