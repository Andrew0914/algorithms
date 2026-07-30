# Pattern: dp
# Complexity: time O(n) and space O(1) since we are using just last 2 values
# Lesson: dp[i] = dp[i - 1] + dp[i - 2] becase to reach dp[i] extends from those one so the sum of that are the ways of i.
def climbing_stairs(n: int) -> int:
    if n <= 0:
        return 0

    if n == 1:
        return 1

    if n == 2:
        return 2

    before_prev = 1
    prev = 2
    for i in range(2, n):
        current = before_prev + prev
        before_prev, prev = prev, current

    return prev


assert climbing_stairs(4) == 5
