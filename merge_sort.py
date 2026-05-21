'''Given an unsorted array, sort it using Merge Sort by dividing the array 
into two subarrays and merging them after sorting.
Also count the number of comparisons and inversions.
Process multiple test cases.
Time Complexity: O(n log n)'''

comparisons = 0
inversions = 0

def merge(arr, l, m, r):
    global comparisons, inversions

    L = arr[l:m+1]
    R = arr[m+1:r+1]

    i = j = 0
    k = l

    while i < len(L) and j < len(R):
        comparisons += 1
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            inversions += (len(L) - i)
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, r)
        merge(arr, l, mid, r)


T = int(input())

for _ in range(T):
    comparisons = 0
    inversions = 0

    n = int(input())
    arr = list(map(int, input().split()))

    merge_sort(arr, 0, n - 1)

    print(*arr)
    print("Comparisons =", comparisons)
    print("Inversions =", inversions)