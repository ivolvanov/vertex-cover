import PySimpleGUI as sg
import random

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
        sg.Button("Generate", enable_events=True, key="-GENERATE-")
    ]
]

image_viewer_column = [
    [sg.Image(key="-IMAGE-", filename='../test_graph.png')],
]

layout = [
    [
        sg.Column(probability_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Image Viewer", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    elif event == "-GENERATE-":

        line = [0] * int(values["-VERTICES-"])
        for i in range(len(line)):
            adjacency_matrix.append(line[:])
        
        probability = float(values["-PROBABILITY-"])
        for i in range(len(adjacency_matrix)):
            for q in range(i):
                if i != q and random.random() <= probability:
                    adjacency_matrix[i][q] = 1
                    adjacency_matrix[q][i] = 1

        f = open("graph.dot", "w")
        graphviz_text = ""
        graphviz_text = graphviz_text + "graph my_graph {\nnode [ fontname = Arial, style=\"filled,setlinewidth(4)\", shape=circle ]"
        f.write(graphviz_text)
        f.close()
    

window.close()