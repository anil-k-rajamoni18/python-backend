sentences = [
  "python is great for data",
  "data science uses python",
  "machine learning requires data"
]
stopwords={"is","for","uses","requires"}
#Create an inverted index:
invertedIndex={}


for i, sentence in enumerate(sentences):
    words=sentence.split()
    uniquewords=set(words)-stopwords
    for word in uniquewordswords:
        invertedIndex.setdefault(word,[]).append(i)
print(invertedIndex)

"""
#Remove stopwords (is, for, uses, requires)
stopwords=["is","for","uses","requires"]
for stopword in stopwords:
    del invertedIndex[stopword]
print(invertedIndex)
"""
