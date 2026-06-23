def intersection(nums1, nums2):
    set1 = set(nums1)
    result = set()

    for num in nums2:
        if num in set1:
            result.add(num)

    return list(result)

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(intersection(nums1, nums2))