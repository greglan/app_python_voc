# -*- coding: utf-8 -*-

import re

score_max=4
score_min=0

class Translation:
    def __init__(this, line, scoreSep, wordSep):
        this.swapped = False                                                    # Direction of translation. Default: order in the file.
        
        firstSepIndex = line.index(scoreSep)                                    # Where is the score sep located?
        this.score = int(line[:firstSepIndex])                                  # Get score
        line = line[firstSepIndex+1:].split(wordSep)                            # New line contains the translation without the scores
        
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
        """
        if answer in this.answers:
            if len(this.answers)!=1:
                print("Other answers: ")
                this.answers.remove(answer)
                print(this.answers)
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