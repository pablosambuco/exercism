def distance(strand_a, strand_b):
    largo = len(strand_a)
    if len(strand_b) != largo:
        raise ValueError("Strands must be of equal length.")
    return sum(strand_a[i] != strand_b[i] for i in range(largo))
