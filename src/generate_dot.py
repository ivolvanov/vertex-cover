def generate_dot(adj_matrix):
    graphviz_text = ""
    graphviz_text = graphviz_text + "graph my_graph {\nnode [ fontname = Arial, style=\"filled,setlinewidth(4)\", shape=circle ]"

    for i in range(len(adj_matrix)):
        line = "\nnode" + str(i) + " [ label = \"" + str(i) + "\" ]"
        graphviz_text = graphviz_text + line

    graphviz_text = graphviz_text + "\n"
    for i in range(len(adj_matrix)):
        for q in range(i):
            if adj_matrix[i][q] == 1:
                line = "\nnode" + str(i) + " -- node" + str(q)
                graphviz_text = graphviz_text + line

    graphviz_text = graphviz_text + "\n" + "}"
    return graphviz_text

def generate_dot_with_cover(adj_matrix, cover):
    graphviz_text = ""
    graphviz_text = graphviz_text + "graph my_graph {\nnode [ fontname = Arial, style=\"filled,setlinewidth(4)\", shape=circle ]"

    for i in range(len(adj_matrix)):
        line = "\nnode" + str(i) + " [ label = \"" + str(i) + "\""
        if i in cover:
            line = line + " color=red "
        line = line + " ]"
        graphviz_text = graphviz_text + line

    graphviz_text = graphviz_text + "\n"
    for i in range(len(adj_matrix)):
        for q in range(i):
            if adj_matrix[i][q] == 1:
                line = "\nnode" + str(i) + " -- node" + str(q)
                graphviz_text = graphviz_text + line

    graphviz_text = graphviz_text + "\n" + "}"
    return graphviz_text