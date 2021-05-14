import unittest
import wordcounter

class testWordCounter(unittest.TestCase):
    def test_space(self):
        #Pass Test
        self.assertEqual(wordcounter.determineWordCount("The cow is black and white"), 6)
        #Fail Test
        #self.assertEqual(wordcounter.determineWordCount("The cow is black and white"), 5)
    def test_withNoSpace(self):
        #Pass Test
        self.assertEqual(wordcounter.determineWordCount("Thecowisblackandwhite"), "Not a valid sentence")
        #Fail Test
        #self.assertEqual(wordcounter.determineWordCount("Thecowisblackandwhite"), 4)


if __name__ == '__main__':
    unittest.main()