class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        llog = []
        dlog = []
        for log in logs:
            if log[log.index(" ") + 1].isdigit():
                dlog.append(log)
            else:
                llog.append(log)
        if not llog: return dlog
        llog.sort(key=lambda x: x[1])
        tmp = []
        for log in llog:
            tmp.append(" ".join(log.split(" ")[1:]))
            # sorted(student_tuples, key=lambda student: student[2])
        llog = list(list(zip(*(sorted(list(zip(llog, tmp)), key=lambda t: t[1]))))[0])
        return llog + dlog
sol = Solution()
sol.reorderLogFiles(["j mo", "5 m w", "g 07", "o 2 0", "t q h"])