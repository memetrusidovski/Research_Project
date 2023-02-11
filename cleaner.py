aa = {'a_0_0': 1.0, 'a_0_1': -1.0, 'a_0_2': 1.0, 'a_0_3': 1.0, 'a_0_4': -1.0, 'a_0_5': -1.0, 'a_0_6': -1.0}
bb = {'b_0_0': -1.0, 'b_0_1': -1.0, 'b_0_2': -1.0, 'b_0_3': -1.0, 'b_0_4': 1.0, 'b_0_5': -1.0, 'b_0_6': -1.0}

n = len(aa)
d = {}
for key, value in bb.items():
    d[int(key[4:])] = value
    #print(key, " ",  value)

s = list(range(1, 28))
print(s)

sorted_dict = {key: value for key, value in sorted(d.items())}
print(sorted_dict)

a = []
b = []

for i in range(n):
    a.append(int(sorted_dict[i]))

print(a)