def quickSort(items):
    if len(items) < 2:
        return items
    else:
        pivot = items[0]
        minors = [i for i in items[1:] if i <= pivot]
        biggers = [i for i in items[1:] if i > pivot]
        return quickSort(minors) + [pivot] + quickSort(biggers)


if __name__ == "__main__":
    myItems = [29, 4, 23, 1]

    print("QuickSort: " + str(quickSort(myItems)))
