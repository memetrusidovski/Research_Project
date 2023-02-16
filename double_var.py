from dwave.system import DWaveSampler, EmbeddingComposite
from dimod import ConstrainedQuadraticModel
import dimod
from dwave.system import LeapHybridCQMSampler

"""
This is a prototype for getting around the limitations of connectivity
"""

n = 85
s = list(range(1, int((n-1)/2)+1))
alpha = (7, 17)


#print(s[:-1])
#s = [1,2,3]

x_0 = [ [dimod.Spin(f'a_{i-1}_{j}' ) for j in range(n)] for i in s ]

x2_0 = [ [dimod.Spin(f'b_{i-1}_{j}' ) for j in range(n)] for i in s ]

print(len(x_0), " ", len(x_0[0]))

cqm = dimod.ConstrainedQuadraticModel()

'''
for j in s:
    cqm.add_constraint(sum(x_0 [j-1]) == -alpha[0], label=f'item_placing_0_{j}')
    cqm.add_constraint(sum(x2_0 [j-1]) == -alpha[1], label=f'item_placing_1_{j}')
'''


cqm.add_constraint(sum(x_0 [0]) == -alpha[0], label=f'item_placing_0')
cqm.add_constraint(sum(x2_0 [0]) == -alpha[1], label=f'item_placing_1')


#remove first to take away a comparison 
for j in s[:-1]:
    for i in range(n):   
        cqm.add_constraint(x_0[j-1] [i] - x_0[j] [i] == 0, label=f'entangle_a_{j}_{i}', copy=False, penalty = 'quadratic')
        #print(j, "<---", i)
        

for j in s[:-1]:
    for i in range(n):   
        cqm.add_constraint(x2_0[j-1][i] - x2_0[j][i] == 0, label=f'entangle_b_{j}_{i}', copy=False, penalty = 'quadratic')


for j in s:
    cqm.add_constraint( 
        sum( (x_0[j-1] [i] * x_0[j-1] [ (i+j) % n ]) for i in range( n ) ) +
        sum( (x2_0[j-1] [i] * x2_0[j-1] [ (i+j) % n ]) for i in range( n ) ) == 2,
        label=f'capacity_bin_{j}1')


#print(cqm, "----------------------------")

for j in s:
    print( cqm.constraints[f'capacity_bin_{j}1'].to_polystring(), "\n\n" )



sampler = LeapHybridCQMSampler()  
sampleset = sampler.sample_cqm(cqm)             
print(sampleset.first, "\n", "="*30)  

feasible_sampleset = sampleset.filter(lambda d: d.is_feasible)
print(feasible_sampleset)
print(feasible_sampleset.first)

'''

from dwave.preprocessing.presolve import Presolver
presolve = Presolver(cqm)
presolve.load_default_presolvers()
presolve.apply()

print(presolve.copy_model())
'''