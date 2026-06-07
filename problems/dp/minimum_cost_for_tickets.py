def minimum_cost_for_tickets(days: list[int], costs: list[int]) -> int:
    last_day = days[-1]
    dp = [0] * 31
    travel_days = set(days)

    def offset(day):
        return 30 if day % 30 == 0 else day % 30

    for day in range(1, last_day + 1):
        if day not in travel_days:
            dp[offset(day)] = dp[offset(day - 1)]
        else:
            dp[offset(day)] = min(
                dp[offset(day - 1)] + costs[0],
                dp[max(0, offset(day - 7))] + costs[1],
                dp[max(0, offset(day - 30))] + costs[2],
            )

    return dp[30 if last_day % 30 == 0 else last_day % 30]


costs = [2, 7, 15]
days = [1, 4, 6, 7, 8, 20]
assert minimum_cost_for_tickets(days, costs) == 11
print("11 ✅")
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
assert minimum_cost_for_tickets(days, costs) == 17
print("17 ✅")
days = [1]
assert minimum_cost_for_tickets(days, costs) == 2
print("2 ✅")
days = [
    1,
    2,
    3,
    7,
    9,
    11,
    13,
    16,
    19,
    21,
    23,
    25,
    27,
    29,
    89,
    344,
    345,
    346,
    347,
    348,
    350,
]
assert minimum_cost_for_tickets(days, costs) == 24
print("24 ✅")
