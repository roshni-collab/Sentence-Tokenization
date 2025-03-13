from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')

text = input("Enter a paragraph: ")
sentences = sent_tokenize(text)

for i, sentence in enumerate(sentences, 1):
    print(f"{i}. {sentence}")
