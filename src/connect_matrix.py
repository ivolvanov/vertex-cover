def connect_matrix(adj_matrix):
    stack = []
    visited_nodes = []

    stack.append(0)
    visited_nodes.append(0)

    while len(visited_nodes) < len(adj_matrix):

        while len(stack) > 0:
            current_node = stack.pop(0)
            visited_nodes.append(current_node)
            for i in range(len(adj_matrix)):
                if adj_matrix[current_node][i] == 1 and (i not in stack) and (i not in visited_nodes):
                    stack.append(i)
    
        for i in range(len(adj_matrix)):
            if i not in visited_nodes:
                adj_matrix[i][visited_nodes[len(visited_nodes) - 1]] = 1
                adj_matrix[visited_nodes[len(visited_nodes) - 1]][i] = 1
                # adj_matrix[i][0] = 1
                # adj_matrix[0][i] = 1
                stack.append(i)
                break

    return adj_matrix
