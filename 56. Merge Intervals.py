# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        i = 0
        output = []
        while i <= len(intervals) - 1:
            j = 1
            while j <= len(intervals) - 1 - i:
                if intervals[i].end > intervals[i + j].start:
                    j += 1
                else:
                    break

            # merge i to j-1

            output.append(Interval(intervals[i].start, intervals[i + j- 1].end))

            i += j
        return output

input= [Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)]

sol = Solution()
sol.merge(input)