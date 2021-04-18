import copy
import random

def isolated_vertices(adj_matrix):

    result = []

    for v in range(len(adj_matrix)):
        if 1 not in adj_matrix[v]:
            result.append(v)

    return result

def pendant_vertices(adj_matrix):

    result = []

    for v in range(len(adj_matrix)):

        if adj_matrix[v].count(1) == 1:
            result.append(v)

    return result

def tops_vertices(adj_matrix,num_edges_needed):

    result = []

    for v in range(len(adj_matrix)):

        num_edges_in_vertex = adj_matrix[v].count(1)

        if num_edges_in_vertex > num_edges_needed:
            result.append(v)

    return result

def make_pendant_vertex(adj_matrix):

    all_tops_vertices = tops_vertices(adj_matrix,1)

    if len(all_tops_vertices) == 0:
        return adj_matrix

    vertex = all_tops_vertices[random.randint(0,len(all_tops_vertices)-1)]

    local_matrix =  copy.deepcopy(adj_matrix)  

    num_edges = adj_matrix[vertex].count(1)
    
    for i in range(len(local_matrix[vertex])):
        if local_matrix[vertex][i] == 1:
            local_matrix[vertex][i] = 0
            local_matrix[i][vertex] = 0
            num_edges -=1
        if num_edges == 1:
            break

    return local_matrix
    
def make_tops_vetrex(adj_matrix,k):

    random.seed()
    all_tops_vertices = tops_vertices(adj_matrix,k)

    if len(all_tops_vertices) == len(adj_matrix) or k > (len(adj_matrix) - 1):
        return adj_matrix

    vertex = random.randint(0,len(adj_matrix)-1)

    while vertex in all_tops_vertices:
        vertex = random.randint(0,len(adj_matrix)-1)

    local_matrix =  copy.deepcopy(adj_matrix) 
    num_edges = k - local_matrix[vertex].count(1) + 1

    while num_edges > 0:
        new_edge = random.randint(0,len(adj_matrix)-1)

        if local_matrix[vertex][new_edge] == 0 and vertex != new_edge:
            local_matrix[vertex][new_edge] = 1
            local_matrix[new_edge][vertex] = 1
            num_edges -=1

    return local_matrix

