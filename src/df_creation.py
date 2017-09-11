import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
snowball = SnowballStemmer('english')
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from collections import Counter
import string
from nltk.tag import pos_tag
from nltk.corpus import stopwords

if __name__ == '__main__':
    tokenized = [word_tokenize(content.lower()) for content in documents]
    snowball = SnowballStemmer('english')

    ## Import files using clean function,  add labels to signify psuedoscience
    ## combine two dataframes into one

    false = clean_csv('data/false_corpus.csv')
    false['label'] = 0
    true = clean_csv('data/corpus.csv')
    true['label'] = 1
    content = [false, true]
    all_content = pd.concat(content)

    ## update stopwords for TF-IDF Vectorizing
    stop = set(stopwords.words('english'))
    html_stopwords = ["span", 'vm', 'hook', 'class', 'strong', 'href', 'style', 'rgb',
                      'transpar', '153', 'br', 'strong', 'span', 'com', 'vm', 'img', 'http', 'zzzzzzzzzzzz']
    stop.update(html_stopwords)

    ## Pandas functions to add columns from above functions
    all_content['credentials'] = all_content['content'].apply(find_credentials)
    all_content['unique_words'] = all_content['content'].apply(unique_word_pct)
    all_content['content_length'] = all_content['content'].apply(len)
    all_content['sources'] = all_content['content'].apply(find_sources)
    all_content['avg_word_length'] = all_content['content'].apply(word_length)
    all_content['uppercase_title'] = all_content['title'].apply(title_capitals)
    all_content['exclamations_title'] = all_content['title'].apply(find_exclamations)
    all_content['exclamations_content'] = all_content['content'].apply(find_exclamations)
    all_content['stemmed_content'] = all_content['content'].apply(stem)



    ## Adding the Parts of Speech percentages to all_content dataframe
    POS_list = ['PRP$', 'VBG', 'VBD', 'VBN', 'VBP', 'WDT', 'JJ', 'WP', 'VBZ', 'DT',
                '#', 'RP', '$', 'NN', ')', '(', ',', '.', 'TO', 'PRP', 'RB', ':',
                'NNS', 'NNP', 'VB', 'WRB', 'CC', 'PDT', 'RBS', 'RBR', 'CD', 'EX',
                'IN', 'WP$', 'MD', 'NNPS', 'JJS', 'JJR', 'UH', 'FW', 'LS', 'POS']
    PoS_tag_list = []
    for row in all_content['content']:
        PoS_tag_list.append(pos_tag_finder(row))
    PoS_df = pd.DataFrame(PoS_tag_list)
    PoS_df = PoS_df.reset_index()

    all_content = all_content.reset_index()
    pos_content = all_content.join(PoS_df, lsuffix='_all_content', rsuffix='_PoS_df')
    pos_content = pos_content.drop(['index_all_content', 'level_0', 'index_PoS_df'], axis=1)
    pos_content = pos_content.fillna(0)
    labels = pos_content.pop('label')


    ## TF-IDF Vectorization and Naive Bayes Model fitting
    vector = TfidfVectorizer(stop_words=stop)
    train_matrix = vector.fit_transform(X_train['stemmed_content'])
    bayes_model = MultinomialNB()
    bayes_model.fit(train_matrix, y_train)
    test_matrix = vector.transform(X_test['stemmed_content'])

    #predicting log probabilities of pseudoscience and adding them back to X_train and X_test
    X_train_predictproba = bayes_model.predict_proba(train_matrix)
    X_test_predictlogprobab = bayes_model.predict_log_proba(test_matrix)
    X_train['predict_proba'] = X_train_predictproba[:,1]
    X_test['predict_proba'] = X_test_predictlogprobab[:,1]
