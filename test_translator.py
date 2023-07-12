import unittest

from translator import englishtofrench, frenchtoenglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishtofrench("hello"),"Bonjour")
        self.assertEqual(englishtofrench("welcome"),"Bienvenue")
        self.assertEqual(englishtofrench("love"),"Amour")
        #self.assertEqual(englishtofrench(""),"error")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchtoenglish("Bonjour"),"hello")
        self.assertEqual(englishtogerman("Bienvenue"),"welcome")
        self.assertEqual(englishtogerman("Amour"),"love")

unittest.main()