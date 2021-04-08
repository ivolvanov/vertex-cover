from itertools import product
import copy


def __generate_all_covers__(matrix_size, cover_size):
    combinations = []

    for assignment in product(list(range(matrix_size)), repeat=cover_size):
        if len(set(assignment)) == cover_size and set(assignment) not in combinations:
            combinations.append(set(assignment))

    return combinations


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
        #alg2.window["-PROG-"].update((index_comb/len(combinations))*1000)
        local_matrix = copy.deepcopy(adj_matrix)
        for i in combo:
            for j in range(len(local_matrix)):
                local_matrix[i][j] = 0
                local_matrix[j][i] = 0

        index_comb -= 1
        
        if __is_cover_valid__(local_matrix) == True:
            return combo

    return set()

#graph = [[0, 1, 0, 0, 1], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 0, 1], [1, 0, 0, 1, 0]]

#cover_check(graph,5)