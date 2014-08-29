import os
import sys
import re

def getdetails():
    details = []
    f = open('details.txt', 'r')
    i = 0
    for line in f:
        temp = line[:-1]
        temp = temp.split(' ')
        if (i == 0):
            if ('Match' in temp[0]):
                details.append(['Tie'])
            elif ('New' in temp[0]):
                details.append([temp[0]+' '+temp[1]])
            else:
                details.append([temp[0]])
        elif i == 1:
            details.append([temp[0] + temp[1]])
            if ('New' in temp[2]):
                details.append(['New Zealand'])
            elif('India' in temp[2]):
                details.append(['India'])
        i += 1
    return details

