import string
import csv
import regex as re

def removePunctuations(tweet):

     out = tweet.translate(None, r"!\"#$%&'()*+,./:;<=>?-[\]^_`{|}~")
    #  test = filter(lambda ch: ch not in "!#""$%&'()*+,./:;<=>?-[\]^_`{|}~", tweet)
    #  out = ""
    #  punct = "!\"#$%&'()*+,./:;<=>?-[\]^_`{|}~"
    #  for char in tweet:
    #      if char not in punct:
    #          out = out + char
    #  return re.sub(ur"[^\P{P}@]+", "", tweet)
     return out

if __name__ == "__main__":

    tweets = []

    with open("../Dataset/final-data.csv",'r') as r, open("../Dataset/tweets-removed-punctuations-test.csv", 'a') as w:
        reader = csv.DictReader(r)

        fieldnames = ['tweet','label']
        writer = csv.DictWriter(w, fieldnames=fieldnames)

        for row in reader:
            tweets.append(row)


        writer.writeheader()

        for line in r.readlines():
            tweet=line[:-2]
            label= line[-2:]

        for t in tweets:
            ar = t['tweet'].lower()
            writer.writerow({'tweet': removePunctuations(ar), 'label':t['label']})
