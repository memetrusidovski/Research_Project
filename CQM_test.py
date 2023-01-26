from dwave.system import DWaveSampler, EmbeddingComposite
from dimod import ConstrainedQuadraticModel
import dimod

s = 1
n = 3

paf = [(3, 1)]

weights = [1, 1, 1]
capacity = 1

y = [dimod.Spin(f'y_0'), dimod.Spin(f'y_1'), dimod.Spin(f'y_2')]

x = [[dimod.Spin(f'x_{i}_{j}') for j in range(len(weights))]
     for i in range(len(weights))]

cqm = dimod.ConstrainedQuadraticModel()

cqm.set_objective(sum(y))

for i in range(1):
    cqm.add_constraint(sum(x[i]) == 1, label=f'item_placing_{i}')

for j in range(1):
    cqm.add_constraint(
        sum( (x[i][j] * x[i][j+1]) for i in range(len(weights))) == -1,
        label=f'capacity_bin_{j}')

print(cqm, "----------------------------")


sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample(cqm, num_reads=10)

sample = sampleset.first.sample

print(sample)
print(cqm)
