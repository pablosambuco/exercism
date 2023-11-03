def find_anagrams(word, candidates):
    letters = {}
    for letter in word:
        if letter.upper() in letters:
            letters[letter.upper()] += 1
        else:
            letters[letter.upper()] = 1

    anagrams = []

    for candidate in candidates:
        if candidate.upper() == word.upper():
            continue
        candidate_letters = {}
        for letter in candidate:
            if letter.upper() in candidate_letters:
                candidate_letters[letter.upper()] += 1
            else:
                candidate_letters[letter.upper()] = 1
        if letters == candidate_letters:
            anagrams.append(candidate)

    return anagrams
