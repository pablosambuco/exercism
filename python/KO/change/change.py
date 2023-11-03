"""Fewest coins
Not proud of the algorithm, it was gtp all the way...
"""


def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")

    minimal_coins = {0: []}

    for t in range(1, target + 1):
        minimal_coins[t] = None
        for coin in coins:
            if t - coin >= 0 and minimal_coins[t - coin] is not None:
                current_combination = minimal_coins[t - coin] + [coin]
                if minimal_coins[t] is None or len(current_combination) < len(
                    minimal_coins[t]
                ):
                    minimal_coins[t] = current_combination

    minimal = minimal_coins[target]
    if minimal is None:
        raise ValueError("can't make target with given coins")

    return sorted(minimal)
