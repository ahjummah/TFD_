import string
import re

def removePunctuation(tweet):
    s = re.sub(r'[^\w\s]','',tweet)
    return tweet

def removePunctuation2(tweet):
    out = tweet.translate(None, r"!\"#$%&'()*+,./:;<=>?-[\]^_`{|}~")
    # if out.startswith(" "):
        # out = out[1:]
    return out

with open("../Dataset/final-data.csv",'r') as f:
    for line in f.readlines():
            tweet=line[:-2]
            label= line[-2:]
            with open("../Dataset/tweets-removed-punctuations-test.csv", 'a') as r:
                r.write(removePunctuation2(tweet)+","+label)
