# -*- coding: utf-8 -*-


import importlib
from core import TranslationManager


class App:
    def __init__(this, filepath, score_sep='=', word_sep='=', gui='console', score_min=0, score_max=20, score_minus=5,
                 score_bonus=1):
        this.TM = TranslationManager.TranslationManager(score_sep, word_sep, score_min, score_max, score_minus,
                                                        score_bonus)
        this.filepath = filepath
        this.score_min = score_min
        this.score_max = score_max
        this.gui = importlib.import_module('gui.' + gui)
        this.running = False
        this.answer = "Default answer"

        f = open(filepath, encoding='utf-8')
        for line in f:
            this.TM.add(line.strip())
        this.index = 0

        f.close()

    def run(this):
        this.running = True
        while this.running:
            this.new_question()
            while not this.process_answer():
                this.gui.info("Wrong")

    def get_answer(this):
        this.answer = input()

    def new_question(this):
        this.TM.new_question()
        this.gui.question(this.TM.get_question())

    def process_answer(this):
        this.get_answer()
        if this.answer == 'r':
            this.print_answer()
            return True
        elif this.answer == 'c':
            this.TM.swap_languages()
            return True
        elif this.answer == 'q':
            this.running = False
            this.save_scores()
            return True
        else:
            result = this.TM.check(this.answer)
            if result[1] is not None:
                print('result[1]')
                this.gui.info(result[1])
            return result[0]

    def print_answer(this):
        this.gui.answer(this.TM.get_answer())

    def save_scores(this):
        this.TM.save_scores(this.filepath)
