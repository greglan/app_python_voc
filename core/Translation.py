# -*- coding: utf-8 -*-

import re


class Translation:
    def __init__(this, line, score_sep, word_sep, score_min, score_max, score_minus=5, score_bonus=1):
        this.swapped = False   # Direction of translation. Default: order in the file.
        this.score_sep = score_sep
        this.word_sep = word_sep
        this.score_min = score_min
        this.score_max = score_max
        this.score_minus = score_minus
        this.score_bonus = score_bonus
        first_sep_index = line.index(score_sep)          # Where is the score sep located?
        this.score = int(line[:first_sep_index])        # Get score
        line = line[first_sep_index+1:].split(word_sep)  # New line contains the translation without the scores

        this.question = line[0]  # String
        this.answer = line[1]    # String
        this.answers = []
        this.build_answer_list(this.answer)

    def build_answer_list(this, s):
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
        this.build_answer_list(this.answer)
    
    def get_question(this):
        return this.question
    
    def get_answer(this):
        return this.answer
    
    def to_string(this):
        """ Returns the corresponding string to be written in a file """
        if this.swapped:
            this.swap()
        return str(this.score)+this.score_sep + this.question + this.word_sep + this.answer + '\n'
    
    def check(this, answer):
        """ Check if the provided answer is correct """
        if answer in this.answers:
            other_answers = None
            if len(this.answers) != 1:
                this.answers.remove(answer)
                other_answers = "Other answers: "+str(this.answers)
            return True, other_answers
        else:
            return False, None
    
    def inc_score(this):
        if this.score < this.score_max:
            this.score += this.score_bonus
    
    def dec_score(this):
        if this.score >= this.score_min+5:
            this.score -= this.score_minus
