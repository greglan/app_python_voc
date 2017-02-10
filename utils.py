# -*- coding: utf-8 -*-

import math
import random
import re

score_max=4
score_min=0

class Translation:
    def __init__(this, line):
        this.swapped = False                                                    # Direction of translation. Default: order in the file.
        line = line.split('-')
        this.score = int(line[0])                                               # Contains the score of the current translation
        
        line = line[1].split('=')
        this.question = line[0]                                                 # String
        this.answer = line[1]                                                   # String
        this.buildAnswerList(this.answer)
    
    def buildAnswerList(this, s):
        """ List of the possible answers 
            Removes the parenthesis
        """
        this.answers = re.split(",|/", s)
        for i in range(len(this.answers)):
            k = this.answers[i].find('(')
            if k != -1:
                this.answers[i] = this.answers[i][:k-1]
    
    def swap(this):
        """ Change the direction of the translation"""
        this.swapped = not this.swapped
        this.question, this.answer = this.answer, this.question
        this.buildAnswerList(this.answer)
    
    def getQuestion(this):
        return this.question
    
    def getAnswer(this):
        return this.answer
    
    def toString(this):
        """ Returns the corresponding string to be written in a file """
        if this.swapped:
            this.swap()
        return str(this.score)+'-'+this.question+'='+this.answer+'\n'
    
    def check(this, answer):
        """ Check if the provided answer is correct
            TODO: display the missing answers
        """
        if answer in this.answers:
            this.incScore()
            return True
        else:
            this.decScore()
            return False
    
    def incScore(this):
        if this.score < score_max:
            this.score += 1
    
    def decScore(this):
        if this.score >= score_min+2:
            this.score -= 2


class TranslationManager:
    def __init__(this):
        this.totalTranslations = 0
        this.cTranslation = None                                                # Current translation
        this.translations = [ [] for k in range(score_max+1) ]
    
    def gettotalTranslations(this):
        return this.totalTranslations
    
    def add(this, line):
        """ Add the line to the list of translations. Sort it by its score. """
        t = Translation(line)
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
        this.cTranslation = this.translations[score][random.randint(0, k)]      #FIXME: list index out of range
    
    def getQuestion(this):
        return this.cTranslation.getQuestion()
    
    def check(this, answer):
        return this.cTranslation.check(answer)
    
    def getAnswer(this):
        return this.cTranslation.getAnswer()
    
    def saveScores(this, filepath):
        f = open(filepath, 'w')
        lines = []
        
        for i in range(score_max+1):
            for t in this.translations[i]:
                lines.append(t.toString())
        
        lines.sort()
        
        for line in lines:
            f.write(line)
    
        f.close()
                
class App:
    def __init__(this, filepath):
        this.TM = TranslationManager()
        this.filepath = filepath
        
        f = open(filepath)
        for line in f:
            this.TM.add(line.strip())
        this.index = 0
        
        f.close()
    
    
    def run(this):
        this.running = True
        while this.running:
            this.newQuestion()
            while(not this.processAnswer()):
                print("Wrong")
    
    
    def getAnswer(this):
        this.answer = input()    
    
    def newQuestion(this):
        print()
        this.TM.newQuestion()
        print(this.TM.getQuestion())
    
    
    def processAnswer(this):
        this.getAnswer()
        if this.answer == 'r':
            this.printAnswer()
            return True
        elif this.answer == 'c':
            this.TM.swapLanguages()
            return True
        elif this.answer == 'q':
            this.running = False
            this.saveScores()
            return True
        else:
            return this.TM.check(this.answer)
    
    def printAnswer(this):
        print(this.TM.getAnswer())
    
    
    def saveScores(this):
        this.TM.saveScores(this.filepath)