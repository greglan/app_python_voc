# -*- coding: utf-8 -*-

import math
import random
from core import Translation

class TranslationManager:
    def __init__(this, scoreSep, wordSep, score_min, score_max, scoreMinus=5, scoreBonus=1):
        this.scoreSep = scoreSep
        this.wordSep = wordSep
        this.score_min=score_min
        this.score_max=score_max
        this.totalTranslations = 0
        this.cTranslation = None                                                # Active translation
        this.translations = [ [] for k in range(this.score_max+1) ]
    
    def gettotalTranslations(this):
        return this.totalTranslations
    
    def add(this, line):
        """ Add the line to the list of translations. Sort it by its score. """
        t = Translation.Translation(line, this.scoreSep, this.wordSep, this.score_min, this.score_max)
        this.translations[t.score].append(t)
    
    def swapLanguages(this):
        for i in range(this.score_max+1):
            for t in this.translations[i]:
                t.swap()
    
    def newQuestion(this):
        """ Choose low scores before. Then random. """
        k=0
        while k == 0:                                                           # Loop until a word in found
            score = math.floor(random.expovariate(0.25))
            while score > this.score_max:                                       # Loop until a valid score is found.
                score = math.floor(random.expovariate(0.25))
            k = len(this.translations[score])
        this.cTranslation = this.translations[score][random.randint(0, k-1)]
    
    def getQuestion(this):
        return this.cTranslation.getQuestion()
    
    def check(this, answer):
        result = this.cTranslation.check(answer)
        score = this.cTranslation.score
        if result[0]:
            this.cTranslation.incScore()
        else:
            this.cTranslation.decScore()
        this.translations[score].remove(this.cTranslation)
        this.translations[this.cTranslation.score].append(this.cTranslation)
        return result
    
    def getAnswer(this):
        return this.cTranslation.getAnswer()
    
    def saveScores(this, filepath):
        f = open(filepath, 'w', encoding='utf-8')
        lines = []
        
        for i in range(this.score_max+1):
            for t in this.translations[i]:
                lines.append(t.toString())
        
        lines.sort()
        
        for line in lines:
            f.write(line)
    
        f.close()