'''Given a sorted array, perform Jump Search by checking elements
at fixed intervals and then applying linear search in the identified range. 
Also count the number of comparisons and determine if the key is present
Time Complexity: O(√n) (i.e., < O(n))'''

import math

T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    key = int(input())

    comparisons = 0
    step = int(math.sqrt(n))  # optimal jump size

    prev = 0
    found = False

    # Step 1: Jumping phase
    while prev < n:
        comparisons += 1
        if arr[min(prev + step, n) - 1] >= key:
            break
        prev += step

    # Step 2: Linear search in block
    for i in range(prev, min(prev + step, n)):
        comparisons += 1
        if arr[i] == key:
            found = True
            break

    if found:
        print("Present", comparisons)
    else:
        print("Not Present", comparisons)