from dwave.system import DWaveSampler, EmbeddingComposite
from dimod import BinaryQuadraticModel

N = [0,1,2]


#Variables 
x = [[f'A_{num}', f'B_{num}'] for num in N]

print(x)
#bqm = BinaryQuadraticModel('BINARY')

