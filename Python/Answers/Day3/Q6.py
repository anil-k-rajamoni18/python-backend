sentence = "Python is widely used and Python is easy to learn"
stopwords = {"is", "and", "to"}

#Remove stopwords
sentence=sentence.replace("is","")
sentence=sentence.replace("and","")
sentence=sentence.replace("to","")
print(sentence)

#Count unique meaningful words
meaningfulWords=sentence.split()
print(meaningfulWords)
print(f"The number of meaningful words is {len(meaningfulWords)}")

#Create a list sorted by word length
meaningfulWords.sort(key=len)
print(meaningfulWords)