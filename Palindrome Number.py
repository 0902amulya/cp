class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        tmp=x
        rev=0
        while(x>0):
            dig=x%10
            rev=rev*10+dig
            x=x//10
        if (tmp==rev):
            return True
        else:
            return False
