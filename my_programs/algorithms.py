def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = round((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
        else:
            return None


my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]


print(binary_search(my_list, 11))
