from criptografiaAps import Caesar
import unittest

class CaesarTest(unittest.TestCase):
    def setUp(self):
        self.caesar = Caesar()
        self.custom_alpha = "qwertyuiopasdfghjklzxcvbnm"

    def test_cript_action(self):
        self.assertEqual(self.caesar.get_action(True).__name__, "encript")
        self.assertEqual(self.caesar.get_action(False).__name__, "decript")

    def test_encript(self):
        self.assertEqual(self.caesar.encript("abc", 1), "bcd")
        self.assertEqual(self.caesar.encript("testçtest", 1), "uftuçuftu")
    
    def test_decript(self):
        self.assertEqual(self.caesar.decript("bcd", 1), "abc")
        self.assertEqual(self.caesar.decript("uftuçuftu", 1), "testçtest")
    
    def test_rot_letter_with_custom_alphabet(self):
        self.assertEqual(
            self.caesar._get_rot_letter(
                'a', 1, lambda x, y: x+y, self.custom_alpha
            ), 's'
        )

        self.assertEqual(
            self.caesar._get_rot_letter(
                'a', 1, lambda x, y: x-y, self.custom_alpha
            ), 'p'
        )


    

        


