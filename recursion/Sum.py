def sumArray(items):
    if not items:
        return 0
    return items[0] + sumArray(items[1:])


if __name__ == "__main__":
    myItems = [2, 9, 20, 1, 34]

    print("Summed array: " + str(sumArray(myItems)))
