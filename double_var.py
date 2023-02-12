from dwave.system import DWaveSampler, EmbeddingComposite
from dimod import ConstrainedQuadraticModel
import dimod
from dwave.system import LeapHybridCQMSampler

"""
This is a prototype for getting around the limitations of connectivity
"""

n = 27
s = list(range(1, int((n-1)/2)+1))
alpha = (5, 9)

print(s[:-1])
#s = [1,2,3]

x_0 = [ [dimod.Spin(f'a_{i-1}_{j}') for j in range(n)] for i in s ]

x2_0 = [ [dimod.Spin(f'b_{i-1}_{j}') for j in range(n)] for i in s ]

#print(x_0)

cqm = dimod.ConstrainedQuadraticModel()

cqm.add_constraint(sum(x_0 [0]) == -alpha[0], label=f'item_placing_0')
cqm.add_constraint(sum(x2_0 [0]) == -alpha[1], label=f'item_placing_1')

#remove first to take away a comparison 
for j in s[:-1]:
    for i in range(n):   
        cqm.add_constraint(x_0[j-1] [i] - x_0[j] [i] == 0)
'''
for j in [ 7, 8, 9, 10, 11, 12]:
    for i in range(n):   
        cqm.add_constraint(x_0[6] [i] - x_0[j] [i] == 0)
'''


for j in s[:-1]:
    for i in range(n):   
        cqm.add_constraint(x2_0[j-1][i] - x2_0[j][i] == 0)
'''
for j in [7, 8, 9, 10, 11, 12]:
    for i in range(n):   
        cqm.add_constraint(x2_0[6][i] - x2_0[j][i] == 0)
'''

for j in s:
    cqm.add_constraint( 
        sum( (x_0[j-1] [i] * x_0[j-1] [ (i+j) % n ]) for i in range( n ) ) +
        sum( (x2_0[j-1] [i] * x2_0[j-1] [ (i+j) % n ]) for i in range( n ) ) == 2,
        label=f'capacity_bin_{j}1')


print(cqm, "----------------------------")




sampler = LeapHybridCQMSampler()  
sampleset = sampler.sample_cqm(cqm)             
print(sampleset.first, "\n", "="*30)  

feasible_sampleset = sampleset.filter(lambda d: d.is_feasible)
print(feasible_sampleset)



'''
for i in sampleset.samples():
    print(i)

bqm, invert = dimod.cqm_to_bqm(cqm)
sampleset = dimod.ExactSolver().sample(bqm)
print(sampleset.first) 

x_0 = []
for i in s:
    x_0.append( [dimod.Spin(f'a_0_{j}') for j in range(n)] )

x2_0 = []
for i in s:
    x2_0.append( [dimod.Spin(f'b_0_{j}') for j in range(n)] )

'''