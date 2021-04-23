from itertools import combinations
import kernelization
import copy
import random

def __generate_all_covers__(items, cover_size):
    combos = []

    for assignment in list(combinations(items, cover_size)):
        combos.append(assignment)

    return combos


def __is_cover_valid__(adj_matrix_arg):
    for i in range(len(adj_matrix_arg)):
        for j in range(len(adj_matrix_arg)):
            if adj_matrix_arg[i][j] == 1:
                return False

    return True

def cover_check(adj_matrix, cover_size):
    if len(adj_matrix) == 0:
        return set()

    combo_items = []
    for i in adj_matrix:
        if 1 in i:
            combo_items.append(adj_matrix.index(i))
    
    combinations = __generate_all_covers__(combo_items, cover_size)

    for combo in combinations:        
        local_matrix = copy.deepcopy(adj_matrix)
        for i in combo:
            for j in range(len(local_matrix)):
                local_matrix[i][j] = 0
                local_matrix[j][i] = 0
        
        if __is_cover_valid__(local_matrix) == True:
            return combo

    return set()

def smart_cover(adj_matrix, k):

    isolated = set(kernelization.isolated_vertices(adj_matrix))
    pendant = set(kernelization.pendant_vertices(adj_matrix))
    tops = set(kernelization.tops_vertices(adj_matrix, k))

    if len(tops) > k:
        return set()

    not_in_cover = set()
    cover = set()

    cover.update(tops)
    not_in_cover.update(isolated)
    not_in_cover.update(pendant)

    pendant_neighbours = []
    for i in pendant:
        if i not in pendant_neighbours:
            if adj_matrix[i].index(1) not in pendant_neighbours:
                pendant_neighbours.append(adj_matrix[i].index(1))            

    cover.update(pendant_neighbours)
    not_in_cover.difference_update(cover)

    to_be_removed = []
    to_be_removed.extend(cover)
    to_be_removed.extend(not_in_cover)

    local_matrix = copy.deepcopy(adj_matrix)

    for i in to_be_removed:
            local_matrix[i] = [0]*len(adj_matrix)  
            for j in range(len(adj_matrix)):
                local_matrix[j][i] = 0       

    if k-len(cover) <= 0:
        return set()

    rest_of_cover = cover_check(local_matrix, k - len(cover))
    if len(rest_of_cover) > 0:
        cover.update(rest_of_cover)
    else:
        return set()

    if len(cover) == k:
        return cover
    elif len(cover) < k:
        added_pendants = 0
        added_isolated = 0
        while len(cover) < k:
            if added_pendants == len(pendant):
                cover.add(isolated[added_isolated])
                added_isolated += 1
            else:
                cover.add(pendant[added_pendants])
                added_pendants += 1


graph = [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]
print(smart_cover(graph,13))




