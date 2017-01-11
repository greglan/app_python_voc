# -*- coding: utf-8 -*-
#!/usr/bin/env python

#TODO: Write new scores to file
#TODO: handle exit signal
#TODO: add optionnal parenthesis
#TODO: ask word with low scores

import os
import random
import re

score_max=99
score_min=0

class App:
    def __init__(this, filepath):
        this.wordList = []
        this.filepath = filepath
        
        f = open(filepath)
        for line in f:
            this.wordList.append(Translation(line.strip()))
        
        this.len_wordList = len(this.wordList)    
        this.index = 0
        
        f.close()
    
    
    def run(this):
        this.running = True
        while this.running:
            this.newQuestion()
            answer = input()
            while(not this.answer(answer)):
                print("Wrong")
                answer = input()

    
    def swapLanguages(this):
        for i in range(len(this.wordList)):
            this.wordList[i].swap()
    
    
    def newQuestion(this):
        print()
        this.index = random.randint(0, this.len_wordList-1)
        print(this.wordList[this.index].getQuestion())
    
    
    def answer(this, answer):
        if answer == 'r':
            this.printAnswer()
            return True
        elif answer == 'c':
            this.swapLanguages()
            return True
        elif answer == 'q':
            this.running = False
            this.saveScores()
            return True
        else:
            return this.wordList[this.index].check(answer)
    
    
    def printAnswer(this):
        print(this.wordList[this.index].getAnswer())
    
    
    def saveScores(this):
        f = open(this.filepath, 'w')
        lines = []
        
        for i in range(this.len_wordList):
            lines.append(this.wordList[i].toString())
        lines.sort()
        
        for line in lines:
            f.write(line)
    
        f.close()
        

class Translation:
    def __init__(this, line):
        this.swapped = False
        line = line.split('-')
        this.score = int(line[0])
        
        line = line[1].split('=')
        this.question = line[0]
        this.answer = line[1]
        this.answers = re.split(",|/", this.answer)
    
    def swap(this):
        this.swapped = not this.swapped
        this.question, this.answer = this.answer, this.question
        this.answers = re.split(",|/", this.answer)
    
    def getQuestion(this):
        return this.question
    
    def getAnswer(this):
        return this.answer
    
    def toString(this):
        if this.swapped:
            this.swap()
        return str(this.score)+'-'+this.question+'='+this.answer+'\n'
    
    def check(this, answer):
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
        if this.score >= score_min+5:
            this.score -= 5
    
        
app = App('s.txt')
app.run()