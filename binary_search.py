'''Given an already sorted array of positive integers, design an
algorithm and implement it using a program to find whether given key
element is present in the array or not. Also, find total number of
comparisons for each input case. (Time Complexity = O(nlogn), where
n is the size of input).'''
arr = list(map(int, input("Enter sorted array: ").split()))
key = int(input("Enter key: "))

low = 0
high = len(arr) - 1
comparisons = 0
found = False

while low <= high:
    mid = (low + high) // 2
    comparisons += 1

    if arr[mid] == key:
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Present")
else:
    print("Not Present")

print("Comparisons =", comparisons)