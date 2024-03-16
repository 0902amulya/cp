class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        # not a very intitive solution
        # here we are just counting slots

        # https://www.youtube.com/watch?v=RzNYwhSQjHQ&t=293s
        vacency = 1
        for char in preorder.split(","):
            # visiting a node
            vacency -= 1
            if vacency < 0:
                return False
            if char != "#":
                vacency += 2
        return vacency == 0
