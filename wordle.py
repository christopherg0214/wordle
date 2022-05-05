# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:35:07 2022

@author: cgarr
"""

import random
import re
import copy

class wordle:
    #initialize
    def __init__(self):
        self.solution = ""
        self.guessCounter = 0
        self.streak = 0
        self.lastGuess = [0]*5
        self.possibleWords = []
        self.file = ""
        
    #creates a wordle of the word arguement
    def createWordle(self,filename):
        
        #reset guessCounter and known words
        self.guessCounter = 0
        self.lastGuess = [0]*5
            
        #open file and add all words to possible word list
        file = open(filename, "r")
        self.file = filename
        self.possibleWords = file.readlines()
        file.close()
        
        #pick random word to guess
        self.solution = random.choice(self.possibleWords)
                    
        return
    
    
    #updates wordle object to reflect guessed word
    def guessWord(self,guess):
        
        self.guessCounter += 1
        #if correct word return true
        if guess[:4] in self.solution:
            return True
        
        temp = copy.deepcopy(self.solution)
        #setup lastGuess based on accuracy of guess
        
        "green"
        tempS = ""
        for guessChar in range(5):
            
            
            #if the character matches the solution
            if guess[guessChar] == self.solution[guessChar]:
                
                tempS += guess[guessChar]
                self.lastGuess[guessChar] = 2
                temp = temp.replace(temp[guessChar],'=')
            
            else:
                
                tempS += "."
                    
                
                    
        #filter out words    
        regex = re.compile(tempS)
        self.possibleWords = [i for i in self.possibleWords if regex.match(i)]
            
        
            
        "yellow"
        for guessChar in range(5):
            
            tempS = ""
            #if the character is in the solution
            if guess[guessChar] in temp:
                
                #the letter exhists somewhere
                tempS += ".*" + guess[guessChar] + ".*"
                regex = re.compile(tempS)
                self.possibleWords = [i for i in self.possibleWords if regex.match(i)]
                self.lastGuess[guessChar] = 1
                tempS = ""
                
                #remove words where the letter exists in this case
                for currentChar in range(5):
                    
                    if guess[guessChar] == guess[currentChar]:
                        
                        tempS += guess[guessChar]
                    else:
                        tempS += "."
                        
                regex = re.compile(tempS)
                self.possibleWords = [i for i in self.possibleWords if not regex.match(i)]
                self.lastGuess[guessChar] = 1
                
                
                
        "gray"
        tempS = ""
        for guessChar in range(5):
            
            
            #if the character matches the solution
            if guess[guessChar] not in self.solution:
                
                tempS += guess[guessChar]
                self.lastGuess[guessChar] = -1
            
            else:
                
                tempS += "."
           
        #filter out words    
        regex = re.compile(tempS)
        self.possibleWords = [i for i in self.possibleWords if not regex.match(i)]
         