# 算法1:  给你一个数据集类似这样：

# [
# #start, end, bandwidth
# [100, 200, 14],
# [110, 120, 15],
# [120, 189, 11],
# [200, 220, 9],
# [210, 218, 8],
# [216, 220, 7]
# ]
#
#
#
# start , end 节目的开始结束时间， bandwidth是用户购买的带宽， 问用户最多需要买多少带宽。 如上面的数据，结果为29

input = [
#start, end, bandwidth
[100, 200, 14],
[110, 120, 15],
[120, 189, 11],
[200, 220, 9],
[210, 218, 8],
[216, 220, 7]
]

def minBandWidth(input):
    st = []
    for i in input:
        st.append((i[0], i[2]))
        st.append((i[1], -i[2]))
    st.sort()
    res = 0
    cur = 0
    for i in st:
        cur += i[1]
        res = max(cur, res)
    print(res)
    return res

minBandWidth(input)
