# tạo một dict trống

from operator import itemgetter, attrgetter
Dict = {}
print(Dict)
# return {}

# tạo một dict với key là các số nguyên
Dict = {1:0, 2:3, 3:2}
Dict[0] = 5
Dict[4] = 4
print(Dict)
s = []
for i in sorted(Dict, key=Dict.get, reverse=True):
    s.append((i, Dict[i]))
print("3 so nguyen lon nhat trong tu dien",s[0],s[1],s[2])