from dwave.system import DWaveSampler, EmbeddingComposite
from dimod import ConstrainedQuadraticModel
import dimod
from dwave.system import LeapHybridCQMSampler


n = 43
s = list(range(1, int((n-1)/2)))
alpha = (7, 11)

x = [[dimod.Binary(f'a_0_{j}') for j in range(n)] ]
x2 = [[dimod.Binary(f'b_0_{j}') for j in range(n)] ]


cqm = dimod.ConstrainedQuadraticModel()



cqm.add_constraint(sum(x[0]) == -alpha[0], label=f'item_placing_0')
cqm.add_constraint(sum(x2[0]) == -alpha[1], label=f'item_placing_1')

for j in s:
    cqm.add_constraint(
        sum( (x[0][i] * x[0][ (i+j) % n ]) for i in range( n ) ) +
        sum( (x2[0][i] * x2[0][ (i+j) % n ]) for i in range( n ) ) == 2,
        label=f'capacity_bin_{j}1')


print(cqm, "----------------------------")


'''
from dwave.preprocessing.presolve import Presolver
presolve = Presolver(cqm)
presolve.load_default_presolvers()
presolve.apply()
'''
'''
sampler = LeapHybridCQMSampler()  
sampleset = sampler.sample_cqm(cqm, min_time_limit = 10    )             
print(sampleset.first)  

'''
'''
bqm, invert = dimod.cqm_to_bqm(cqm)
sampleset = dimod.ExactSolver().sample(bqm)
print(sampleset.first) '''