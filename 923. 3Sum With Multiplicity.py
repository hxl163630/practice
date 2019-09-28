class Solution:
    def threeSumMulti(self, A, target: int) -> int:
        if not A or len(A) < 3:
            return 0
        from collections import Counter
        count = Counter(A)
        n = len(count)
        keys = sorted(count.keys())
        res = 0
        for i in range(n):
            t = target - keys[i]
            l = i
            r = n - 1

            while l <= r:
                tmp = keys[l] + keys[r]
                if tmp == t:
                    if keys[i] != keys[l] and keys[i] != keys[r] and keys[l] != keys[r]:
                        res += count[keys[i]] * count[keys[l]] * count[keys[r]]
                    elif keys[i] == keys[l] and keys[l] == keys[r]:
                        res += count[keys[i]] * (count[keys[i]] - 1) * (count[keys[i]] - 2) // 6
                    elif keys[i] == keys[l]:
                        res += count[keys[i]] * (count[keys[i]] - 1) // 2 * count[keys[r]]
                    elif keys[l] == keys[r] and count[keys[l]] >= 2:
                        res += count[keys[l]] * (count[keys[r]] - 1) // 2 * count[keys[i]]
                    l += 1
                    r -= 1
                elif tmp > t:
                    r -= 1
                else:
                    l += 1
        return res % (1000000007)