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


bqm.add_linear_equality_constraint( [ ('a_0', 1), ('a_1', 1), ('a_2', 1) ], 10, -1)

sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample(bqm, num_reads=10)

sample = sampleset.first.sample

print(sample)


"""
# example for n = 7 *works
bqm.add_linear_equality_constraint( [ ('a_0', 1), ('a_1', 1), ('a_2', 1),
                                        ('a_3', 1), ('a_4', 1), ('a_5', 1), ('a_6', 1) ], 10, -5)


"""