class Solution(object): # time o(n) and space o(n)-> max can be o(n)
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height == []: return 0

        # find all the max elements
        maxElement = []
        maxValue = max(height)
        for i in range(len(height)):
            if height[i] == maxValue:
                maxElement.append(i)

        output = 0
        # from beginning to fist max
        jumpTag = 0
        for i in range(maxElement[0]):
            i += jumpTag
            j = i + 1
            if i >= maxElement[0]: break
            while height[j] < height[i]:
                output += height[i] - height[j]
                j += 1
                if j >= maxElement[0] + 1: break
            jumpTag += j - i - 1

        # from end to last max
        jumpTag = 0
        for i in range(len(height) - 1, maxElement[-1], -1):
            i -= jumpTag
            j = i - 1
            if i <= maxElement[-1]: break
            while height[j] < height[i]:
                output += height[i] - height[j]
                j -= 1
                if j <= maxElement[-1] - 1: break
            jumpTag += i - j - 1

        # between maxs
        for i in range(maxElement[0], maxElement[-1]):
            output += maxValue - height[i]

        return output