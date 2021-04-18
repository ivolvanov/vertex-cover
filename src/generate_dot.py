def generate_dot(adj_matrix):
    graphviz_text = ""
    graphviz_text += "graph my_graph {\nnode [ fontname = Arial, style=\"filled,setlinewidth(4)\", shape=circle ]"

    for i in range(len(adj_matrix)):
        line = "\nnode" + str(i) + " [ label = \"" + str(i) + "\" ]"
        graphviz_text += line

    graphviz_text += __add_connections__(adj_matrix)
    
    return graphviz_text

def generate_dot_with_cover(adj_matrix, cover):
    graphviz_text = ""
    graphviz_text += "graph my_graph {\nnode [ fontname = Arial, style=\"filled,setlinewidth(4)\", shape=circle ]"

    for i in range(len(adj_matrix)):
        line = "\nnode" + str(i) + " [ label = \"" + str(i) + "\""
        if i in cover:
            line = line + " color=red "
        line = line + " ]"
        graphviz_text += line

    graphviz_text += __add_connections__(adj_matrix)

    return graphviz_text

def generate_dot_with_kernelization(adj_matrix, isolated_vertices, pendant_vertices, tops_vertices):
    graphviz_text = "graph my_graph {\nnode [ fontname = Arial, style=\"filled,setlinewidth(4)\", shape=circle ]"
    graphviz_text += "label = \"RED - isolated \n GREEN - pendant \n BLUE - tops\" \n labelloc = t"

    for i in range(len(adj_matrix)):
        line = "\nnode" + str(i) + " [ label = \"" + str(i) + "\""

        if i in isolated_vertices:
            line = line + " color=red "
        elif i in pendant_vertices:
            line = line + " color=green "
        if i in tops_vertices:
            line = line + " color=blue "
        line = line + " ]"

        graphviz_text += line

    graphviz_text += __add_connections__(adj_matrix)
        
    return graphviz_text

def __add_connections__(adj_matrix):
    local_text = ""
    local_text += "\n"
    for i in range(len(adj_matrix)):
        for q in range(i):
            if adj_matrix[i][q] == 1:
                line = "\nnode" + str(i) + " -- node" + str(q)
                local_text += line

    local_text += "\n" + "}"
    return local_text