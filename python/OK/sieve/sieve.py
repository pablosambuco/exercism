def primes(limit):
    is_prime = [x for x in range(limit + 1)]
    for x in range(2, int(limit**0.5) + 1):
        if is_prime[x]:
            for y in range(x * 2, limit + 1, x):
                is_prime[y] = False
    return [x for x in is_prime[2:] if is_prime[x]]
