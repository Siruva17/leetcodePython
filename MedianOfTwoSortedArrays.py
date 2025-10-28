class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array to minimize the binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        
        left, right = 0, m
        while True:
            i = (left + right) // 2  # Partition index in nums1
            j = half - i             # Partition index in nums2
            
            # Handle boundaries using -inf and inf
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')
            
            # Check if correct partition is found
            if left1 <= right2 and left2 <= right1:
                # Even total length
                if total % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                # Odd total length
                else:
                    return min(right1, right2)
            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1
