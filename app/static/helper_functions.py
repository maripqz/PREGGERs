


# functions to used to add additional columns to test text
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

def pos_tag_finder(content):
    content_clean = str(content).decode('utf-8').encode('ascii','ignore').replace('\n', '')
    tokens = word_tokenize(content_clean)
    tags = pos_tag(tokens)
    counts = Counter(tag for word,tag in tags)
    total = sum(counts.values())
    return dict((word, float(count)/total) for word,count in counts.items())

def find_sources(content):
    short_content = content[-(len(content)/4):].lower()
    replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
    content_clean = short_content.translate(replace_punctuation)
    word_dict = word_counter(content_clean)
    word_set = set([key for key in word_dict])
    source_words = set(['source', 'sources', 'citation', 'citations', 'reference', 'references'])
    return int(any(word in word_set for word in source_words))

def stem(content, stemmer ='snowball' ):
    content_clean = content.decode('utf-8', errors='ignore').encode('ascii',errors='ignore').replace('\n', ' ')
    if stemmer=='snowball':
        stemmed = [snowball.stem(word) for word in content_clean.split(' ')]
    return ' '.join(stemmed)

def find_credentials(content):
    word_dict = word_counter(content)
    word_set = set([key for key in word_dict])
    source_words = set(['MD', 'PhD', 'MPH', "RD", "M.D.", "R.D.", "M.P.H.", 'Ph.D.', 'DPhil'])
    return int(any(word in word_set for word in source_words))

def word_length(content):
    words = content.split()
    return sum([len(word) for word in words])/float(len(words))

def title_capitals(title):
    title = str(title).strip()
    return sum([1 for letter in title if letter.isupper()])/float(len(title))

def add_columns(df):
    dataframe = df
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
