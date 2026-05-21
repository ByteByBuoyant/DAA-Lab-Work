'''Given an unsorted array, find two elements such that their sum is equal 
to a given key using sorting and two-pointer technique. 
If such elements exist, print them, otherwise print "No Such Elements Exist".
Process multiple test cases.
Time Complexity: O(n log n)'''

T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    key = int(input())

    arr.sort()
    i, j = 0, n - 1
    found = False

    while i < j:
        s = arr[i] + arr[j]

        if s == key:
            print(arr[i], arr[j])
            found = True
            break
        elif s < key:
            i += 1
        else:
            j -= 1

    if not found:
        print("No Such Elements Exist")