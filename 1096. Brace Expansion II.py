
class Solution:
    def braceExpansionII(self, expression):
        st = []

        for c in expression:

            if c != "}":
                st.append([c])
                continue
            curExp = []
            while st and st[-1][0] != "{":
                curExp.append(st.pop())
            st.pop()
            tmp = self.calExp(curExp)
            st.append(tmp)
        res = self.calExp(st)
        return list(set(res))

    def calExp(self, curExp):
        st = []
        i = 0
        while i < len(curExp):
            if not st:
                st.append(curExp[i])
            else:
                if curExp[i][0] == ",":
                    i += 1
                    st.append(curExp[i])
                else:
                    st.append(self.getDot(st.pop(), curExp[i]))
            i += 1
        return st

    def getDot(self, list1, list2):
        res = []


        for a in list1:
            for b in list2:
                if type(a) != list:
                    a = [a]
                if type(b) != list:
                    b = [b]
                res.append(a + b)
        return res



sol = Solution()
sol.braceExpansionII("{a,b}{c{d,e}}")