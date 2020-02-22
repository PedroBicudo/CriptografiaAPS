from criptografiaAps import Vernam
import unittest


class VernamTest(unittest.TestCase):
    
    def setUp(self):
        self.vernam = Vernam()

    def test_is_hex(self):
        self.assertTrue(
            self.vernam._is_hex('0xFF')
        )

        self.assertTrue(
            self.vernam._is_hex('FF')
        )
        
        self.assertFalse(
            self.vernam._is_hex('0xZZ')
        )

        self.assertFalse(
            self.vernam._is_hex('ZZ')
        )

        # Raises
        with self.assertRaises(ValueError) as error:
            self.vernam._is_hex('0x440xAA')
        
        self.assertTrue(
            'Apenas um hexadecimal deve ser inserido.'
            in str(error.exception)
            )
