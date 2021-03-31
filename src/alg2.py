import PySimpleGUI as sg
import generate_dot as gd
import connect_matrix as cm
import random
import os

adjacency_matrix = []

probability_column = [
    [
        sg.Text("Number of vertices"),
        sg.In(size=(25, 1), enable_events=True, key="-VERTICES-"),
    ],
    [
        sg.Text("Probability"),
        sg.In(size=(25, 1), enable_events=True, key="-PROBABILITY-"),
    ],
    [
        sg.Button("Generate", enable_events=True, key="-GENERATE-"),
        sg.Button("Connect", enable_events=True, key="-CONNECT-")
    ]
]

image_viewer_column = [
    [sg.Image(key="-IMAGE-")],
]

layout = [
    [
        sg.Column(probability_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Graph Visualiser", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    elif event == "-GENERATE-":

        adjacency_matrix = []
        line = [0] * int(values["-VERTICES-"])
        for i in range(len(line)):
            adjacency_matrix.append(line[:])
        
        probability = float(values["-PROBABILITY-"])
        for i in range(len(adjacency_matrix)):
            for q in range(i):
                if i != q and random.random() <= probability:
                    adjacency_matrix[i][q] = 1
                    adjacency_matrix[q][i] = 1

        f = open("../dotfiles/graph.dot", "w")
        graphviz_text = gd.generate_dot(adjacency_matrix)
        f.write(graphviz_text)
        f.close()

        os.system('dot -Tpng -o../img/graph.png ../dotfiles/graph.dot')
        window["-IMAGE-"].update(filename="../img/graph.png")

    elif event == "-CONNECT-":
        f = open("../dotfiles/connected_graph.dot", "w")
        graphviz_text = gd.generate_dot(cm.connect_matrix(adjacency_matrix))
        f.write(graphviz_text)
        f.close()

        os.system('dot -Tpng -o../img/connected_graph.png ../dotfiles/connected_graph.dot')
        window["-IMAGE-"].update(filename="../img/connected_graph.png")


window.close()