import pickle
import os
import re

def getquestion(words):
    test = 0
    if "which" in words:
        if "which over" in " ".join(words) or "which overs" in " ".join(words) or "which over(s)" in " ".join(words):
            return 1

        elif "bowler" or "bowlers" or " bowler(s)" in " ".join(words):
            test = test + 1
            return 2

        elif "which ball" in " ".join(words):
            return 3

    elif "who" in words:

        if "dismissed" in words:
            return 4

        elif "hit" in words:
            return 5
