from dwave.system import DWaveSampler, EmbeddingComposite
from dimod import BinaryQuadraticModel

N = [0,1,2]


#Variables 
x = [[f'A_{num}', f'B_{num}'] for num in N]

print(x)

#bqm = BinaryQuadraticModel('BINARY')

qubo = {(0, 0): 0, (1, 1): 0, (0, 1): 0.5, (2, 2): 0,
        (0, 2): 0.5, (1, 2): 0.5}
bqm = BinaryQuadraticModel.from_qubo(qubo)

print(bqm)
#change