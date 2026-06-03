from heapq import heappop, heappush


class MedianOfStream:
    def __init__(self):
        self.smaller = []
        self.larger = []

    def add_number(self, num: float) -> None:
        if len(self.larger) == 0 or num >= self.larger[0]:
            heappush(self.larger, num)
        else:
            heappush(self.smaller, -num)
        self._balance()

    def _balance(self):
        if len(self.larger) < len(self.smaller):
            val = heappop(self.smaller)
            heappush(self.larger, -val)
        if len(self.larger) > len(self.smaller) + 1:
            val = heappop(self.larger)
            heappush(self.smaller, -val)

    def get_median(self) -> float:
        if len(self.larger) > len(self.smaller):
            return self.larger[0]

        return (self.larger[0] + -self.smaller[0]) / 2


mo = MedianOfStream()
mo.add_number(5)
mo.add_number(15)
assert mo.get_median() == 10.0, f"Wrong {mo.get_median()}"
print("✅")
mo.add_number(1)
assert mo.get_median() == 5.0, f"Wrong {mo.get_median()}"
print("✅")
mo.add_number(3)
assert mo.get_median() == 4.0, f"Wrong {mo.get_median()}"
print("✅")
