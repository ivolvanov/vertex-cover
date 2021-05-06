import copy

def take2(adjacency_matrix):
    adj_matrix = copy.deepcopy(adjacency_matrix)
    cover = []
    for i in range(len(adj_matrix)):
        if 1 in adj_matrix[i]:
            for y in range(len(adj_matrix)):
                if adj_matrix[i][y] == 1:
                    cover.append(i)
                    cover.append(y)

                    for x in range(len(adj_matrix)):
                        adj_matrix[i][x] = 0
                        adj_matrix[x][i] = 0
                        adj_matrix[y][x] = 0
                        adj_matrix[x][y] = 0

    return cover