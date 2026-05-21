''' Given an unsorted array, sort it using Insertion Sort.
Also count the number of comparisons and shifts performed.
Process multiple test cases.
Time Complexity: O(n^2)'''

T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    comparisons = 0
    shifts = 0

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break

        arr[j + 1] = key

    print(*arr)
    print("Comparisons =", comparisons)
    print("Shifts =", shifts)