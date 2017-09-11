import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from collections import Counter
import string
from nltk.tag import pos_tag
from nltk.corpus import stopwords
snowball = SnowballStemmer('english')



## Clean in csv files of all data
def clean_csv(filename):
    new_df = pd.read_csv(filename)
    clean_df = new_df.rename(index=str, columns={"0": "title", "1": "link", '2': 'article'})
    clean_df = clean_df.drop_duplicates(subset='article')
    clean_df = clean_df.dropna(how='any')
    clean_df = clean_df.drop('Unnamed: 0', axis=1)
    return clean_df




## Functions to use in featurizing text and title columns
def title_capitals(title):
    title = str(title).strip()
    return sum([1 for letter in title if letter.isupper()])/float(len(title))

def find_exclamations(title):
    title = str(title).strip()
    return sum([1 for letter in title if letter == '!'])/float(len(title))

def unique_word_pct(string):
    unique_words = set()
    for word in string.split():
        unique_words.add(word)
    return float(len(unique_words))/float(len(string.split()))

def word_counter(content):
    words = Counter()
    for word in content.split():
        words[word] += 1
    return words

def find_sources(content):
    short_content = content[-(len(content)/4):].lower()
    replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
    content_clean = short_content.translate(replace_punctuation)
    word_dict = word_counter(content_clean)
    word_set = set([key for key in word_dict])
    source_words = set(['source', 'sources', 'citation', 'citations', 'reference', 'references'])
    return int(any(word in word_set for word in source_words))

def find_credentials(content):
    word_dict = word_counter(content)
    word_set = set([key for key in word_dict])
    source_words = set(['MD', 'PhD', 'MPH', "RD", "M.D.", "R.D.", "M.P.H.", 'Ph.D.', 'DPhil'])
    return int(any(word in word_set for word in source_words))

def word_length(content):
    words = content.split()
    return sum([len(word) for word in words])/float(len(words))


def pos_tag_finder(content):
    content_clean = str(content).decode('utf-8').encode('ascii','ignore').replace('\n', '')
    tokens = word_tokenize(content_clean)
    tags = pos_tag(tokens)
    counts = Counter(tag for word,tag in tags)
    total = sum(counts.values())
    return dict((word, float(count)/total) for word,count in counts.items())

def create_pos_df():
    # all of the parts of speech, to be used in the dataframe below
    POS_list = ['PRP$', 'VBG', 'VBD', 'VBN', 'VBP', 'WDT', 'JJ', 'WP', 'VBZ', 'DT',
                '#', 'RP', '$', 'NN', ')', '(', ',', '.', 'TO', 'PRP', 'RB', ':',
                'NNS', 'NNP', 'VB', 'WRB', 'CC', 'PDT', 'RBS', 'RBR', 'CD', 'EX',
                'IN', 'WP$', 'MD', 'NNPS', 'JJS', 'JJR', 'UH', 'FW', 'LS', 'POS', 'SYM', '``', "''"]

    #create a list of all the parts of speech for all articles, with each element in the list corresponding to it's article
    PoS_tag_list = []
    for row in all_content['article']:
        PoS_tag_list.append(dc.pos_tag_finder(row))

    #create a dataframe with this list of PoS tags
    PoS_df = pd.DataFrame(PoS_tag_list)
    return PoS_df.reset_index()

#Functions to clean text and then use Naive-Bayes on the text column
def tokenize(text_column):
    text_list = list(text_column)
    #convert all lines to strings (some were floats (?)
    string_list = []
    for item in text_list:
        string_list.append(str(item))
    # decode unicode into ascii
    content_clean = []
    for item in string_list:
        content_clean.append(item.decode('utf-8').encode('ascii','ignore').replace('\n', ''))
    tokenized_list = [word_tokenize(content.lower()) for content in content_clean]
    return tokenized_list

def stem(content, stemmer ='snowball' ):
    content_clean = content.decode('utf-8', errors='ignore').encode('ascii',errors='ignore').replace('\n', ' ')
    if stemmer=='snowball':
        stemmed = [snowball.stem(word) for word in content_clean.split(' ')]
    return ' '.join(stemmed)

def add_columns(dataframe):
    dataframe['credentials'] = dataframe['article'].apply(find_credentials)
    dataframe['unique_words'] = dataframe['article'].apply(unique_word_pct)
    dataframe['content_length'] = dataframe['article'].apply(len)
    dataframe['sources'] = dataframe['article'].apply(find_sources)
    dataframe['avg_word_length'] = dataframe['article'].apply(word_length)
    dataframe['uppercase_title'] = dataframe['title'].apply(title_capitals)
    dataframe['exclamations_title'] = dataframe['title'].apply(find_exclamations)
    dataframe['exclamations_content'] = dataframe['article'].apply(find_exclamations)
    dataframe['stemmed_content'] = dataframe['article'].apply(stem)
    pos_dict = pos_tag_finder(dataframe['article'][0])
    for key, value in pos_dict.iteritems():
        pos_content = dataframe.set_value(0, col=key, value=value)
    pos_content = pos_content.fillna(0)
    return pos_content
