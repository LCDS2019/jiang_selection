from nltk.tokenize import word_tokenize
from nltk.util import ngrams


def get_ngrams_01(text):

    word_list = text.split()
    #number_of_words = len(word_list)
    number_of_words = 8
    #print('Number_of_words: '+str(number_of_words))
    #print(''.center(40, '-'))

    list_ngrams = []
    for i in range(1,number_of_words+2):
        #print(i)
        result_gram=get_ngrams_02(text, i)
        for j in result_gram:
            list_ngrams.append(j.lower())
    #print(list_ngrams)
    #print(''.center(40, '-'))
    #print('')

    return list_ngrams

def get_ngrams_02(text, n ):
    n_grams = ngrams(word_tokenize(text), n)
    list_ngram2=[]
    for i in n_grams:
        list_ngram2.append([ ' '.join(i)][0])
    #print(list_ngram2)
    #print(''.center(40, '-'))
    return list_ngram2