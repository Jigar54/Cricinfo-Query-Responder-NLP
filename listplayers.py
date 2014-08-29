import os
import sys
import re
def listplayers(fname):
    play = []
    f = open(fname, 'r')
    for line in f:
        temp = line[:-1]
        temp = temp.split(',')
        a = temp[0]
        a = a.split('\t')
        if a[0] not in play:
            play.append(a[0])
    return play

