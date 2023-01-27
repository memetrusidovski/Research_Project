from dwave.system import DWaveSampler, EmbeddingComposite
from dimod import BinaryQuadraticModel

s = 1
n = 3

paf = [(3, 1)]

a_n = [f'a_{i}' for i in range(n)]

print(a_n)
bqm = BinaryQuadraticModel('SPIN')

BinaryQuadraticModel.to_ising(bqm)

for i in a_n:
    bqm.add_variable(i)


# constraint two P_k
#bqm.add_quadratic('a_0', 'a_1', 0)
#bqm.add_quadratic('a_1', 'a_2', 0)
#bqm.add_quadratic('a_2', 'a_0', 0)


#bqm.add_linear_equality_constraint( [ ('a_0', 1), ('a_1', 1), ('a_2', 1) ], 0.5, -1)

qubo = {(0, 0): 0, (1, 1): 0, (0, 1): 0.5, (2, 2): 0,
        (0, 2): 0.5, (1, 2): 0.5}
bqm = BinaryQuadraticModel.from_qubo(qubo)

BinaryQuadraticModel.to_ising(bqm)

sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample(bqm, num_reads=10)

sample = sampleset.first.sample

print(sample)
print(bqm)


dwave.inspector.show(sampleset)