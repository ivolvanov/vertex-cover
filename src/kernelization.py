import copy
import random

def independant_set(adj_matrix):

    local_matrix =  copy.deepcopy(adj_matrix)   

    result = []

    for v in range(len(adj_matrix)):
        if 1 in local_matrix[v]:
            continue
        else:
            result.append(v)

    return result

def pendant_vetices(adj_matrix):

    local_matrix =  copy.deepcopy(adj_matrix)  

    result = []

    for v in range(len(adj_matrix)):

        if 1 in adj_matrix[v]:
            local_matrix[v].remove(1)

            if 1 in local_matrix[v]:
                continue
            else:
                result.append(v)

            

    return result

def tops_vetices(adj_matrix,num_edges_needed):

    local_matrix =  copy.deepcopy(adj_matrix)  

    result = []

    for v in range(len(adj_matrix)):
        num_edges_in_vertex = 0

        for i in range(len(adj_matrix)):
            if adj_matrix[v][i] == 1:
                num_edges_in_vertex +=1

        if num_edges_in_vertex > num_edges_needed:
            result.append(v)

    return result


def make_pendant_vertex(adj_matrix,vetrex):

    local_matrix =  copy.deepcopy(adj_matrix)  

    num_edges = 0
    for i in range(len(local_matrix[vetrex])):
        if local_matrix[vetrex][i] == 1:
            num_edges +=1
        else:
            pass
    
    for i in range(len(local_matrix[vetrex])):
        if local_matrix[vetrex][i] == 1:
            local_matrix[vetrex][i] = 0
            num_edges -=1
        if num_edges == 1:
            break

    return local_matrix
    
            
def make_tops_vetrex(adj_matrix,vertex):

    local_matrix =  copy.deepcopy(adj_matrix) 

    num_edges = random.randrange(1,len(adj_matrix)-1)

    while num_edges > 0:

        new_edge = random.randint(0,len(adj_matrix)-1)

        if adj_matrix[vertex][new_edge] == 0:
            local_matrix[vertex][new_edge] = 1;
            num_edges -=1
        else:
            pass

    return local_matrix




graph = [[0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0], 
        [0, 1, 0, 1, 0], 
        [0, 1, 1, 1, 1], 
        [1, 0, 0, 1, 1]]

print(tops_vetices(graph,2))

