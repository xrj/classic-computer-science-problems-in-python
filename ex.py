from collections import  namedtuple

MazeLoaction = namedtuple('MazeLoaction',['row', 'column'])

a = MazeLoaction(0,0)
b = MazeLoaction(0,0)
x = {a}
x.add(b)
print(a == b)
print(a is b)
print(a in x)
print(len(x))
