class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        n1 = len(nums1)
        n2 = len(nums2)

        nums1.append(inf)
        nums2.append(inf)

        i = j = 0
        ans = []
        while i != n1 and j != n2:
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j+=1
        return ans
