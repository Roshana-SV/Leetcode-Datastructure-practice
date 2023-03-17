class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        num=[]
        for i in range(m):
            x=nums1[i]
            num.append(x)
        for i in range(n):
            x=nums2[i]
            num.append(x)
        num.sort()
        del nums1[:]
        nums1.extend(num)
