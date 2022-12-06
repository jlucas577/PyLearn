class BinarySearch:
    def search(self, items, target):
        low = 0
        high = len(items) - 1

        while low <= high:
            middle = (low + high) // 2
            tip = items[middle]

            if tip == target:
                return middle
            if tip > target:
                high = middle - 1
            else:
                low = middle + 1
        return None


if __name__ == "__main__":
    binarySearch = BinarySearch()
    my_items = [1, 3, 5, 7, 9]

    print("Position of '3' value: " + str(binarySearch.search(my_items, 3)))
    print("Position of '-1' value: " + str(binarySearch.search(my_items, -1)))
    print("Position of '9' value: " + str(binarySearch.search(my_items, 9)))
