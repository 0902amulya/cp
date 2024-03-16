import sys
class MinStack(object):

    def __init__(self):
        self.stack= []
        self.min = sys.maxsize
        x=None 
        

    def push(self,x) :
        self.min=min(self.min,x)
        self.stack.append([x,self.min])
        

    def pop(self):
        self.stack.pop()
        if(self.stack):
            self.min=self.stack [-1][1]
        else:
            self.min=sys.maxsize
    def top(self):
        return self.stack[-1][0]

        

    def getMin(self):
        return self.stack[-1][1]
