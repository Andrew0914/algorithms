from heapq import heappop, heappush


class MedianOfStream:
    def __init__(self):
        self.heap = []

    def add_number(self, num: float) -> None:
        heappush(self.heap, num)

    def get_median(self) -> float:
        n = len(self.heap)
        temp = []

        if n == 0:
            return 0
        elif n == 1:
            return self.heap[0]

        limit = (n // 2) + 1

        for _ in range(limit):
            temp.append(heappop(self.heap))

        for value in temp:
            heappush(self.heap, value)

        if n % 2 == 0:
            return (temp[-1] + temp[-2]) / 2
        else:
            return temp[-1]


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
