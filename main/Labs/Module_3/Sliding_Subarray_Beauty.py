# Problem Statement:
# You are given an array of integers arr and an integer k. Your task is to find the given n th position of the smallest integer in each contiguous subarray of size k and print these smallest integers. 
# A subarray is a contiguous non-empty sequence of elements within the original array. For each subarray of size k, you need to find the given n th position of the smallest integer within that subarray. 
# The given n th position of the smallest integer in a subarray is the integer that appears at the given n th position when the subarray is sorted in ascending order. Your task is to return an integer array 
# containing n - k + 1 elements, denoting the beauty of the subarrays in order from the first index in the array.

# Exercise-1 :
# Input: 
# 1 2 3 4 5 6 7 8 9 10
# 3
# 2
# Note: 
# Line 1: input array
# Line 2: sub array length
# Line 3: position of the smallest value
# Output:
# 2 3 4 5 6 7 8 9

# Exercise-2 :
# Input:
# 1 2 3 4 5 6 7 8 9 10
# 4
# 2
# Output:
# 2 3 4 5 6 7 8

def ssb(arr, k, n):
    res = []
    
    def nth_sisa(sa, n):
        s_sa = sorted(sa)
        return s_sa[n-1]
    c_sa = arr[:k]
    res.append(nth_sisa(c_sa, n))
    
    for i in range(k, len(arr)):
        c_sa.pop(0)
        c_sa.append(arr[i])
        res.append(nth_sisa(c_sa, n))
    return res

arr = list(map(int, input().split()))
k = int(input())
n = int(input())
res = ssb(arr, k, n)
for i in res:
    print(i, end=" ")