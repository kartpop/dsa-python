

from math import inf


def mergesort(nums):
    if len(nums) == 0 or len(nums) == 1:
        return nums
    
    def merge(left, right):
        out = []
        i, j = 0, 0
        while i < len(left) or j < len(right):
            lcur, rcur = inf, inf
            if i < len(left) and left[i] < lcur:
                lcur = left[i]
            if j < len(right) and right[j] < rcur:
                rcur = right[j]
            if lcur < rcur:
                out.append(lcur)
                i += 1
            else:
                out.append(rcur)
                j += 1
        return out
    
    l, r = 0, len(nums)-1
    m = l + (r - l) // 2
    left, right = mergesort(nums[:m+1]), mergesort(nums[m+1:])
    
    return merge(left, right)
    
        
    
    

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 100, 0, 0, 4, 3]
nums0 = []
nums1 = [1]
nums2 = [1, 0]
print(mergesort(nums))
print(mergesort(nums0))
print(mergesort(nums1))
print(mergesort(nums2))