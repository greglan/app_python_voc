# -*- coding: utf-8 -*-

import importlib
from core import TranslationManager

class App:
    def __init__(this, filepath, scoreSep='=', wordSep='=', gui='console', score_min=0, score_max=20, scoreMinus=5, scoreBonus=1):
        this.TM = TranslationManager.TranslationManager(scoreSep, wordSep, score_min, score_max, scoreMinus, scoreBonus)
        this.filepath = filepath
        this.score_min=score_min
        this.score_max=score_max
        this.gui = importlib.import_module('gui.'+gui)
        
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
                this.gui.info("Wrong")
    
    
    def getAnswer(this):
        this.answer = input()    
    
    def newQuestion(this):
        this.TM.newQuestion()
        this.gui.question( this.TM.getQuestion() )
    
    
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
            result =  this.TM.check(this.answer)
            if result[1] != None:
                print('result[1]')
                this.gui.info(result[1])
            return result[0]
    
    def printAnswer(this):
        this.gui.answer( this.TM.getAnswer() )
    
    
    def saveScores(this):
        this.TM.saveScores(this.filepath)