from dwave.system import DWaveSampler, EmbeddingComposite
from dimod import ConstrainedQuadraticModel
import dimod
from dwave.system import LeapHybridCQMSampler

"""
This is a prototype for getting around the limitations of connectivity
"""

n = 7
s = list(range(1, int((n-1)/2)))
alpha = (1, 5)

s = [1,2,3]

x_0 = [dimod.Spin(f'a_0_{j}') for j in range(n)] 
x_1 = [dimod.Spin(f'a_1_{j}') for j in range(n)] 
x_2 = [dimod.Spin(f'a_2_{j}') for j in range(n)] 
x2_0 = [dimod.Spin(f'b_0_{j}') for j in range(n)] 
x2_1 = [dimod.Spin(f'b_1_{j}') for j in range(n)] 
x2_2 = [dimod.Spin(f'b_2_{j}') for j in range(n)] 


cqm = dimod.ConstrainedQuadraticModel()

cqm.add_constraint(sum(x_0 ) == -alpha[0], label=f'item_placing_0')
cqm.add_constraint(sum(x2_0 ) == -alpha[1], label=f'item_placing_1')

for i in range(n):   
    cqm.add_constraint(x_0[i] - x_1[i] == 0)

for i in range(n):   
    cqm.add_constraint(x_0[i] - x_2[i] == 0)

for i in range(n):   
    cqm.add_constraint(x2_0[i] - x2_1[i] == 0)

for i in range(n):   
    cqm.add_constraint(x2_0[i] - x2_2[i] == 0)


cqm.add_constraint( 
        sum( (x_0 [i] * x_0 [ (i+1) % n ]) for i in range( n ) ) +
        sum( (x2_0 [i] * x2_0 [ (i+1) % n ]) for i in range( n ) ) == 2,
        label=f'capacity_bin_{1}1')
cqm.add_constraint( 
        sum( (x_0 [i] * x_0 [ (i+2) % n ]) for i in range( n ) ) +
        sum( (x2_0 [i] * x2_0 [ (i+2) % n ]) for i in range( n ) ) == 2,
        label=f'capacity_bin_{2}1')
cqm.add_constraint( 
        sum( (x_0 [i] * x_0 [ (i+3) % n ]) for i in range( n ) ) +
        sum( (x2_0 [i] * x2_0 [ (i+3) % n ]) for i in range( n ) ) == 2,
        label=f'capacity_bin_{3}1')


print(cqm, "----------------------------")


'''
from dwave.preprocessing.presolve import Presolver
presolve = Presolver(cqm)
presolve.load_default_presolvers()
presolve.apply()

print(presolve.copy_model())
'''


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
print(sampleset.first) '''