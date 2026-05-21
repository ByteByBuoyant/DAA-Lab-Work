''' Given an unsorted array, sort it using Selection Sort.
Also count the number of comparisons and swaps performed.
Process multiple test cases.
Time Complexity: O(n^2) '''

T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    comparisons = 0
    swaps = 0

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1

    print(*arr)
    print("Comparisons =", comparisons)
    print("Swaps =", swaps)