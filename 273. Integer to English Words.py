class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
             9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
             16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty",
             50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
        if num == 0:
            return "Zero"

        def word(num):
            if num < 20:
                if num == 0:
                    return []
                return [d[num]]
            if num < 100:
                return [d[num - num % 10]] + word(num % 10)
            if num < 1000:
                return [d[int(num / 100)], "Hundred"] + word(num % 100)
            if num < 1000000:
                return word(int(num / 1000)) + ["Thousand"] + word(num % 1000)
            if num < 1000000000:
                return word(int(num / 1000000)) + ["Million"] + word(num % 1000000)
            if num <= 2 ** 31 - 1:
                return word(int(num / 1000000000)) + ["Billion"] + word(num % 1000000000)
            else: return "Out of number range!!!"

        return " ".join(word(num))


sol = Solution()
print(sol.numberToWords(100))