from itertools import combinations
import kernelization
import copy


def __generate_all_covers__(matrix_size, cover_size):
    combos = []

    for assignment in list(combinations(range(matrix_size), cover_size)):
        combos.append(assignment)

    return combos


def __is_cover_valid__(adj_matrix_arg):
    for i in range(len(adj_matrix_arg)):
        for j in range(len(adj_matrix_arg)):
            if adj_matrix_arg[i][j] == 1:
                return False

    return True

def cover_check(adj_matrix, cover_size):
    if len(adj_matrix[0]) == 0:
        return set()

    combinations = __generate_all_covers__(len(adj_matrix), cover_size)
    index_comb = len(combinations)
    for combo in combinations:
        
        local_matrix = copy.deepcopy(adj_matrix)
        for i in combo:
            for j in range(len(local_matrix)):
                local_matrix[i][j] = 0
                local_matrix[j][i] = 0

        index_comb -= 1
        
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
            pendant_neighbours.append(adj_matrix[i].index(1))            

    cover.update(pendant_neighbours)
    not_in_cover.difference_update(cover)

    to_be_removed = set()
    to_be_removed.update(cover)
    to_be_removed.update(not_in_cover)

    to_be_removed2 = list(to_be_removed)
    local_matrix = copy.deepcopy(adj_matrix)

    local_matrix = [i for i in local_matrix if i not in to_be_removed2]
    local_matrix = [listEle for listEle in local_matrix if listEle != []]
    if len(local_matrix) > 0:
        for q in range(len(local_matrix)):
            local_matrix[q] = [p for p in local_matrix[q] if p not in to_be_removed2]
            local_matrix[q] = [listEle for listEle in local_matrix[q] if listEle != []]

    
    cover.update(cover_check(local_matrix, k - len(cover)))

    if len(cover) == k:
        return cover
    else:
        return set()




