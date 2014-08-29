# JIGAR THAKKAR
# 201201072

import pickle
import os
import re
from nltk import *
from nltk.corpus import wordnet as wn
from getdetails import *
from listplayers import *
from getquestion import *


def get_match1(query, dic):
    for j in query:
        i = j.lower()
        if i == 'first' or i == '1' or i == 'one':
            return 1
        if i == 'second' or i == '2' or i == 'two':
            return 2
        if i == 'third' or i == '3' or i == 'three':
            return 3
        if i == 'forth' or i == '4' or i == 'four':
            return 4
        if i == 'fifth' or i == '5' or i == 'five':
            return 5
    return 0


def getmatch(words):
    matchnum = {"first": 1, "fourth": 4, "second":
                2, "third": 3, "fifth": 5}
#    for i in range(len(words)):
#        if words[i] in matchnum:
#            print words[i]
#            return matchnum[words[i]]
    for y in words:
        if y in matchnum:
            print y
            return matchnum[y]
    return 0


def getplayers(words, players):
    old = 0
    name = ""

    for j in players:
        ct = 0
        x = j.split(" ")
        answer = ""

        for k in x:
            for y in words:
                if y.lower() == k.lower():
                    ct += 1
                    answer += k + " "
                    if ct > old:
                        old = ct
                        name = answer
#                        print "D"
                        print name
    return name


def hitfunc(k, words, score, answer, inn1, inn2):
    for k in words:
        k = k.lower()

    for l in words:
        for j in score:
            if j == l:
                answer = []
                for i in inn1:
                    if (str(score[j]) + ' run') in inn1[i]['what'].lower():
                        answer.append(inn1[i]['to'])

                for i in inn2:
                    if (str(score[j]) + ' run') in inn2[i]['what'].lower():
                        answer.append(inn2[i]['to'])
                return answer


def dismissfunc(inn1, inn2, who):
    for i in inn1:
        if inn1[i]['what'] == 'OUT' and inn1[i]['to'] in who:
            return inn1[i]["from"]

    for i in inn2:
        if inn2[i]['what'] == 'OUT' and inn2[i]['to'] in who:
            return inn2[i]["from"]


def emptied(inn, i):
    inn[i]['what'] = ""
    inn[i]['to'] = ""
    inn[i]['from'] = ""
    inn[i]['why'] = ""


def aimain(no, who, what, words, callcheck):
    os.chdir("../dataset/match"+str(no))
    print callcheck
    inn1 = pickle.load(open(str(no)+"1comm.p", "rb"))
    inn2 = pickle.load(open(str(no)+"2comm.p", "rb"))
    over = -1
    who = who.split(" ")[callcheck]
    if "over" in words:
        for i in range(len(words)):
            if words[i] == "over":
               # print len(words[i+1])
                try:
                    over = int(words[i-1])
                 #   print "yes"
                except:
                    pass
                try:
                    over = int(words[i+1])
                #    print "yes-1"
                except:
                    pass
        over = str(over)
        if over != "-1":
            for i in inn1:
                if re.match(over+'\.*', i):
                    pass
                else:
                    emptied(inn1, i)
                    #inn1[i]['what'] = ""
                    #inn1[i]['to'] = ""
                    #inn1[i]['from'] = ""
                    #inn1[i]['why'] = ""
            for i in inn2:
                if re.match(over+'\.*', i):
                    pass
                else:
                    emptied(inn2, i)
                    #inn2[i]['what'] = ""
                    #inn2[i]['to'] = ""
                    #inn2[i]['from'] = ""
                    #inn2[i]['why'] = ""

    score = {"ones": 1, "twos": 2, "fours": 4, "sixes": 6, "threes": 3, "four":
             4, "six": 6, "wide": -1, "no ball": -2, "wides": -1, "no balls": -2}

    if what == 4:
        ans1 = dismissfunc(inn1, inn2, who)
        return ans1

    elif what == 1 or what == 3:
        mx = {}

        for k in words:
            k = k.lower()

        for l in words:
            for j in score:
                if j == l:
                    answer = []
                    for i in inn1:
                        if (str(score[j]) + ' run') in inn1[i]['what'].lower() and inn1[i]['to'] in who:
                            if "max" in words or "maximum" in words:
                                try:
                                    mx[i] += 1
                                except:
                                    mx[i] = 1
                            answer.append(inn1[i])
                            answer.append(i)

                        elif "wide" in inn1[i]['what'].lower() and inn1[i]['from'] in who and ("wide" in words or "wides" in words):
                            if "max" in words or "maximum" in words:
                                try:
                                    mx[i] += 1
                                except:
                                    mx[i] = 1

                        elif "no-ball" in inn1[i]['what'].lower() and inn1[i]['from'] in who and ("no ball" in words or "no balls" in words):
                            if "max" in words or "maximum" in words:
                                try:
                                    mx[i] += 1
                                except:
                                    mx[i] = 1
                            answer.append(inn1[i])
                            answer.append(i)

                    for i in inn2:
                        if (str(score[j]) + ' run') in inn2[i]['what'].lower() and inn2[i]['to'] in who:
                            if "max" in words or "maximum" in words:
                                try:
                                    mx[i] += 1
                                except:
                                    mx[i] = 1
                            answer.append(inn2[i])
                            answer.append(i)

                        elif "wide" in inn2[i]['what'] and who in inn2[i]['from'] and ("wide" in words or "wides" in words):
                            print "here"
                            if "max" in words or "maximum" in words:
                                try:
                                    mx[i] += 1
                                except:
                                    mx[i] = 1
                            answer.append(inn2[i])
                            answer.append(i)

                        elif "no-ball" in inn2[i]['what'].lower() and inn2[i]['from'] in who and ("no ball" in words or "no balls" in words):
                            if "max" in words or "maximum" in words:
                                try:
                                    mx[i] += 1
                                except:
                                    mx[i] = 1
                            answer.append(inn2[i])
                            answer.append(i)
                    if mx:
                        return max(mx, key=mx.get)

                    return answer
        if 'wicket' in words or 'out' in words:
            for i in inn1:
                if inn1[i]['what'] == 'OUT' and inn1[i]['to'] in who:
                    return i
            for i in inn2:
                if inn2[i]['what'] == 'OUT' and inn2[i]['to'] in who:
                    return i

    elif what == 2:
        for k in words:
            k = k.lower()
        for l in words:
            for j in score:
                if j == l:
                    answer = []
                    for i in inn1:
                        if (str(score[j]) + ' run') in inn1[i]['what'].lower() and inn1[i]['to'] in who:
                            answer.append(inn1[i]['from'])
                        elif "wide" in inn1[i]['what'].lower() and inn1[i]['from'] in who and ("wide" in words or "wides" in words):
                            answer.append(inn1[i]['from'])
                        elif "no-ball" in inn1[i]['what'].lower() and inn1[i]['from'] in who and ("no ball" in words or "no balls" in words):
                            answer.append(inn1[i]['from'])
                    for i in inn2:
                        if (str(score[j]) + ' run') in inn2[i]['what'].lower() and inn2[i]['to'] in who:
                            answer.append(inn2[i]['from'])
                        elif "wide" in inn2[i]['what'].lower() and inn2[i]['from'] in who and ("wide" in words or "wides" in words):
                            answer.append(inn2[i]['from'])
                        elif "no-ball" in inn2[i]['what'].lower() and inn2[i]['from'] in who and ("no ball" in words or "no balls" in words):
                            answer.append(inn2[i]['from'])
                    return answer
        if 'wicket' in words or 'out' in words:
            for i in inn1:
                if inn1[i]['what'] == 'OUT' and inn1[i]['to'] in who:
                    return i
            for i in inn2:
                if inn2[i]['what'] == 'OUT' and inn2[i]['to'] in who:
                    return i
    elif what == 5:
        ans = hitfunc(k, words, score, answer, inn1, inn2)
        return ans
    os.chdir("..")


def printer(string):
    print "->  ",
    print string


def main():
    test = 0
    match2 = 1
    iplayer = "../dataset/player_profile/indian_players_profile.txt"
    nzplayer = "../dataset/player_profile/nz_players_profile.txt"
    question = raw_input(
        "Ask a question in the given format:\n<info><description><question>\n")
    parse = question.replace(",", "")
    parse = parse.split('?')[test]
    parse = parse.split(' ')
    nzplayers = listplayers(nzplayer)
    indiaplayers = listplayers(iplayer)
    # print indiap layers

    players = indiaplayers+nzplayers
    match = getmatch(parse)
    dic = {"first": '1'}
    match2 = get_match1(parse, dic)
    # print match2
    player = getplayers(parse, players)
    quest = getquestion(parse)
    # print match
    # print player
    # print quest
    callcheck = 0
    answer = aimain(match, player, quest, parse, callcheck)
    test = test + 1
    winner = pickle.load(open("win.p", "rb"))
    # print test
    ct = 0
    if (len(answer) > 1 and type(answer) == list and quest == 1 or quest == 3):
            print "In the over and on the ball ",
            for i in range(len(answer)):
                    if (i % 2 != 0):
                        ct = 1
                        print answer[i],
                        print " and "
    if (ct == 1):
        print "ohh sorry thats it! "
    print "Here is the entire info about the ball:\n"
    printer(answer)
    print "\nHere is the game results:"
    printer(winner['0'])

if __name__ == "__main__":
    main()
