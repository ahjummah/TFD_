from nltk.corpus import stopwords
from cStringIO import StringIO
stop = []

# string = "i kick the seat up hip shake the pants down and aim hands free and you dumb motherfuckers still want me to wash my hands get wrecked"
# for i in string.lower().split():
#      if i not in stop:
#          print i

def retrieve_stopwords():
    with open('../Dataset/stopwords_list.txt','r') as f:
        for line in f.readlines():
            stop.append(str(line).strip())
    print stop

def remove_words():
    print "ok"
    with open('../Dataset/tweets-removed-punctuations-test.csv','r') as f:
        for line in f.readlines():
            new_tweet = " "
            tweet=line[:-3]
            # print tweet

            label = line[-2:]
            for i in tweet.lower().split():
                 if i not in stop:
                     print i
                     new_tweet += i + " "
            print new_tweet
            write_to_file(new_tweet,label)

def write_to_file(new_tweet, label):
    with open('../Dataset/2500_training_data.csv','a') as w:
        w.write(new_tweet+","+label)



retrieve_stopwords()
remove_words()
# write_to_file()
# print removed_stopwords
