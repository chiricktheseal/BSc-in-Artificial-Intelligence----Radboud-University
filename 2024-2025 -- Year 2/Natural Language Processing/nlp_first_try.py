import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text = "Я стремлюсь стать дата-сайентистом."
word_tokens = word_tokenize(text)
print(word_tokens)

text2 = "I dkjdnqjkndj. i love you. but does Mr. brown loves me?"
sent_tokens = sent_tokenize(text2)
print(sent_tokens)

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

print(stemmer.stem("running"))  # → "runn"
print(stemmer.stem("better"))   # → "better" (неправильно)
print(stemmer.stem("caring"))   # → "car"


from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("running", pos="v"))  # → "run"
print(lemmatizer.lemmatize("better", pos="a"))   # → "good"
print(lemmatizer.lemmatize("caring", pos="v"))   # → "care"

