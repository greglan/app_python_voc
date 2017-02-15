# -*- coding: utf-8 -*-

import math
import random
from core import Translation

score_max=4
score_min=0

class TranslationManager:
    def __init__(this):
        this.totalTranslations = 0
        this.cTranslation = None                                                # Current translation
        this.translations = [ [] for k in range(score_max+1) ]
    
    def gettotalTranslations(this):
        return this.totalTranslations
    
    def add(this, line):
        """ Add the line to the list of translations. Sort it by its score. """
        t = Translation.Translation(line)
        this.translations[t.score].append(t)
    
    def swapLanguages(this):
        for i in range(score_max+1):
            for t in this.translations[i]:
                t.swap()
    
    def newQuestion(this):
        """ Choose low scores before. Then random. """
        k=0
        while k == 0:                                                           # Loop until a word in found
            score = math.floor(random.expovariate(1.5))
            while score > score_max:                                            # Loop until a valid score is found.
                score = math.floor(random.expovariate(1.5))
            k = len(this.translations[score])
        this.cTranslation = this.translations[score][random.randint(0, k-1)]    
    
    def getQuestion(this):
        return this.cTranslation.getQuestion()
    
    def check(this, answer):
        return this.cTranslation.check(answer)
    
    def getAnswer(this):
        return this.cTranslation.getAnswer()
    
    def saveScores(this, filepath):
        f = open(filepath, 'w', encoding='utf-8')
        lines = []
        
        for i in range(score_max+1):
            for t in this.translations[i]:
                lines.append(t.toString())
        
        lines.sort()
        
        for line in lines:
            f.write(line)
    
        f.close()