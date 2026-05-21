'''Given an unsorted array of positive integers, check whether duplicate 
elements are present using sorting. Output YES if duplicates exist, 
otherwise NO. Process multiple test cases.
Time Complexity: O(n log n)'''

T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    found = False

    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            found = True
            break

    if found:
        print("YES")
    else:
        print("NO")