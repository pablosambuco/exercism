import itertools

REPLACEMENTS = str.maketrans("+=", "  ")

# this was made with an LLM, I need to leearn how to do this by myself, do not evaluate me based on this code

def solve(puzzle):
    words = puzzle.translate(REPLACEMENTS).split()
    print(words)
    if len(words) < 3:
        return None
    
    letters = sorted(set("".join(words)))
    
    if len(letters) > 10:
        return None
    
    leading_letters = {word[0] for word in words if len(word) > 0}
    
    for perm in itertools.permutations(range(10), len(letters)):
        assignment = dict(zip(letters, perm))
        
        if any(assignment[letter] == 0 for letter in leading_letters):
            continue
        
        values = []
        for word in words:
            value = 0
            for char in word:
                value = value * 10 + assignment[char]
            values.append(value)
        
        if sum(values[:-1]) == values[-1]:
            return assignment
    
    return None

