# -*- coding: utf-8 -*-

from core import TranslationManager

class App:
    def __init__(this, filepath, scoreSep='=', wordSep='='):
        this.TM = TranslationManager.TranslationManager(scoreSep, wordSep)
        this.filepath = filepath
        
        f = open(filepath, encoding='utf-8')
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