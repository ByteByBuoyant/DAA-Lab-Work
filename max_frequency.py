'''Given an array of alphabets (with possible duplicates), find the element 
with maximum occurrences using counting technique. 
If all elements are unique, print "No Duplicates Present".
Process multiple test cases.
Time Complexity: O(n)'''

T = int(input())

for _ in range(T):
    n = int(input())
    arr = input().split()   # alphabets

    freq = {}

    # Count frequency
    for ch in arr:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    max_count = 0
    max_char = ''

    for ch in freq:
        if freq[ch] > max_count:
            max_count = freq[ch]
            max_char = ch

    if max_count == 1:
        print("No Duplicates Present")
    else:
        print(max_char, max_count)