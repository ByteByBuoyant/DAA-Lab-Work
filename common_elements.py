'''Given two sorted arrays, find the list of common elements using 
two-pointer technique. Print all common elements.
Time Complexity: O(m + n)'''

m = int(input())
arr1 = list(map(int, input().split()))

n = int(input())
arr2 = list(map(int, input().split()))

i, j = 0, 0
result = []

while i < m and j < n:
    if arr1[i] == arr2[j]:
        result.append(arr1[i])
        i += 1
        j += 1
    elif arr1[i] < arr2[j]:
        i += 1
    else:
        j += 1

print(*result)