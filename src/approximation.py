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

def greedy(adjacency_matrix):
    adj_matrix = copy.deepcopy(adjacency_matrix)
    cover = []
    index_N = 0
    biggest_N = 0
    stop = False

    while not stop:
        isFinish = False
        biggest_N = 0
        for i in range(len(adj_matrix)):
            N = 0 
            if 1 in adj_matrix[i]:
                isFinish = True
                for y in range(len(adj_matrix)):
                    if adj_matrix[i][y] == 1:
                        N += 1

            if N > biggest_N:
                biggest_N = N
                index_N = i 

                    
        if not isFinish:
            stop = True

        else:
            for x in range(len(adj_matrix)): 
                cover.append(index_N)          
                adj_matrix[x][index_N] = 0
                adj_matrix[index_N][x] = 0

        

    return cover