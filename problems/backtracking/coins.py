def coin_change(coins: list[int], amount: int) -> int:
    memo = {}

    def backtrack(change=0, coins_count=0, min_coins=0):

        # is leaf
        if change == amount:
            return min(min_coins, coins_count)

        # second prune
        if coins_count >= min_coins:
            return min_coins

        # Memoization
        if change in memo and coins_count >= memo[change]:
            return min_coins
        memo[change] = coins_count

        for coin in coins:
            # prune
            if change + coin > amount:
                continue
            min_coins = backtrack(change + coin, coins_count + 1, min_coins)

        return min_coins

    IMPOSSIBLE = amount + 1
    minimun = backtrack(0, 0, min_coins=IMPOSSIBLE)
    print(memo)
    return -1 if minimun == IMPOSSIBLE else minimun


coins = [1, 2, 5]
amount = 11
print(
    f"Need ({coin_change(coins, amount)}) at least to have {amount} with coins {coins}"
)
