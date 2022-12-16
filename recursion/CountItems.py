def countArray(items):
    if not items:
        return 0
    return 1 + countArray(items[1:])


if __name__ == "__main__":
    myItems = [29, 4, 23, 9, 1, 0, 5, 2]

    print("Items on array: " + str(countArray(myItems)))
