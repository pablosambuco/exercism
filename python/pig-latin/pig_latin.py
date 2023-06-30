"""pig latin
"""


def cut_consonants(word):
    consonant_cluster = ""
    rest_of_word = ""

    # Rule 1
    ant = None
    for c in word:
        if c in ("a", "e", "i", "o", "u"):
            break
        if c == "y" and ant:
            break
        if c == "r" and ant == "x" or c == "t" and ant == "y":
            consonant_cluster = consonant_cluster[:-1]
            break
        consonant_cluster += c
        ant = c
    rest_of_word = word[len(consonant_cluster) :]
    print(consonant_cluster, rest_of_word)

    # Rule 3
    if consonant_cluster and consonant_cluster[-1] == "q" and rest_of_word and rest_of_word[0] == "u":
        consonant_cluster += "u"
        rest_of_word = rest_of_word[1:]
    print(consonant_cluster, rest_of_word)

    return consonant_cluster, rest_of_word


def translate(text):
    string = []
    for word in text.split(" "):
        c, r = cut_consonants(word)
        string.append(r + c + "ay")
    return " ".join(string)
