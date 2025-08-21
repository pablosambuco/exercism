def distance(strand_a, strand_b):
    largo = len(strand_a)
    if len(strand_b) != largo:
        raise ValueError("Strands must be of equal length.")
    return sum(1 for i in range(largo) if strand_a[i] != strand_b[i])
