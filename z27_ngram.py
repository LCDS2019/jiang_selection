from nltk.tokenize import word_tokenize
from nltk.util import ngrams


def get_ngrams_01(text):

    word_list = text.split()
    number_of_words = len(word_list)
    print('Number_of_words: '+str(number_of_words))
    print(''.center(40, '-'))


    list_ngrams = []
    for i in range(number_of_words):
        print(i)
        result_gram=get_ngrams_02(text, i)
        list_ngrams.append('')
    print('')


def get_ngrams_02(text, n ):
    n_grams = ngrams(word_tokenize(text), n)
    list_ngram2=[]
    for i in n_grams:
        list_ngram2.append([ ' '.join(i)][0])
    print(list_ngram2)

    print(''.center(40, '-'))