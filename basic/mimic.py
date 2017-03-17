#!/usr/bin/python -tt
# -*- coding: UTF-8 -*-
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    # +++your code here+++
    f = open(filename,'r')
    list = f.read().split()
    length = len(list)

    dict = {}
    dict[''] = [list[0]]
    for x,pal1 in enumerate(list):
        oList = []
        for y,pal2 in enumerate(list):
            if pal1 == pal2 and x<=y and y<len(list)-1:
                oList.append(list[y+1])
        # Se entrada já existe no dic, então ele é atualizada.
        if pal1 in dict:
            oList = oList + dict[pal1]
        else:
            if oList:
                dict[pal1] = oList
    print(list)
    print((dict))

    return dict


def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""
    # +++your code here+++
    if word in mimic_dict:
        # print(word + ' '),
        for x in range(200):
            if word in mimic_dict:
                chosen_word = random.choice(mimic_dict[word])
            else:
                chosen_word = ''
            if x % 30 == 0:
                print(chosen_word +  ' ')
            else:
                print(chosen_word + ' '),
            word = chosen_word

    return


# Provided main(), calls mimic_dict() and mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)

    dict = mimic_dict(sys.argv[1])
    print_mimic(dict, '')


if __name__ == '__main__':
  main()
