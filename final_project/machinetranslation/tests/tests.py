import unittest
from translator import english_to_french , french_to_english

class testTranslator (unittest.TestCase):

    def test_null_english_to_french(self):
        self.assertNotEqual(english_to_french('None'),'')

    def test_null_french_to_english(self):
        self.assertNotEqual(french_to_english('None'),'')

    def test_bonjour_french_to_english(self):
        self.assertEqual('Hello', french_to_english('Bonjour'))

    def test_hello_english_to_french(self):
        self.assertEqual('Bonjour', english_to_french('Hello'))

if  __name__=='__main__':
    unittest.main()
