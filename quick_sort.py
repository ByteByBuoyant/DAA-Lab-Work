'''
Given an unsorted array, sort it using Quick Sort with a randomly 
selected pivot. Also count the number of comparisons and swaps.
Process multiple test cases.
Time Complexity: O(n log n) (average)
'''
import random

comparisons = 0
swaps = 0

def partition(arr, low, high):
    global comparisons, swaps

    # Random pivot selection
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    swaps += 1

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swaps += 1

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


T = int(input())

for _ in range(T):
    comparisons = 0
    swaps = 0

    n = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, n - 1)

    print(*arr)
    print("Comparisons =", comparisons)
    print("Swaps =", swaps)