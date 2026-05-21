'''Given an array of nonnegative integers, design a linear algorithm
and implement it using a program to find whether given key element is
present in the array or not. Also, find total number of comparisons for
each input case. (Time Complexity = O(n), where n is the size of input)'''

arr = list(map(int, input("Enter array: ").split()))
key = int(input("Enter key: "))

comparisons = 0

for i in range(len(arr)):
    comparisons += 1
    if arr[i] == key:
        print("Present")
        print("Comparisons =", comparisons)
        break
else:
    print("Not Present")
    print("Comparisons =", comparisons)