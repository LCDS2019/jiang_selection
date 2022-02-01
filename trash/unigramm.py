
'''
from nltk import ngrams

sentence = 'this is a foo bar sentences and i want to ngramize it'

n = 1
sixgrams = ngrams(sentence.split(), n)

print(sentence)

for grams in sixgrams:
  print (grams)

  '''

from nltk.tokenize import word_tokenize
from nltk.util import ngrams

def get_ngrams(text, n ):
    n_grams = ngrams(word_tokenize(text), n)
    for i in n_grams:
        print( [ ' '.join(i)])

sentence = 'this is a foo bar sentences and i want to ngramize it'
print(sentence)

#n = 5
for n in range(15):
    print(n)
    get_ngrams(sentence, n )