#a = [-1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1]
#b[1,-1,1,1,1]
# working ->a[-1, 1,1,1, 1,  -1,1, 1,  -1,  1,  -1,  -1,  1,  1, 1,  1, 1,  -1,  -1,  1, 1,  1,  -1, -1,  -1,  1, -1]
#[ -1, 1, -1, 1,  1, -1,  1, -1, 1,  1,  1,  1, 1,  1, -1,  1, 1,  1,  -1,  1, 1,  1, -1,  -1,  -1,  -1,  -1]
#[-1,1,1,1,-1,1,-1]#[1,-1,1,1,1,1,1]#[-1, 1,1,1,1] #[1,-1,1,1,1]
#b = [-1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1]
#b[1,1,1,1,-1]
# working ->a[-1,  -1,  -1,  -1,  1, -1,  1,  -1,  1,  -1,  -1,  1,  -1,  -1, 1, 1,  1,  -1,  1,  -1, -1,  -1,  1,  -1,  -1,  -1,  -1]
#[1,  -1,  1,   1,  -1,  -1,  -1,  -1,  1,  -1,1,  -1,  -1, -1, -1,  -1,  -1,  -1,  -1,  1,  1,  -1,  1,  -1,  1, -1,  -1]
#[1,1,1,1,1,1,-1]#[1,1,-1,1,-1,-1,1]#[1,1,1,-1,1] #[1,1,-1,1,1]
#a = [-1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, -1]
#b = [-1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1]

a =  [-1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1]
b = [-1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1]

lst = []
n = len(a)
for j in range(1, int((n-1)/2) + 1 ):
    print("S of ", j)
    print("="*30)
    a_s = 0
    b_s = 0

    a_paf = 0
    b_paf = 0

    for i in a:
        a_s += i

    for i in b:
        b_s += i

    for i in range(n):
        a_paf += a[i] * a[(i+j) % n]

    for i in range(n):
        b_paf += b[i] * b[(i+j) % n]


    print("sum of a: ", a_s)
    print("sum of b: ", b_s)
    print("-"*30)

    print("sum of P(a): ", a_paf)
    print("sum of P(b): ", b_paf)

    print("P(a) + P(b) = ", a_paf+ b_paf)
    print("\n\n")
    lst.append(a_paf+b_paf)

print(lst)

