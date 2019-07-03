class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        import math
        self.min = math.inf

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if (x <= self.min):
            self.data.append(self.min)
            self.min = x

        self.data.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if (self.data.pop() == self.min): self.min = self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

# Your MinStack object will be instantiated and called as such:
obj = MinStack()


obj.push(-2)
obj.push(0)
obj.push(-3)
obj.push(1)
param_4 = obj.getMin()
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_4)

