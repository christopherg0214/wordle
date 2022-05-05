# -*- coding: utf-8 -*-
"""
Created on Wed May  1 18:26:58 2022

@author: cgarr
"""

import wordle
import random
import ml

def taperIterationTests():
    taper = 0.90
    for i in range(200):
        guessCount = []
        avg = 0
        for j in range(10):
            guess = ml.FreqAI("training.txt","maxFreq", taper)
            guessCount.append(guess)
        
        avg = (sum(guessCount)/len(guessCount))
        print(round(taper,3),",",avg)
        taper += 0.002