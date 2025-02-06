

from math import inf
import random


def quicksort(nums):
    def qsort(nums, l, r):
        if l >= r:
            return
        p = random.randint(l, r)
        pivot = nums[p]
        nums[p] = nums[l]
        i = l + 1
        p = l
        while i <= r:
            if nums[i] < pivot:
                nums[p+1], nums[i] = nums[i], nums[p+1]
                nums[p] = nums[p+1]
                p += 1
            i += 1
        nums[p] = pivot
        qsort(nums, l, p-1)
        qsort(nums, p+1, r)
                
    qsort(nums, 0, len(nums)-1)

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 100, 0, 0, 4, 3]
nums0 = []
nums1 = [1]
nums2 = [1, 0]

quicksort(nums)
print(nums)
quicksort(nums0)
print(nums0)
quicksort(nums1)
print(nums1)
quicksort(nums2)
print(nums2)