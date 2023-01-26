from dwave.system import DWaveSampler, EmbeddingComposite
from dimod import ConstrainedQuadraticModel
import dimod
from dwave.system import LeapHybridCQMSampler

s = [1,2,3,4,5,6,7,8,9,10,11,12,13]
n = 27

paf = [
    (3, -1),
    (-5, 7),
    (-1, 3),
    (-5, 7),
    (3, -1),
    (3, -1),
    (-5, 7),
    (-1, 3),
    (3, -1),
    (-1, 3),
    (-1, 3),
    (3, -1),
    (3, -1)]

#y = [dimod.Spin(f'y_0'), dimod.Spin(f'y_1'), dimod.Spin(f'y_2')]

x = [[dimod.Spin(f'a_0_{j}') for j in range(n)] ]
x2 = [[dimod.Spin(f'b_0_{j}') for j in range(n)] ]
     #for i in range(len(weights))]

cqm = dimod.ConstrainedQuadraticModel()

# cqm.set_objective(sum(y))


cqm.add_constraint(sum(x[0]) == 5, label=f'item_placing_0')
cqm.add_constraint(sum(x2[0]) == -9, label=f'item_placing_1')

for j, t in zip(s, paf):
    cqm.add_constraint(
        sum( (x[0][i] * x[0][ (i+j) % n ]) for i in range( n ) ) == t[0],
        label=f'capacity_bin_{j}{t[0]}')
    cqm.add_constraint(
        sum( (x2[0][i] * x2[0][ (i+j) % n ]) for i in range( n ) ) == t[1],
        label=f'capacity_bin_{j}{t[1]}1')

'''
cqm.add_constraint(
        x[0][0] * x[0][1] + x[0][1] * x[0][2] + x[0][2] * x[0][0]  == -1,
        label=f'capacity_bin_0')
'''

print(cqm, "----------------------------")


sampler = LeapHybridCQMSampler()                
sampleset = sampler.sample_cqm(cqm)             
print(sampleset.first)  




'''
sampler = LeapHybridCQMSampler()
raw_sampleset = sampler.sample_cqm(cqm)
feasible_sampleset = raw_sampleset.filter(lambda d: d.is_feasible)
num_feasible = len(feasible_sampleset)
if num_feasible > 0:
    best_samples =  feasible_sampleset.truncate(min(10, num_feasible))

best_samples = raw_sampleset.truncate(10)

print(" \n" + "=" * 30 + "BEST SAMPLE SET" + "=" * 30)
print(best_samples)

best_sample = best_samples.first.sample

print(best_samples)'''