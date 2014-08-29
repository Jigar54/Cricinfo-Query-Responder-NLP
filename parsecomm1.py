import re
import os
import pickle
from nltk import *
from nltk.corpus import wordnet as wn
import BeautifulSoup


def listplayers(play, fname):
    f = open(fname, 'r')
    for line in f:
        temp = line[:-1]
        temp = temp.split(',')
        a = temp[0]
        a = a.split('\t')
        print a[0]
        if a[0] not in play:
            play.append(a[0])


def postagging(q):
    text = word_tokenize(q)
    tags = pos_tag(text)
    words = {}
    for tag in tags:
        search1 = "N.*"
        search2 = "V.*"
        if re.findall(search1, tag[1]) or re.findall(search2, tag[1]):
            try:
                words[tag] += 1
            except:
                words[tag] = 1
    return words


def parsecomm1(dic):
    ballwise = {}
    for j in dic:
        dic[j]['why'] = dic[j]['why'][2:]
        y = dic[j]['to']  + dic[j]['from'] + " " + \
            dic[j]['why'] + " " + dic[j]['what']
        z = postagging(y)
        table2 = []
        l = 0
        for i in z:
            s = "NNP"
            search1 = "N.*"
            search2 = "V.*"
            if re.findall(s, i[1]):
                l = 13
                # for k in range(l):
                table2.append(i[0])
                #x = wn.synsets(i[0], pos=wn.NOUN)
            if re.findall(search1, i[1]):
                l = 7
                # for k in range(l):
                table2.append(i[0])
                #x = wn.synsets(i[0], pos=wn.NOUN)
            elif re.findall(search2, i[1]):
                l = 3
# for k in range(l):#
                table2.append(i[0])
                #x = wn.synsets(i[0], pos=wn.VERB)
            else:
#		for k in range(l):
                table2.append(i[0])
                #x = wn.synsets(i[0])
#            for m in range(l):
#                table2.append(i[0])
#            for z in x:
#                for y in z.lemma_names:
#                    table2.append(y)
        table3 = {}
        for i in table2:
            try:
                table3[i] += 1
            except:
                table3[i] = 1
        ballwise[j] = table3
    return ballwise
