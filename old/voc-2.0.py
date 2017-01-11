# -*- coding: utf-8 -*-
#!/usr/bin/env python
#TODO: Optionnal parenthesis
#TODO: Windows plateform
#TODO: Pretty_print: Remove given answer from answers
#TODO: Pretty_print: ,rep2,rép3. Remove first coma
#TODO: Pretty-print: adamant=catégorique,ferme/inflexible. Given answer: ferme. Answer: ,ferme/inflexible
import os
import random

class App:
    def __init__(self,english_mode=True):
        self.run = True
        self.android = True         # Android device?
        self.errors_count = 0       # Number of errors made during runtime
        self.answer_ok = False      # Good answer or not
        self.answer_ok_key = (0,0)
        self.words_number = 0        # Number of words
        self.answer = ''             # Hold the input
        self.mode_toforeign = 0      #French to target
        self.words = [[],[]]         # Words[0]: French. Words[0][k] = [[trad1,synontrad1],[trad2,synotrad2]]
        self.chosen_word = 0
        
        # Check the device type
        if not os.path.isdir('/sdcard'):
            self.android = False
            #os.chdir('/home/herbertz0/Documents/Google Drive/Culture/Langues')
            os.chdir('E:/Documents/Google Drive/Culture/Langues')
        else:
            os.chdir('/sdcard')
    
        f = open('s.txt', 'r')
        
        # Copy the words
        for line in f:
            line = line.strip()                     # Remove any unwanted character
            line = line.split('=')
                    
            # English words
            line[0] = line[0].split(',')
            n = len(line[0])
            for i in range(n):
                line[0][i] = line[0][i].split('/')
            self.words[0].append(line[0])
            
            # French words
            line[1] = line[1].split(',')
            n = len(line[1])
            for i in range(n):
                line[1][i] = line[1][i].split('/')
            self.words[1].append(line[1])
        
        f.close()
        
        self.words_number = len(self.words[0])
        
        print('Android device: '+str(self.android))
        
        
    def new_word(self):
        print('-------------')
        self.chosen_word = random.randint(0,self.words_number-1)
        self.pretty_print(self.words[self.mode_toforeign][self.chosen_word])
    
    def get_answer(self):
        #raw_input()
        self.answer = input()
    
    def check(self):
        self.answer_ok = False
        i=0
        for e in self.words[(self.mode_toforeign+1)%2][self.chosen_word]:
            # Remove ()
            e_f = []
            for w in e:
                try:
                    i = w.index('(')
                except ValueError:
                    i = 0
                if i > 0:
                    e_f.append(w[:i-1])
                else:
                    e_f.append(w)
            
            if e_f.count(self.answer)>0:
                self.answer_ok = True
                self.answer_ok_key = (i,e_f.index(self.answer))
            i+=1
        
    def pretty_print(self,word):
        s = ''
        for i in range(len(word)):
            for j in range(len(word[i])): # For each synonym
                s+= word[i][j]
                s+= '/'
            s = s[:-1]
            s+= ','
        s = s[:-1]
        print(s)

    def exit(self):
        print('Errors: '+str(self.errors_count))


app = App()
app.new_word()
while app.run:
    app.get_answer()
    app.check()
    if app.answer_ok:
        print('Other answers:')
        app.pretty_print(app.words[(app.mode_toforeign+1)%2][app.chosen_word])
        print()
        app.new_word()
        
    elif app.answer=='r' or app.answer=='':
        app.pretty_print(app.words[(app.mode_toforeign+1)%2][app.chosen_word])
        print()
        app.new_word()
        app.errors_count += 1
        
    elif app.answer=='q':
        app.run = False
  
    elif app.answer=='m':
        app.mode_toforeign = (app.mode_toforeign+1)%2
        print()
        app.new_word()
            
    else:
        print('Wrong!')
        print()
        app.errors_count += 1
        
app.exit()