# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter

a = "aaaaaaaadddddffffvvvvccccssseee"
myCounter = Counter(a)
print(myCounter)
print(myCounter.most_common(1)[0][0])

print(list(myCounter.elements()))
