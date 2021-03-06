from sklearn import svm
from sklearn.model_selection import GridSearchCV
import os

nowords = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount",  "an", "and", "another", "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are", "around", "as", "at", "back", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom", "but", "by", "call", "can", "cannot", "can't", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "do not", "don't", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven", "else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "i", "i'm", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

tweets = []
for line in open('training_tweets.txt').readlines():
    items = line.split(',')
    tweets.append([int(items[0]), items[1].lower().strip()])

#print(tweets)

words = dict()

for class_label, text in tweets:
    for term in text.split():
        term = term.lower()
        #print(term)
        if len(term) > 2 and term not in nowords:
            if term in words:
                words[term] = words[term] + 1
                #print("IF", vocab[term])
            else:
                words[term] = 1
                #print("ELSE", vocab[term])

#print(len(words))

words = {term: freq for term, freq in words.items() if freq > 17}
#print(len(words))
print(words)

words_idx = {term: idx for idx, (term, freq) in enumerate(words.items())}
print(words_idx)
'''
X = []
y = []
for class_label, text in tweets:
    x = [0] * len(words)
    terms = [term for term in text.split() if len(term) > 2]
    #print(terms)
    for term in terms:
        if term in words_idx:
            x[words_idx[term]] += 1
    y.append(class_label)
    X.append(x)

svc = svm.SVC(kernel='linear')
Cs = range(1, 20)
clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), cv = 10)
clf.fit(X, y)

#prediction = clf.predict(X)
#print(prediction)

tweets = []
for line in open('testing_tweets.txt').readlines():
    tweets.append(line)

X = []

for text in tweets:
    x = [0] * len(words)
    terms = [term for term in text.split() if len(term) > 2]
    for term in terms:
        if term in words_idx:
            x[words_idx[term]] += 1
    X.append(x)


y = clf.predict(X)
print(y)

path = '/Users/jinal/PycharmProjects/HW 6/'

if not os.path.exists(path):
    os.makedirs(path)

file_name = 'Predicted Tweets.txt'
with open(os.path.join(path, file_name), 'w') as f:
    f.write('Sentiment: 1 means positive class; 0 means negative class')
    f.write('\n')

with open(os.path.join(path, file_name), 'a') as f:
    for i in range(len(tweets)):
        f.write('Sentiment: ')
        f.write(str(y[i]))
        f.write('\n')
        f.write('Text:')
        f.write(tweets[i])
        f.write('\n')
'''

