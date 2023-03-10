"""
Saumya will use this file to create benchmarking data and use up 
QPU time on his leap account. This will be added to the poster 
by Saumya
"""
from dwave.system import DWaveSampler, EmbeddingComposite
from dimod import ConstrainedQuadraticModel
import dimod
from dwave.system import LeapHybridCQMSampler
import colorama
from colorama import Fore, Style

n = 7
s = list(range(1, int((n-1)/2)))
alpha = (1, 5)

x = [[dimod.Spin(f'a_0_{j}') for j in range(n)] ]
x2 = [[dimod.Spin(f'b_0_{j}') for j in range(n)] ]


cqm = dimod.ConstrainedQuadraticModel()

cqm.add_constraint(sum(x[0]) == -alpha[0], label=f'item_placing_0')
cqm.add_constraint(sum(x2[0]) == -alpha[1], label=f'item_placing_1')

for j in s:
    cqm.add_constraint( 
        sum( (x[0][i] * x[0][ (i+j) % n ]) for i in range( n ) ) +
        sum( (x2[0][i] * x2[0][ (i+j) % n ]) for i in range( n ) ) == 2,
        label=f'capacity_bin_{j}1')


print(cqm, "----------------------------")


sampler = LeapHybridCQMSampler()  
sampleset = sampler.sample_cqm(cqm)    
first = sampleset.first         
print(first, "\n", "="*30)

feasible_sampleset = sampleset.filter(lambda d: d.is_feasible)
num_feasible = len(feasible_sampleset)

print(f"{Fore.BLUE}Runtime is{feasible_sampleset.info}")
print(f"{Fore.YELLOW}there are {num_feasible} solutions found, the are\n", feasible_sampleset)
