def greaterValue(items):
    if len(items) == 2:
        return items[0] if items[0] > items[1] else items[1]
    max_value = greaterValue(items[1:])
    return items[0] if items[0] > max_value else max_value


if __name__ == "__main__":
    myItems = [1, 3, 5, 6, 10, 2, 20, 9, 4, 16]

    print("Greater value on array: " + str(greaterValue(myItems)))
