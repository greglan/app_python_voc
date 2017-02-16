# -*- coding: utf-8 -*-

import re

class Translation:
    def __init__(this, line, scoreSep, wordSep, score_min, score_max):
        this.swapped = False                                                    # Direction of translation. Default: order in the file.
        this.scoreSep = scoreSep
        this.wordSep = wordSep
        this.score_min=score_min
        this.score_max=score_max
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
        return str(this.score)+this.scoreSep+this.question+this.wordSep+this.answer+'\n'
    
    def check(this, answer):
        """ Check if the provided answer is correct """
        if answer in this.answers:
            this.incScore()
            otherAnswers = None
            if len(this.answers)!=1:
                this.answers.remove(answer)
                otherAnswers = "Other answers: "+str(this.answers)
            return True, otherAnswers
        else:
            this.decScore()
            return False, None
    
    def incScore(this):
        if this.score < this.score_max:
            this.score += 1
    
    def decScore(this):
        if this.score >= this.score_min+5:
            this.score -= 5