'''
Given an array of non-negative integers, count the number of pairs 
such that the difference between elements is equal to a given key K.
Process multiple test cases and print total count for each case.
Time Complexity: O(n log n)'''

T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())

    arr.sort()
    count = 0
    i, j = 0, 1

    while j < n:
        if i != j and arr[j] - arr[i] == k:
            count += 1
            i += 1
            j += 1
        elif arr[j] - arr[i] < k:
            j += 1
        else:
            i += 1

    print(count)