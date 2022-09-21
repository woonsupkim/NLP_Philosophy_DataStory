def remove_punc(string):
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~ '''
    for ele in string:  
        if ele in punc:  
            string = string.replace(ele, "") 
    return string


def generate_ngrams(text, n_gram=1):
    from wordcloud import WordCloud, STOPWORDS
    stopwords = set(STOPWORDS)

    #Enhanced stopwording
    more_stopwords = {'  ', '   '}
    stopwords = stopwords.union(more_stopwords)

    import nltk
    from nltk.tokenize import word_tokenize
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    #text = tokenizer.tokenize(text)

    token = [token for token in text.split(" ") if token != "" if token not in stopwords]
    token = [remove_punc(i) for i in token]
    #token = [token for token in tokenizer.tokenize(text) if token != "" if token not in STOPWORDS]
    
    ngrams = zip(*[token[i:] for i in range(n_gram)])
    return [" ".join(ngram) for ngram in ngrams]


## custom function for horizontal bar chart ##
def horizontal_bar_chart(df, color):
    import plotly.graph_objs as go

    trace = go.Bar(
        y=df["word"].values[::-1],
        x=df["wordcount"].values[::-1],
        showlegend=False,
        orientation = 'h',
        marker=dict(
            color=color,
        ),
    )
    return trace


## Word count function
def count_words(string):
    string1 = string.strip()
    count = 1
    for i in string1:
        if i == " ":
            count = count + 1
    return count