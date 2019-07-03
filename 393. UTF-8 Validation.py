class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(data):
            binNum = str(bin(data[i]))[2:]
            if len(binNum) < 8:
                i += 1
            else:
                tmp = len(binNum.split("0")[0]) - 1
                while tmp > 0:
                    if i + tmp >= len(data): return False
                    tmp1 = str(bin(data[i + tmp]))[2:]
                    if tmp1.find("10") == 0 and len(tmp1) == 8:
                        tmp -= 1
                    else:
                        return False
                i += len(binNum.split("0")[0])
        return True


sol = Solution()
print(sol.validUtf8([145]))