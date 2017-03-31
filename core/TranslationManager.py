# -*- coding: utf-8 -*-

import math
import random
from core import Translation


class TranslationManager:
    def __init__(this, score_sep, word_sep, score_min, score_max, score_minus=5, score_bonus=1):
        this.score_sep = score_sep
        this.word_sep = word_sep
        this.score_min = score_min
        this.score_max = score_max
        this.total_translations = 0
        this.cTranslation = None  # Active translation
        this.translations = [[] for k in range(this.score_max+1)]
    
    def get_total_translations(this):
        return this.total_translations
    
    def add(this, line):
        """ Add the line to the list of translations. Sort it by its score. """
        t = Translation.Translation(line, this.score_sep, this.word_sep, this.score_min, this.score_max)
        this.translations[t.score].append(t)
    
    def swap_languages(this):
        for i in range(this.score_max+1):
            for t in this.translations[i]:
                t.swap()
    
    def new_question(this):
        """ Choose low scores before. Then random. """
        k = 0
        while k == 0:                                                           # Loop until a word in found
            score = math.floor(random.expovariate(0.25))
            while score > this.score_max:                                       # Loop until a valid score is found.
                score = math.floor(random.expovariate(0.25))
            k = len(this.translations[score])
        this.cTranslation = this.translations[score][random.randint(0, k-1)]
    
    def get_question(this):
        return this.cTranslation.get_question()
    
    def check(this, answer):
        result = this.cTranslation.check(answer)
        score = this.cTranslation.score
        if result[0]:
            this.cTranslation.inc_score()
        else:
            this.cTranslation.dec_score()
        this.translations[score].remove(this.cTranslation)
        this.translations[this.cTranslation.score].append(this.cTranslation)
        return result
    
    def get_answer(this):
        return this.cTranslation.get_answer()
    
    def save_scores(this, filepath):
        f = open(filepath, 'w', encoding='utf-8')
        lines = []
        
        for i in range(this.score_max+1):
            for t in this.translations[i]:
                lines.append(t.to_string())
        
        lines.sort()
        
        for line in lines:
            f.write(line)
    
        f.close()
