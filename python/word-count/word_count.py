import re


def count_words(sentence):
    sentence = re.findall("[0-9]|[a-z]+(?:'[a-z]+)?", sentence.lower())
    return {word: sentence.count(word) for word in sentence}
