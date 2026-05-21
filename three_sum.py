'''Given a sorted array of positive integers, find three indices i, j, k such that arr[i] + arr[j] = arr[k].
For each test case, print the indices if such a triplet exists, otherwise print “No sequence found”.
Time Complexity: O(n²)'''

T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    found = False

    for k in range(n - 1, -1, -1):
        i = 0
        j = k - 1

        while i < j:
            if arr[i] + arr[j] == arr[k]:
                print(i, j, k)
                found = True
                break
            elif arr[i] + arr[j] < arr[k]:
                i += 1
            else:
                j -= 1

        if found:
            break

    if not found:
        print("No sequence found")