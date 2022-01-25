##########################################################################################
#Algoritmo 01- Pseudo code for ”extract terms through NLP”
##########################################################################################
'''
Tokenize dataset title and description text and get a set of tokenized sentences
for each tokenized sentence do
    Use POS-tagger to identify lexical categories
    Apply a chunker to extract noun phrases
    if the words in a phrase are not stopwords then
        Normalize the phrase by lemmatization
        Add the lemmas to the set of terms Td
    end if
end for
'''
##########################################################################################

import regex as re
import nltk
#nltk.download('omw-1.4')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from nltk.tag import DefaultTagger
#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

def english_stops():
    english_stops = list(set(stopwords.words('english')))
    print(english_stops)
    return(english_stops)

def punctuations():
    punctuations = list(string.punctuation)
    print(punctuations)
    return(punctuations)


def tokenize_descriptions(index, atributo,row,english_stops,punctuations):

    ##print(80 * '*')

    #print('Atributo: '+atributo)
    atribute = atributo.lower()

    tokens_atribute = word_tokenize(atribute)
    #print('tokens_atribute = '+ str(tokens_atribute))

    tokens_atribute_without_stopwords = \
        [word for word in tokens_atribute if word not in english_stops]
    #print('tokens_atribute_without_stopwords: ', end='')
    #print(tokens_atribute_without_stopwords)

    tokens_atribute_without_stopwords_and_punctuation = \
        [i for i in tokens_atribute_without_stopwords if i not in punctuations]
    ##print('tokens_atribute_without_stopwords_and_punctuation: ', end='')
    ##print(tokens_atribute_without_stopwords_and_punctuation)

    ##print('--------------------------')

    #print('Descrição: '+row)
    description = row.lower()
    tokens_description = word_tokenize(description)
    #print('tokens_description = '+ str(tokens_description))

    tokens_description_without_stopwords = \
        [word for word in tokens_description if word not in english_stops]
    #print('tokens_description_without_stopwords: ', end='')
    #print(tokens_description_without_stopwords)

    tokens_description_without_stopwords_and_punctuation = \
        [i for i in tokens_description_without_stopwords if i not in punctuations]
    ##print('tokens_description_without_stopwords_and_punctuation: ', end='')
    ##print(tokens_description_without_stopwords_and_punctuation)

    ##print('--------------------------')

    result = tokens_atribute_without_stopwords_and_punctuation + tokens_description_without_stopwords_and_punctuation

    result = list(dict.fromkeys(result))
    ##print('result: ', end='')
    ##print(result)

    tokens_description_without_stopwords_and_punctuation_and_numbers = []

    for i in result:
        try:
            float(i)
        except:
            if not i.isnumeric():
                tokens_description_without_stopwords_and_punctuation_and_numbers.append(i)
    ##print('tokens_description_without_stopwords_and_punctuation_and_numbers: ', end='')
    ##print(tokens_description_without_stopwords_and_punctuation_and_numbers)

    ##print('--------------------------')

    pos_tagging = nltk.pos_tag(tokens_description_without_stopwords_and_punctuation_and_numbers)
    #print('pos_tagging = ' + str(pos_tagging))

    # NN noun, singular ‘desk’
    # NNS noun plural ‘desks’
    # NNP proper noun, singular ‘Harrison’
    # NNPS proper noun, plural ‘Americans’

    pos_tagging_filter = [(word, tag) for word, tag in pos_tagging
                          if tag.startswith('NN') or tag.startswith('NNS') \
                          or tag.startswith('NNP') or tag.startswith('NNPS')]

    ##print('pos_tagging_filter = ' + str(pos_tagging_filter))

    lemmatizer = WordNetLemmatizer()

    td = []
    for word, tag in pos_tagging_filter:
        lemma = lemmatizer.lemmatize(word)
        td.append(lemma)

    ##print('td = ' + str(td))

    ##lines = [index, atribute, description]
    lines = [index, atribute]
    #print('Line = ' + str(lines))

    if atributo not in td:
        td.append(atributo)

    return(td)



