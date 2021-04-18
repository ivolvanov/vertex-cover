from itertools import combinations
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