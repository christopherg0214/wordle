# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:45:51 2022

@author: cgarr
"""

import wordle
import random
import testing
from collections import Counter

"untrained AI"
def untrainAI(filename):
    
    wrdl = wordle.wordle()
    wrdl.createWordle(filename)
    solved = False
    
    #untrained ai guesses random possible word
    while True:
        if(len(wrdl.possibleWords)):
            guess = random.choice(wrdl.possibleWords)
            solved = wrdl.guessWord(guess)
            if solved:
                return wrdl.guessCounter
        else:
            return -1
            


def randAI(filename):
    
    wrdl = wordle.wordle()
    wrdl.createWordle(filename)

    
    while True:
        if(len(wrdl.possibleWords)):
            
            guess = random.choice(wrdl.possibleWords)
            solved = wrdl.guessWord(guess)
            if solved:
                return wrdl.guessCounter
        else:
            return -1
    
    return

def FreqAI(filename, freqType, taper):
    
    wrdl = wordle.wordle()
    wrdl.createWordle(filename)

    
    solved = False
    while True:
        if(len(wrdl.possibleWords)):
            guess = ""
            if freqType == "maxFreq":
                guess = maxFreq(taper,wrdl)
            solved = wrdl.guessWord(guess)
            if solved:
                return wrdl.guessCounter
        else:
            return -1
    
    return

"for testing purposes"
def human(filename):
    
    wrdl = wordle.wordle()
    wrdl.createWordle(filename)
    
    for i in range(5):
        guess = input("")
        solved = wrdl.guessWord(guess)
        print(wrdl.lastGuess)
        if solved:
            print("Game won")
            return
    print("Game lost")
    return

    
#scores words by relative letter frequency
#returns word with best score
#taper adjusts penalty for words with repeat letters
def maxFreq(taper,wrdl):
    
    
    #convert file from strings to one string
    bigString = ""
    for words in wrdl.possibleWords:
        bigString += words
        
    #create dictionary of total character counts
    countDict = Counter(bigString)
    
    
    #calculate score for each word
    scores = [0] * len(wrdl.possibleWords)
    
    index = 0
    for word in wrdl.possibleWords:
        
        #check for duplicate letters
        dupe = False
        for letter in range(5):
            for nextLetter in range(letter + 1,5):
                if word[nextLetter] == word[letter]:
                    dupe = True
                    

            for letter in range(5):
                scores[index] += countDict.get(word[letter])
                
            if dupe:
                scores[index] /= taper
        index += 1
    
    #return word with biggest score
    indexMaxVal = scores.index(max(scores))
    
    return wrdl.possibleWords[indexMaxVal]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    