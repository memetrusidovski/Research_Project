aa = {'a_0_0': 1.0, 'a_0_1': 1.0, 'a_0_10': 1.0, 'a_0_11': 1.0, 'a_0_12': -1.0, 'a_0_13': -1.0, 'a_0_14': -1.0, 'a_0_15': -1.0, 'a_0_16': -1.0, 'a_0_17': 1.0, 'a_0_18': -1.0, 'a_0_19': -1.0, 'a_0_2': -1.0, 'a_0_20': -1.0, 'a_0_21': -1.0, 'a_0_22': -1.0, 'a_0_23': 1.0, 'a_0_24': 1.0, 'a_0_25': -1.0, 'a_0_26': 1.0, 'a_0_3': -1.0, 'a_0_4': 1.0, 'a_0_5': 1.0, 'a_0_6': -1.0, 'a_0_7': -1.0, 'a_0_8': 1.0, 'a_0_9': 1.0, 'a_1_0': 1.0}
bb = {'b_0_0': 1.0, 'b_0_1': 1.0, 'b_0_10': -1.0, 'b_0_11': -1.0, 'b_0_12': 1.0, 'b_0_13': -1.0, 'b_0_14': 1.0, 'b_0_15': -1.0, 'b_0_16': -1.0, 'b_0_17': -1.0, 'b_0_18': -1.0, 'b_0_19': -1.0, 'b_0_2': -1.0, 'b_0_20': -1.0, 'b_0_21': 1.0, 'b_0_22': -1.0, 'b_0_23': 1.0, 'b_0_24': -1.0, 'b_0_25': 1.0, 'b_0_26': -1.0, 'b_0_3': -1.0, 'b_0_4': -1.0, 'b_0_5': -1.0, 'b_0_6': 1.0, 'b_0_7': -1.0, 'b_0_8': -1.0, 'b_0_9': 1.0}

n = len(aa)
d = {}
for key, value in aa.items():
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