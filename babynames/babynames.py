#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main() to call it.

For writing regex, it's nice to include a copy of the target text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # +++your code here+++
    f = open(filename,'r')

    page = f.read()

    f.close()

    ano = re.findall('Popularity in ([0-9]{4})', page)
    rank_e_nomes = re.findall('<tr align="right"><td>([0-9]{1,4})</td><td>([a-zA-Z]{1,20})</td><td>([a-zA-Z]{1,20})</td>', page)

    lista_nome_rank = []

    for rank, nome1, nome2 in rank_e_nomes:
        lista_nome_rank.append(nome1 + ' ' + rank)
        lista_nome_rank.append(nome2 + ' ' + rank)

    lista_nome_rank.sort()
    lista_nome_rank.insert(0,ano[0])

    return lista_nome_rank


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

        # +++your code here+++
        # For each filename, get the names, then either print the text output
        # or write it to a summary file
    if summary:
        for filename in args:
            sum_file = open('summary-' + filename + '.txt','w')
            sum_file.write(str(extract_names(filename)))
            sum_file.close()
    else:
        for filename in args:
            print('-' * 70 + filename + '-' * 70)
            print(extract_names(filename))
            print('\n\n\n')

if __name__ == '__main__':
    main()
