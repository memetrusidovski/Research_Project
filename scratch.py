from dwave.system import DWaveSampler, EmbeddingComposite
sampler_auto = EmbeddingComposite(DWaveSampler())

# linear = {('a', 'a'): -1, ('b', 'b'): -1, ('c', 'c'): -1}
# quadratic = {('a', 'b'): 2, ('b', 'c'): 2, ('a', 'c'): 2}

linear = {('0', '0'): -4.0, ('1', '1'): -4.0,('2', '2'): -4.0, ('3', '3'): 4.0, ('4', '4'): 4.0, ('5', '5'): 4.0}
quadratic = {('1', '0'): 8.0, ('2', '0'): 8.0, ('2', '1'): 8.0, ('4', '3'): 8.0, ('5', '3'): 8.0, ('5', '4'): 8.0}
Q = {**linear, **quadratic}

sampleset = sampler_auto.sample_qubo(Q, num_reads=10)

print(sampleset.first, "\n", "="*30)
