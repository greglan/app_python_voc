#TODO: Optionnal parenthesis
#TODO: Print well the answers
#TODO: If question=m1/m2, prints m1m2. Not good...
#TODO: Not all traductions are printed after the loop. answer_list is correct: answer_ok = always True


import os
import random

android = True          # Android device?
loop = True             # Continue program's loop
answer_ok = False       # Good answer or not
words_number = 0        # Number of words
prob = []               # Probability repartition
answer = ''             # Hold the input
answer_list = []        # Hold the list of all possible answers

mode_en = True #True for english
mode_toforeign = False #French to target
words_score = []
words_fr = []
words_target = []
cur_question = ''
cur_target = ''






def init():
    global android
    global words_number
    global prob
    
    global mode_en
    global words_fr
    global words_target
    global cur_word
    global cur_target
    global words_score
    
    
    # Empty the lists
    words_fr = []
    words_target = []
    prob = []

    
    # Check the device type
    if not os.path.isdir('/sdcard'):
        android = False
        os.chdir('/home/herbertz0/Documents/Google Drive/Culture')
    else:
        os.chdir('/sdcard')
    
    # Open the correct file according to the target language
    if mode_en:
        f = open('english.txt', 'r')
    else:
        f = open('spanish.txt', 'r')
    
    # Copy the words
    for line in f:
        line = line.strip()                     # Remove any unwanted character
        line = line.split('=')
        
        words_score.append(int(line[0]))        # Add scores
        
        # English words
        line[1] = line[1].split(',')
        n = len(line[1])
        for i in range(n):
            line[1][i] = line[1][i].split('/')
        words_target.append(line[1])
        
        # French words
        line[2] = line[2].split(',')
        n = len(line[2])
        for i in range(n):
            line[2][i] = line[2][i].split('/')
        words_fr.append(line[2])
    
    # Close the file
    f.close()
    
    # Set up global variable
    words_number = len(words_fr)
    
    # Create the prob law
    for k in range(1,words_number):
        prob+=[k for i in range(0,words_number-k)]


def exit():
    global words_number
    global words_score
    global words_target
    global words_fr
    
    # Open the correct file according to the target language
    if mode_en:
        f = open('english.txt', 'w')
    else:
        f = open('spanish.txt', 'w')
    
    # Lines formatting
    lines = []
    for k in range(words_number):
        
        # Write scores
        s = str(words_score[k])+'='
        
        # Foreign words
        for w in words_target[k]:
            s2 = ''
            for u in w:
                s2 += u+'/'
            s2 = s2[:-1]                    # Remove last '/'
            s += s2+','
        s = s[:-1]                          # Remove last ','
        s += '='                            # Replace it with separator
        
        # French words
        for w in words_fr[k]:
            s2 = ''
            for u in w:
                s2 += u+'/'
            s2 = s2[:-1]                    # Remove last '/'
            s += s2+','
        s = s[:-1]
        s += '\n'
        lines.append(s)        
    lines.sort()

    # Write data to file
    for line in lines:
        f.write(line)
    f.close()
    
    print('Bye!')

 
def new_word():
    global mode_toforeign
    global words_fr
    global words_target
    global prob
    global chosen_word
    global answer_ok
    global answer_list
    
    global cur_question
    global cur_target
    
    # New answer false
    answer_ok = False
    
    # Choose new word
    chosen_word = prob[random.randint(0,len(prob)-1)]
    
    # According to the language
    if mode_toforeign:
        cur_question = words_fr[chosen_word]
        cur_target = words_target[chosen_word]
    else:
        cur_question = words_target[chosen_word]
        cur_target = words_fr[chosen_word]
    
    # Format the question
    s = ''
    for w in cur_question:
        for x in w:
            s+=x
    cur_question = s
    print('New cur_target:',cur_target)
    
    # Build answer_list
    answer_list = []
    for e in cur_target:
        for w in e:
            answer_list.append(w)
    print('answer_list:',answer_list)
    
    print('\n')


def question():
    global android
    global cur_question
    global answer
    
    print(cur_question+':')
    
    # Return the correct input according to the device
    if android:
        answer = raw_input()
    else:
        answer = input()


def check():
    global answer_ok
    global answer
    global answer_list
    global chosen_word
    global loop
    global mode_toforeign
    global mode_en
    
    # Print the correct answers
    if answer=='r':
        # Minus 1 if possible
        if words_score[chosen_word] >= 1:
            words_score[chosen_word] -= 2
        return True
    
    # Change direction of question
    elif answer=='d':
        mode_toforeign = not mode_toforeign
        return True
        
    # Change the target language
    elif answer=='m':
        mode_en = not mode_en
        init()
        return True
    
    # Exit
    elif answer=='q':
        loop = False
        return True
    
    else:
        answer_ok = is_in_list(answer, answer_list)
        return False
    

def is_in_list(x,l):
    # Search the list
    n = len(l)
    i = 0
    while i<n:
        if l[i] == x:
            i = n
        i += 1
    
    return (i==n+1)


def print_answers():
    global cur_target
    global answer_ok
    
    str = ''
    print('answer_ok:',answer_ok)
    for s in cur_target:
        # If correct answer, do not print the provided answer
        if answer_ok :
            for w in s:
                if w!= answer:
                    str+=w+'/'
            str+=','
        # Else, print everything
        else:
            for w in s:
                str+=w
    
    print(str)

init()
while loop:
    new_word()
    while check():
        question()

    print_answers()
    
    answer_ok = False
    
    # Handles scores
    if words_score[chosen_word] < 9:
        words_score[chosen_word] += 1 
exit()