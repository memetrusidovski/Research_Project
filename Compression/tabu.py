from typing import List, Dict
# a:List[int] =  [1, 1, 1, -1, -1, -1, -1, 1,
#                      1, -1, -1, 1, -1, 1, -1] 

# b:List[int] =  [1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1]
# a =  [-1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1] 
# b =  [-1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1]

# a =  [-1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1] 
# b =  [-1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1]
a =[-1, -1,-1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, -1, 1]
b=[-1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1]

n: int = len(a)
global found 
s_count = int((n-1)/2) 
global bit
bit = 0

besta = []
bestb = []


def check(a_temp: List[int], b_temp: List[int], aa, bb):
    lst = []
    lst2 = []
    global bit 
    bit = 1
    twos = 0

    for j in range(1, int((n-1)/2) + 1 ):
        a_paf = 0
        b_paf = 0

        for i in range(n):
            a_paf += a_temp[i] * a_temp[(i+j) % n]

        for i in range(n):
            b_paf += b_temp[i] * b_temp[(i+j) % n]

        lst2.append(f"{a_paf} + {b_paf} = {a_paf+b_paf}")
        lst.append(a_paf+b_paf)
        if lst[-1] != 2:
            bit = 0

    twos = lst.count(2)
    if bit:
        print(lst, " ", twos, " ", bit)
        aa = a_temp
        bb = b_temp

    print(a_temp, " ", b_temp, " ", twos)

    return aa, bb


check(a,b,besta,bestb)
q = 0
w = 0
a.extend(b)

for i in a:
    if int(i) == 1:
        q += 1
    else:
        w += 1
print("1: ", q, "  -1: ", w)

# for j in range(n):
#     a[j] *= -1
#     for k in range(1, n):
#         a[(j + k)%n] *= -1

#         for i in range(2, n):
#             a[(i + j)%n] *= -1
            
#             besta,bestb = check(a,b,besta,bestb)
            
            
#             a[(i + j)%n] *= -1
        
#         a[(j + k)%n] *= -1
#     a[j] *= -1

# print(besta, bestb)

'''
def tab():
    sBest ← s0
    bestCandidate ← s0
    tabuList ← []
    tabuList.push(s0)
    while (not stoppingCondition())
        sNeighborhood ← getNeighbors(bestCandidate)
        bestCandidate ← sNeighborhood[0]
        for (sCandidate in sNeighborhood)
            if ( (not tabuList.contains(sCandidate)) and (fitness(sCandidate) > fitness(bestCandidate)) )
                bestCandidate ← sCandidate
            end
        end
        if (fitness(bestCandidate) > fitness(sBest))
            sBest ← bestCandidate
        end
        tabuList.push(bestCandidate)
        if (tabuList.size > maxTabuSize)
            tabuList.removeFirst()
        end
    end
    return sBest
'''