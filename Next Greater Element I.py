class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        for i in nums1:
            j=nums2.index(i)+1
            max= -1
            while j <len(nums2):
                if (nums2[j]>i):
                    max=nums2[j]
                    break;
                j+=1
            stack.append(max)
        return stack
