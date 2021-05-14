import pytest 
import wordcounter

def test_space():
    #Pass Test
    assert wordcounter.determineWordCount("The cow is black and white") == 6, "pass test"
    #Fail Test
    #assert wordcounter.determineWordCount("The cow is black and white") == 5, "fail test"
def test_withNoSpace():
    #Pass Test
    assert wordcounter.determineWordCount("Thecowisblackandwhite") == "Not a valid sentence", "pass test"
    #Fail Test
    #assert wordcounter.determineWordCount("The cow is black and white") == 6, "fail test"

   
