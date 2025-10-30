import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()
text = "The leaves on the trees are falling and the children were playing happily."
words = word_tokenize(text)

print("Original Word  -->  Lemmatized Word")
print("-" * 40)
for word in words:
    lemma = lemmatizer.lemmatize(word)
    print(f"{word:15} -->  {lemma}")

print("\nLemmatization with POS Tagging:")
print("-" * 40)
lemmatized_verbs = [lemmatizer.lemmatize(word, pos='v') for word in words]
for w, l in zip(words, lemmatized_verbs):
    print(f"{w:15} -->  {l}")
