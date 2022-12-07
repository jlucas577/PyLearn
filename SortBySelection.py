class SortBySelection:
    def smallerSearch(self, items):
        smaller_value = items[0]
        smaller_index = 0

        for i in range(1, len(items)):
            if items[i] < smaller_value:
                smaller_value = items[i]
                smaller_index = i
        return smaller_index

    def order(self, items):
        new_items = []

        for i in range(1, len(items)):
            smaller = self.smallerSearch(items)
            new_items.append(items.pop(smaller))
        return new_items


if __name__ == "__main__":
    sortBySelection = SortBySelection()
    myItems = [5, 3, 16, 6, 2, 10, 8]

    print("Sorted array: " + str(sortBySelection.order(myItems)))
