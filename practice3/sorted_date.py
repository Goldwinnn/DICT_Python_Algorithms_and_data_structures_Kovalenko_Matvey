from list_extra import CustomList
class SortedList(CustomList):
    def append(self, value):
        index = self._binary_search(value)
        super().insert(index, value)

    def insert(self, index, value):
        raise NotImplementedError("The 'insert' operation is not supported in a sorted list!")

    def search(self, value):
        return self._recursive_binary_search(value, 0, self.size - 1)

    def _binary_search(self, value):
        left = 0
        right = self.size
        while left < right:
            mid = (left + right) // 2
            if self.array[mid] < value:
                left = mid + 1
            else:
                right = mid
        return left

    def _recursive_binary_search(self, value, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if self.array[mid] == value:
            return mid
        elif self.array[mid] < value:
            return self._recursive_binary_search(value, mid + 1, right)
        else:
            return self._recursive_binary_search(value, left, mid - 1)
