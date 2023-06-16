f = open("test.txt", "r")

a = 0
b = 0

for x in f:
        y = x.split(' ')[1:-1]
        for i in y:
                if int(i) == 1:
                        a += 1
                else:
                        b += 1
        print("1: ", a, "  -1: ", b)
        a = 0
        b =0