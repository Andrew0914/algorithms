from operator import le


class QuickSort:
    def __init__(self, arr):
        self.arr = arr

    def _swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def _partition(self, left, right):
        pivot = self.arr[right]
        pivot_pos = right
        right = right - 1

        while True:
            while self.arr[left] < pivot:
                left += 1

            while self.arr[right] > pivot:
                right -= 1

            if left >= right:
                break

            self._swap(left, right)

        self._swap(left, pivot_pos)
        return left

    def _sort(self, left, right):
        if right - left <= 0:
            return
        pivot_pos = self._partition(left, right)
        self._sort(left, pivot_pos - 1)
        self._sort(pivot_pos + 1, right)

    def sort(self):
        self._sort(0, len(self.arr) - 1)

    def _select(self, left, right, k):
        if right - left <= 0:
            return

        pivot_pos = self._partition(left, right)

        if k < pivot_pos:
            return self._select(left, pivot_pos - 1, k)
        elif k > pivot_pos:
            return self._select(pivot_pos + 1, right, k)
        else:
            return self.arr[pivot_pos]

    def select(self, k):
        return self._select(0, len(self.arr) - 1, k)


nums = [0, 50, 20, 10, 60, 30]

qs = QuickSort(nums)
print(qs.select(2))
