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

        # Raises ValueError
        with self.assertRaises(ValueError) as error:
            self.vernam._is_hex('0x440xAA')
        
        self.assertTrue(
            'Apenas um hexadecimal deve ser inserido.'
            in str(error.exception)
            )

    def test_hex_to_char(self):
        self.assertEqual(
            self.vernam._hex_to_chr('0x74:0x65:0x73:0x74:0x65'),
            list('teste')
        )
    
    def test_vernam(self):
        self.assertEqual(
            self.vernam._vernam('teste', 'abcde'),
            [21, 7, 16, 16, 0]
        )

        # Raises
        with self.assertRaises(TypeError) as error_msg:
            self.vernam._vernam(1234, 'teste')
        
        with self.assertRaises(TypeError) as error_key:
            self.vernam._vernam('teste', 12345)

        with self.assertRaises(ValueError) as error_size:
            self.vernam._vernam('teste', 'test')

        self.assertTrue(
            "'msg' devem ser do tipo string ou list."
            in str(error_msg.exception)
        )

        self.assertTrue(
            "key' devem ser do tipo string ou list."
            in str(error_key.exception)
        )

        self.assertTrue(
            "'key' deve ter tamanho maior ou igual a 'msg'."
            in str(error_size.exception)
        )


    def test_encript(self):
        self.assertEqual(
            self.vernam.encript('teste', 'abcde'),
            '0x15:0x7:0x10:0x10:0x0'
        )

    def test_decript(self):
        self.assertEqual(
            self.vernam.decript('0x15:0x7:0x10:0x10:0x0', 'abcde'),
            'teste'
        )
