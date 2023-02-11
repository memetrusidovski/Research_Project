from dwave.system import DWaveSampler, EmbeddingComposite
from dimod import ConstrainedQuadraticModel
import dimod
from dwave.system import LeapHybridCQMSampler


n = 5
s = list(range(1, int((n-1)/2)))
alpha = (3, 3)

#s = [1]

x = [[dimod.Spin(f'a_0_{j}') for j in range(n)] ]
x2 = [[dimod.Spin(f'b_0_{j}') for j in range(n)] ]


cqm = dimod.ConstrainedQuadraticModel()

cqm.add_constraint(sum(x[0]) == -alpha[0], label=f'item_placing_0')
cqm.add_constraint(sum(x2[0]) == -alpha[1], label=f'item_placing_1')

'''
for j in s:
    cqm.add_constraint( 
        sum( (x[0][i] * x[0][ (i+j) % n ]) for i in range( n ) ) +
        sum( (x2[0][i] * x2[0][ (i+j) % n ]) for i in range( n ) ) == 2,
        label=f'capacity_bin_{j}1')
'''

print(cqm, "----------------------------")


import neal

from dwave.preprocessing.presolve import Presolver
presolve = Presolver(cqm)
presolve.load_default_presolvers()
presolve.apply()

bqm, invert = dimod.cqm_to_bqm(presolve.copy_model())

print(bqm)
print("----------------------------")
print(presolve.copy_model())

'''
sampler = neal.SimulatedAnnealingSampler()
sampleset = sampler.sample(bqm)             
print(sampleset.first, "\n", "="*30) 
'''
'''
sampler = LeapHybridCQMSampler()  
sampleset = sampler.sample_cqm(cqm)             
print(sampleset.first, "\n", "="*30)  

feasible_sampleset = sampleset.filter(lambda d: d.is_feasible)
print(feasible_sampleset)
'''

'''
for i in sampleset.samples():
    print(i)

sampleset = dimod.ExactSolver().sample(bqm)
print(sampleset.first) '''