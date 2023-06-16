
import colorama
from colorama import Fore, Style
from copy import deepcopy


# a =  [1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1] 
# b =  [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1]
# a =  [-1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1] 
# b =  [-1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1]
# a =  [-1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1] 
# b =  [1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, -1]
# a =  [1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1] 
# b =  [1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1]
a =  [1, -1, 1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, -1] 
b =  [1, 1, -1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1]

# a =  [-1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1] 
# b =  [1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1]

n = len(a)
global found
found = "NO"
s_count = int((n-1)/2) 
global bit 
bit = 0

def check(a_temp, b_temp):
    lst = []
    count = 0
    

    for j in range(1, int((n-1)/2) + 1 ):
        a_s = 0
        b_s = 0

        a_paf = 0
        b_paf = 0

        for i in a_temp:
            a_s += i

        for i in b_temp:
            b_s += i

        for i in range(n):
            a_paf += a_temp[i] * a_temp[(i+j) % n]

        for i in range(n):
            b_paf += b_temp[i] * b_temp[(i+j) % n]

        lst.append(a_paf+b_paf)

    print("[", end="")
    for t in lst:
        if t == 2:
            count += 1
            print(f"{Fore.CYAN}{t}", " ", end="")
        else:
            print(f"{Fore.GREEN}{t}", " ", end="")

    if  count == s_count:
        global found 
        found = "YES"
        global bit
        bit = 1

    print(f"{Fore.WHITE}] {count} \n")

check(a,b)
depth = 6

def DFS(a_tmp, b_tmp, d):
    if d == depth:
        return
    if bit == 1:
        return

    
    for i in range(0, int((n-1)/2)  ):
        tmp = deepcopy(a_tmp)
        tmp[i] *= -1
        # print(i, end="")
        check(tmp,b_tmp)
        DFS(tmp, b_tmp, d+1)
        

    for i in range(0, int((n-1)/2)  ):
        tmp = deepcopy(b)
        tmp[i] *= -1
        # print(i, end="")
        DFS(a_tmp, tmp, d+1)
        check(a,tmp)

    

# DFS(a,b,0)

print(found, s_count)

'''

a =  [-1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1] 
b =  [-1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1]

a2 =  [-1, -1, 1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, -1, -1] 
b2 =  [1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, 1]

def doto(k,l):
    c = 0
    for i in k:
        if i == 1:
            c+=1
    print(c, "<- a")
    c = 0
    for i in l:
        if i == 1:
            c+=1
    print(c, "<- b")
    
def doit(k,l):
    c = 0
    for i in k:
        a[c] -= i
        c+=1
    c = 0
    for i in l:
        b[c] -= i
        c+=1

doto(a,b)
doto(a2,b2)
doit(a2,b2)
print(a, "\n", b)
'''
'''

a =  [-1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1] 
b =  [1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1]
#[2  2  2  2  2  2  2  2  -2  2  2  -2  2  2  10  ] 12
x =  [1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1] 
z =  [-1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1]
#[2  -2  2  2  2  6  2  2  2  2  2  2  2  2  2  ] 13


a1 =  [1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, 1] 
a2 =  [-1, -1, -1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1]

a3 =  [1, -1, 1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, -1] 
a4 =  [-1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1]


a5 =  [-1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1] 
a6 =  [-1, 1, -1, -1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1]

a7 =  [1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1] 
a8 =  [-1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1]

a9 =  [1, 1, -1, 1, -1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1] 
a10 =  [1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1]


a11 =  [-1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1] 
a12 =  [-1, -1, -1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1]

a13 =  [1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1] 
a14 =  [-1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1]

a15 =  [-1, -1, 1, -1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1] 
a16 =  [-1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1]

ax =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
az =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



def doit(k,l):
    c = 0
    for i in k:
        if a[c] == i:
            ax[c] += 1
        c+=1
    c = 0
    for i in l:
        if b[c] == i:
            az[c] += 1
        c+=1

doit(a1,a2)
doit(a3,a4)
doit(a5,a6)
doit(a7,a8)
doit(a9,a10)
doit(a11,a12)
doit(a13,a14)
doit(a15,a16)

b[2] *= -1
b[3] *= -1

print(ax, "\n\n", az, "\n\n")
check(a,b)
'''