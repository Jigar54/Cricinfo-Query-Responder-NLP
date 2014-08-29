import re
import os
import pickle
from nltk import *
from nltk.corpus import wordnet as wns
from parsecomm1 import *


def getmatch(query):
    for j in query:
        i = j.lower()
        if i == 'first' or i == 'one' or i == 'match number one' or i == '1':
            return 1
        if i == 'second' or i == 'two' or i == 'match number two' or i == '2':
            return 2
        if i == 'third' or i == 'three' or i == "match number three"or i == '3':
            return 3
        if i == 'forth' or i == 'four' or i == "match number four" or i == '4':
            return 4
        if i == 'fifth' or i == 'five'or i == "match number five" or i == '5':
            return 5
    return 0


def add_to_dict(dictionary, fname):
    f = open(fname, 'r')
    for line in f:
        temp = line[:-1]
        temp = temp.split(',')
        a = temp[0]
        b = temp[1:]
        if a not in dictionary:
            dictionary[a] = b


def gettag(q):
    text = word_tokenize(q)
    tags = pos_tag(text)
    searchfor = "W.*"
    for tag in tags:
        if re.findall(searchfor, tag[1]):
            return tag[0]
    return 0


def generatesynsets(table):
    table2 = []
    table3 = {}
    for i in table:
        search1 = "N.*"
        search2 = "V.*"
        if re.findall(search1, i[1]):
            x = wns.synsets(i[0], pos=wns.NOUN)
        elif re.findall(search2, i[1]):
            x = wns.synsets(i[0], pos=wns.VERB)
        for z in range(len(x)):
            for y in x[z].lemma_names:
                syn = 'SYN'
                if y not in ['match', 'be', 'in', 'is']:
                    table2.append((y, syn))
    test = 0
    test += 1
    for i in table2:
        try:
            table3[i] += test

        except:
            table3[i] = test

    return table3


def heu(diction1, diction2, query, dic, dic2, table):
    h = {}
    # print query
    if "best" in query:
        print "here"
        for k in diction1:
            if "best" or "classy" or "wonderful" or "brilliant" or "great shot" in dic[j]['why']:
                h[k] = 2
#                        for k in query:
#                                if (re.findall("N.*", table[k])):
#                                        print "!here"
#                                        print k
#                                        if "best" or "classy" or "wonderful" or "brilliant" or "great shot" in dic[j]['why']:
#                                                h[j] = 2
        for k in diction2:
            if "best" or "classy" or "wonderful" or "brilliant" or "great shot" in dic[j]['why']:
                h[k] = 2
#                        for k in query:
#                                if (re.findall("N.*", table[k])):
#                                        print "!here"
#                                        print k
#                                        if "best" or "classy" or "wonderful" or "brilliant" or "great shot" in dic[j]['why']:
#                                                h[j] = 2
    return h


def findmatch(query, diction1, diction2, dic, dic2, table, table2):
    bst = -1
    h = {}
    print query
    h = heu(diction1, diction2, query, dic, dic2, table)
    diction = diction1
    for j in diction:
        cnt = 0.0
        for i in table2:
            if i[0] in diction[j].keys():
                try:
                    cnt += diction[j][i[0]] + h[j]
                except:
                    cnt += diction[j][i[0]]
        if cnt > bst:
            bst = cnt
            answer = j
            inn = 1

    diction = diction2
    for j in diction:
        cnt = 0.0
        for i in table2:
            if i[0] in diction[j].keys():
                try:
                    cnt += diction[j][i[0]] + h[j]
                except:
                    cnt += diction[j][i[0]]
        if cnt > bst:
            bst = cnt
            answer = j
            inn = 2
    return (answer, inn)


def printingproperly(no, ball, match, questn):
    print "Match no:",
    print match
    if questn == "when" or questn == "When":
        print "BALL: ",
        print no,
        print "was when this incident occured"
        print "For additional information\n\n\n read below :P"
        print ball['why']

    elif questn == "who" or questn == "Whom" or questn == "Who" or questn == "whom":
        print no,
        print " ",
        print ball['from'] + " to ",
        print ball['to']

    elif questn == "what" or questn == "What":
        print "On "
        print no,
        print " ,",
        print ball['why']

    elif questn == 'why' or questn == "Why":
        print "At the time when "
        print no,
        print " was bowled this event happend because,",
        print ball['why']

    elif questn == "How " or questn == "how":
        print "In the over and the on the ball"
        print no,
        print " ,",
        print ball['what']
    else:
        print "In " + no + " ,",
        print ball['why']

# driver function
q = raw_input("Please Give your query:\n")
# print "splitting query.."
query = q.split('?')[0]
query = query.split(' ')
# print "detecting match number.."
match = getmatch(query)
# print "match",
# print match,
# print "detected.."
if match == 0:
    print "Please give match no."
    exit(0)
os.chdir("../dataset/match"+str(match))
dic = pickle.load(open(str(match)+"1comm.p", "rb"))
dic2 = pickle.load(open(str(match)+"2comm.p", "rb"))
os.chdir("../../codes")
print "Processing ... "
# print "QUERY",
# print query
question = gettag(q)
print question,
print "Processing ... "
table = postagging(q)
print
print "Now the part ahead is of the 4th part"
print "Generating synsets.."
print
table2 = generatesynsets(table)
f1 = '../dataset/match1/11bat.txt'
bats1 = {}
add_to_dict(bats1, f1)
# print table2
print "Synsets generated.."
print "Addition to part 3 in part 4 completed!!!"
diction1 = parsecomm1(dic)
diction2 = parsecomm1(dic2)
print "Still processing ....\n"
print
result = findmatch(query, diction1, diction2, dic, dic2, table, table)
print "The CLOSEST answer is the following:\n"
print
if result[1] == 0:
    printingproperly(result[0], dic2[result[0]], match, question)
else:
    printingproperly(result[0], dic[result[0]], match, question)
print
