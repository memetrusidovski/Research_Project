
from dwave.system import DWaveSampler, EmbeddingComposite
from dimod import ConstrainedQuadraticModel
import dimod
from dwave.system import LeapHybridCQMSampler
import colorama
from colorama import Fore, Style


working = []
def clean(qq):
    aa ={}
    bb ={}
    n = 15
    count = 0
    con = 1

    for key, value in qq.items():
        if count == 0:
            print(f"Now {con} is, ")
        if count < n * 2:
            print("(", int(value), ") + ", end='')
            count += 1 
            if count == n * 2:
                print(" = 2\n")
                con += 1
                count = 0

        # if 'a' in key:
        #     aa[int(key[4:])] = int(value)
        # else:
        #     bb[int(key[4:])] = int(value)
        
        #print(aa[int(key[4:])])
    #print(aa)

#     n = len(aa)
#     da = {}
#     for key, value in aa.items():
#         da[key] = value

#     sorted_dict_a = {key: value for key, value in sorted(da.items())}
    
#     db = {}
#     for key, value in bb.items():
#         db[key] = value


#     sorted_dict_b = {key: value for key, value in sorted(db.items())}


#     a = []
#     b = []
#     ct = 0

#     for i in range(n):
#         a.append(int(sorted_dict_a[i]))
#     for i in range(n):
#         b.append(int(sorted_dict_b[i]))
    
#     print("a = ", a, "\nb = ", b)

#     lst = []
#     n = len(a)
#     for j in range(1, int((n-1)/2) + 1 ):
# #for j in [1]:
#     # print("S of ", j)
#     # print("="*30)
#         a_s = 0
#         b_s = 0

#         a_paf = 0
#         b_paf = 0

#         for i in a:
#             a_s += i

#         for i in b:
#             b_s += i

#         for i in range(n):
#             a_paf += a[i] * a[(i+j) % n]

#         for i in range(n):
#             b_paf += b[i] * b[(i+j) % n]

#         lst.append(a_paf+b_paf)

#     print("[", end="")
#     for t in lst:
#         if t == 2:
#             ct += 1 
#             print(f"{Fore.CYAN}{t}", " ", end="")
#         else:
#             print(f"{Fore.GREEN}{t}", " ", end="")

#     if ct == int((n-1)/2):
#         print(f"{Fore.WHITE}] {ct}<-----------\n")
#     else:
#         print(f"{Fore.GREEN}] {ct}\n")


n = 15
# s = [1,2,3,4,5] #
s = list(range(1, int((n-1)/2)))
# s = [15,16,17,18,19,20]
# s = [1,2,3,4,5,6,7,8,9,10]
alpha = (3, 7)

x = [[dimod.Spin(f'a_{i}_{j}') for j in range(n)] for i in s]
x2 = [[dimod.Spin(f'b_{i}_{j}') for j in range(n)]  for i in s]

y = [dimod.Spin(f'a_1_{j}') for j in range(n)] 
y2 = [dimod.Spin(f'b_1_{j}') for j in range(n)]

cqm = dimod.ConstrainedQuadraticModel()

# cqm.add_constraint(sum(x[0]) == -alpha[0], label=f'Linear_0')
# cqm.add_constraint(sum(x2[0]) == -alpha[1], label=f'Linear_1')


# cqm.set_objective( sum( (x[0][i] * x[0][ (i) % n ]) for i in range( n ) )  + sum( (x2[0][i] * x2[0][ (i) % n ]) for i in range( n ) ))


for j in s:
    cqm.add_constraint( 
        sum( x [j-1]) + sum( x2 [j-1]) == 2,
        copy=True,
        # penalty='quadratic',
        # weight=0.1,
        label=f'capacity_bin_{j}1')

    # for i in range(n):
    #     cqm.add_constraint( 
    #         x [j] [i] == y[i] * y[ (i+j) % n ],
    #         copy=True, 
    #         penalty='quadratic',
    #         weight=0.1,
    #         label=f'con_{j}_{i}_a')

    # for i in range(n):
    #     cqm.add_constraint( 
    #         x [j] [i] == y2[i] * y2[ (i+j) % n ],
    #         copy=True, 
    #         penalty='quadratic',
    #         weight=0.1,
    #         label=f'con_{j}_{i}_b')
print(cqm, "----------------------------")

sampler = LeapHybridCQMSampler()  
sampleset = sampler.sample_cqm(cqm, time_limit=5)    
first = sampleset.first         
print(first, "\n", "="*30)

feasible_sampleset = sampleset.filter(lambda d: d.is_feasible)
num_feasible = len(feasible_sampleset)

print(f"{Fore.CYAN}Runtime is{feasible_sampleset.info}")
print(f"{Fore.YELLOW}there are {num_feasible} solutions found, the are\n", feasible_sampleset)
print(f"{Fore.RED}there are {5} solutions found, the are\n", feasible_sampleset.first)
print(f"{Fore.GREEN} solutions found, \n")#, feasible_sampleset.first.sample)

clean(feasible_sampleset.first.sample)

# for feasibles in feasible_sampleset:
#     #print(x, "\n\n")
#     clean(feasibles)
#     print("\n\n")