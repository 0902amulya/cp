class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst_num=list(str(n))
        flag=len(lst_num)
        for i in range(len(lst_num)-1,0,-1):
            if lst_num[i-1]>lst_num[i]:
                flag=i
                lst_num[i-1]=str(int(lst_num[i-1])-1)
        for i in range(flag,len(lst_num)):
            lst_num[i]='9'
        return int("".join(lst_num)) 
