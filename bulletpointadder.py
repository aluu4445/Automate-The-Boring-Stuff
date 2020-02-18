#! python3

#bulletpointadder.py adds bullet points of each line of text on the clipboard

import pyperclip

text = pyperclip.paste()

#separate lines and add stars

lines = text.split('\n')
for i in range(len(lines)): #loop through all indexes in the lines list
    lines[i] = '* ' + lines[i] #add star to each string

text = '\n'.join(lines)

pyperclip.copy(text)
