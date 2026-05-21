def first_occurrence(arr, n, key):
    low = 0
    high = n - 1
    result = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            result = mid
            high = mid - 1     # move left
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return result


def last_occurrence(arr, n, key):
    low = 0
    high = n - 1
    result = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            result = mid
            low = mid + 1      # move right
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return result



T = int(input())
arr=[]
while T > 0:
    n = int(input())
    for _ in range(n):
        arr.append(int(input()))

    key = int(input())

    first = first_occurrence(arr, n, key)

    if first == -1:
        print("Key not present")
    else:
        last = last_occurrence(arr, n, key)
        count = last - first + 1
        print(f"{key}-{count}")
    arr.clear()
    T -= 1
