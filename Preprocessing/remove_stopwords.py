from cStringIO import StringIO
stop = []

def retrieve_stopwords():
    with open('stopwords_list.txt','r') as f:
        for line in f.readlines():
            stop.append(str(line).strip())

def remove_words(tweet):
    new_tweet = ""
    for i in tweet.lower().split():
         if i not in stop:
             new_tweet += i + " "
    return new_tweet

if __name__ == "__main__":
    retrieve_stopwords()
    with open('tweets-removed-punctuations-test.csv','r') as r, open('../Training_ Dataset/2500_training_data.csv','a') as w:
        reader = csv.DictReader(r)

        fieldnames = ['tweet','label']
        writer = csv.DictWriter(w, fieldnames=fieldnames)

        for row in reader:
            tweets.append(row)


        writer.writeheader()

        for t in tweets:
            ar = t['tweet'].lower()
            writer.writerow({'tweet': remove_words(ar), 'label':t['label']})
