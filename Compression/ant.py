import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from typing import List, Dict
from copy import deepcopy

a =  [-1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1] 
b =  [-1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1]

# a =  [1, 1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1] 
# b =  [-1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1]

# a =  [-1, -1, -1, -1, -1, -1, -1,-1, 1, 1, -1, -1, 1, -1,  1] 
# b =  [-1,  1,  1,  1,  1, -1, 1 ,-1, 1, 1,  1, -1, -1, 1, -1]

n: int = len(a)
N: int = 2 * n 
w_i = np.ones(n*4)

def check(a_temp: List[int], b_temp: List[int]):
    lst = []
    lst2 = []
    cor = 0

    for j in range(1, int((n-1)/2) + 1 ):
        a_paf = 0
        b_paf = 0

        for i in range(n):
            a_paf += a_temp[i] * a_temp[(i+j) % n]

        for i in range(n):
            b_paf += b_temp[i] * b_temp[(i+j) % n]

        lst2.append(f"{a_paf} + {b_paf} = {a_paf+b_paf}")
        lst.append(a_paf+b_paf)
        if a_paf+b_paf == 2:
            cor += 1

    # print(lst)
    if cor*2 == n -1:
        print("a = ", a_temp, "\nb = ", b_temp, "\n", cor)

    return cor

def distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2)**2))

def ones(t1, t2):
    q = 0
    w = 0

    for i in t1:
        if int(i) == 1:
            q += 1
        else:
            w += 1  
    print("1: ", q, "  -1: ", w)
    q = 0
    w = 0
    for i in t2:
        if int(i) == 1:
            q += 1
        else:
            w += 1
    print("1: ", q, "  -1: ", w)

def ant_colony_optimization(n_ants, n_iterations, alpha, beta, evaporation_rate, Q):
    # n_points = len(points)
    # pheromone = np.ones((n_points, n_points))
    w_i = np.ones(n*4)
    best_list = []
    best_solution = 0
    walks = 20
    current_point = np.random.randint(0, N)

    print(w_i, "\n ->", n)
    for iteration in range(n_iterations):
        path_lengths = 0
        
        for ant in range(n_ants):
            # visited = [False]*n_points
            a_temp = deepcopy(a)
            b_temp = deepcopy(b)
            c_temp = a_temp + b_temp

            # current_point = np.random.randint(n_points)
            # visited[current_point] = True
            # path = [current_point]
            # path_length = 0
            
            # while False in visited:
            for w in range(walks):
                # unvisited = np.where(np.logical_not(visited))[0]
                probabilities = np.zeros(N)
                total_check = check(a_temp, b_temp)

                if total_check > 0:
                    for i, unvisited_nodes in enumerate(c_temp):
                        if unvisited_nodes == 1:
                            probabilities[i] = (w_i[current_point]**alpha) * ( ( total_check **beta))
                        else:
                            probabilities[i] = (w_i[current_point+n]**alpha) * ( ( total_check **beta))
                    
                    probabilities /= np.sum(probabilities)
                    
                    pick = range(0,N)
                    next_point = np.random.choice(pick, p=probabilities)
                    if c_temp[next_point] == 1:
                        w_i[ next_point ] += Q/total_check
                        
                    else:
                        w_i[ next_point + N ] += Q/total_check
                else:
                    pick = range(0,N)
                    next_point = np.random.choice(pick)

                
                # path.append(next_point)

                # maintain feasiblity 
                flag = True
                while flag:
                    if next_point < n: 
                        pick = range(0,n)
                        npoint = np.random.choice(pick)
                        if a_temp[next_point] != a_temp[npoint]:
                            flag = False 
                            a_temp[npoint] *= -1
                    else:
                        pick = range(n,N)
                        npoint = np.random.choice(pick)
                        npoint -= n
                        if b_temp[next_point-n] != b_temp[npoint]:
                            flag = False 
                            b_temp[npoint] *= -1


                # path_length += distance(points[current_point], points[next_point])
                # visited[next_point] = True
                current_point = next_point
                c_temp[next_point] *= -1
                if next_point < n:
                    a_temp[next_point] *= -1
                else:
                    b_temp[next_point - n] *= -1
                
                

            # paths.append(path)
            # path_lengths.append(path_length)
            
            # if path_length < best_path_length:
            #     best_path = path
            #     best_path_length = path_length
        
        w_i *= 1 - evaporation_rate
    print(w_i, "\n ->", ones(a_temp, b_temp))
        
        # for path, path_length in zip(paths, path_lengths):
        #     for i in range(n_points-1):
        #         pheromone[path[i], path[i+1]] += Q/path_length
        #     pheromone[path[-1], path[0]] += Q/path_length
    
    # fig = plt.figure(figsize=(8, 6))
    # ax = fig.add_subplot(111, projection='3d')
    # ax.scatter(points[:,0], points[:,1], points[:,2], c='r', marker='o')
    
    # for i in range(n_points-1):
    #     ax.plot([points[best_path[i],0], points[best_path[i+1],0]],
    #             [points[best_path[i],1], points[best_path[i+1],1]],
    #             [points[best_path[i],2], points[best_path[i+1],2]],
    #             c='g', linestyle='-', linewidth=2, marker='o')
        
    # ax.plot([points[best_path[0],0], points[best_path[-1],0]],
    #         [points[best_path[0],1], points[best_path[-1],1]],
    #         [points[best_path[0],2], points[best_path[-1],2]],
    #         c='g', linestyle='-', linewidth=2, marker='o')
    

    
# Example usage:
# points = np.random.rand(10, 3) # Generate 10 random 3D points

# ant_colony_optimization(n_ants=10, n_iterations=50, alpha=1, beta=1, evaporation_rate=0.9, Q=1)
# ant_colony_optimization(n_ants=10, n_iterations=100, alpha=1.01, beta=1.01, evaporation_rate=0.05, Q=1)
# ant_colony_optimization(n_ants=10, n_iterations=50, alpha=0.1, beta=0.1, evaporation_rate=0.2, Q=1)
ant_colony_optimization(n_ants=60, n_iterations=500, alpha=1.6, beta=1.6, evaporation_rate=0.05, Q=1)


print(check(a,b))