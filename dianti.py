#persons = [0, 2, 5 , 7 , 3 , 5 , 2 , 6, 2 , 6 , 3]
from collections import Counter

print(Counter([4,8,3,9,10,5]))

# persons = Counter([4,8,3,9,10,5]).values()
# tmp = [i * n for i, n in enumerate(persons)]
#
# print("using Average:")
# print(sum([i * n for i, n in enumerate(persons)]) / (sum(persons)))
#
# for cur in range(len(persons)):
#     print("staying level: " + str(cur))
#     print(sum([person * abs(i - cur) for i, person in enumerate(persons)]))
