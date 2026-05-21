'''Given an unsorted array, find the Kth smallest or largest element 
using Quick Select. If not present, print "not present".
Process multiple test cases.
Time Complexity: O(n) (average), O(n^2) worst case'''

def partition(arr, low, high):
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i


def quick_select(arr, low, high, k):
    if low <= high:
        pi = partition(arr, low, high)

        if pi == k:
            return arr[pi]
        elif pi > k:
            return quick_select(arr, low, pi - 1, k)
        else:
            return quick_select(arr, pi + 1, high, k)

    return -1


T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())

    if k > n:
        print("not present")
    else:
        # Kth smallest
        ans = quick_select(arr, 0, n - 1, k - 1)
        print(ans)