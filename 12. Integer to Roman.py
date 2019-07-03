class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        output = ""
        while num != 0:
            if num // 1000:
                num -= 1000
                output += "M"
                continue
            if num // 500:
                num -= 500
                output += "D"
                continue
            if num // 100:
                num -= 100
                output += "C"
                continue
            if num // 50:
                num -= 50
                output += "L"
                continue
            if num // 10:
                num -= 10
                output += "X"
                continue
            if num // 5:
                num -= 5
                output += "V"
                continue
            if num // 1:
                num -= 1
                output += "I"
                continue
        output = output.replace("IIII","IV")
        output = output.replace("VIV","IX")
        output = output.replace("XXXX","XL")
        output = output.replace("LXL","XC")
        output = output.replace("CCCC","CD")
        output = output.replace("DCD","CM")
        return output

sol = Solution()
sol.intToRoman(9)