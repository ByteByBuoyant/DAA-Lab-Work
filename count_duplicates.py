'''Given a sorted array of positive integers that may contain duplicate elements, 
use Binary Search to determine whether a given key element is present or not.
If the key is present, find and print the number of occurrences of the key in the array; 
otherwise, print “Key not present”. 
Also process multiple test cases as per input format.
Time Complexity: O(log n)'''

def first_occurrence(arr, n, key):
    low, high = 0, n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            ans = mid
            high = mid - 1   # go left
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return ans


def last_occurrence(arr, n, key):
    low, high = 0, n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            ans = mid
            low = mid + 1   # go right
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return ans


T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    key = int(input())

    first = first_occurrence(arr, n, key)

    if first == -1:
        print("Key not present")
    else:
        last = last_occurrence(arr, n, key)
        count = last - first + 1
        print(key, count)