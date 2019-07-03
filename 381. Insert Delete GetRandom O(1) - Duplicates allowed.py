import random


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = {}
        self.l = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.s:
            self.l.append(val)
            self.s[val].append(len(self.l) - 1)
            return False
        self.l.append(val)
        self.s[val] = [len(self.l) - 1]
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.s:
            return False
        index = self.s[val].pop()
        if not self.s[val]:
            lastnum = self.l[-1]
            self.l[index] = lastnum
            self.l.pop()
            self.s.pop(val)
        if val == self.l[index]:
            return True

        lastnum = self.l[-1]
        self.l[index] = lastnum
        self.l.pop()
        self.s[lastnum].pop()
        self.s[lastnum].append(index)

        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.l[random.randint(0, len(self.l) - 1)]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
"""
sol = RandomizedCollection()
sol.insert(9)
sol.insert(9)
sol.insert(1)
sol.insert(1)
sol.insert(2)
sol.insert(1)
sol.remove(2)
sol.remove(1)
sol.remove(1)
sol.insert(9)
sol.remove(1)
"""
sol = RandomizedCollection()
sol.insert(0)
sol.remove(0)
sol.insert(-1)
sol.remove(0)
print(sol.getRandom())
print(sol.getRandom())
print(sol.getRandom())
print(sol.getRandom())
print(sol.getRandom())