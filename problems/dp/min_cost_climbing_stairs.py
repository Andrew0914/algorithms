def min_cost_climbing_stairs(cost: list[int]) -> int:
    n = len(cost)

    if n <= 2:
        return min(cost)

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 0

    for i in range(2, n + 1):
        dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        # curr = min(prev2 + cost[i - 2], prev1 + cost[i - 1])
        # prev2, prev1 = prev1, curr

    return dp[-1]


costs = [10, 15, 20]
assert min_cost_climbing_stairs(costs) == 15, f"RIGHT ANSWER IS {15}"
print("✅")
costs = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
assert min_cost_climbing_stairs(costs) == 6, f"RIGHT ANSWER IS {6}"
print("✅")
costs = [1, 2, 3, 4, 5]
assert min_cost_climbing_stairs(costs) == 6, f"RIGHT ANSWER IS {6}"
print("✅")
