import PySimpleGUI as sg
import generate_dot as gd
import connect_matrix as cm
import vertex_cover as vc
import kernelization as kz
import random
import os
import asyncio

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
        sg.Text("Nr of vertices for vertex cover"),
        sg.In(size=(25, 1), enable_events=True, key="-VERTICES_COVER-"),
    ],
    [
        sg.Button("Generate", enable_events=True, key="-GENERATE-"),
        sg.Button("Connect", enable_events=True, key="-CONNECT-"), 
        sg.Button("Vertex cover", enable_events=True, key="-COVER-")
    ],
    [
        sg.Text("",key="-STATUS-", text_color="red",size=(51, 1)),
    ],
    [
        sg.Text("k"),
        sg.In(size=(25, 1), enable_events=True, key="-K-"),
    ],
    [
        sg.Button("Add pendant", enable_events=True, key="-P++-"),
        sg.Button("Add tops using k", enable_events=True, key="-T++-"),
        sg.Button("Kernelize using k", enable_events=True, key="-KERNELIZE-")
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
        window["-STATUS-"].update('')
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
        window["-STATUS-"].update('')
        f = open("../dotfiles/connected_graph.dot", "w")
        adjacency_matrix = cm.connect_matrix(adjacency_matrix)
        graphviz_text = gd.generate_dot(adjacency_matrix)
        f.write(graphviz_text)
        f.close()

        os.system('dot -Tpng -o../img/connected_graph.png ../dotfiles/connected_graph.dot')
        window["-IMAGE-"].update(filename="../img/connected_graph.png")

    elif event == "-COVER-":  
        cover = vc.cover_check(adjacency_matrix,int(values["-VERTICES_COVER-"]))

        if len(cover) > 0:
            f = open("../dotfiles/covered_graph.dot", "w")
            graphviz_text = gd.generate_dot_with_cover(adjacency_matrix, cover)
            f.write(graphviz_text)
            f.close()

            os.system('dot -Tpng -o../img/covered_graph.png ../dotfiles/covered_graph.dot')
            window["-IMAGE-"].update(filename="../img/covered_graph.png")

        else:
            window["-STATUS-"].update('There is no vertex cover with the selected number of vertices')

    elif event == "-P++-":
        window["-STATUS-"].update('')
        f = open("../dotfiles/p++_graph.dot", "w")
        adjacency_matrix = kz.make_pendant_vertex(adjacency_matrix)
        graphviz_text = gd.generate_dot(adjacency_matrix)
        f.write(graphviz_text)
        f.close()

        os.system('dot -Tpng -o../img/p++_graph.png ../dotfiles/p++_graph.dot')
        window["-IMAGE-"].update(filename="../img/p++_graph.png")

    elif event == "-T++-":
        window["-STATUS-"].update('')
        k = int(values["-K-"])
        f = open("../dotfiles/t++_graph.dot", "w")
        adjacency_matrix = kz.make_tops_vetrex(adjacency_matrix, k)
        graphviz_text = gd.generate_dot(adjacency_matrix)
        f.write(graphviz_text)
        f.close()

        os.system('dot -Tpng -o../img/t++_graph.png ../dotfiles/t++_graph.dot')
        window["-IMAGE-"].update(filename="../img/t++_graph.png")

    elif event == "-KERNELIZE-":
        window["-STATUS-"].update('')
        k = int(values["-K-"])
        f = open("../dotfiles/kernelized_graph.dot", "w")

        isolated = kz.isolated_vertices(adjacency_matrix)
        pendant = kz.pendant_vertices(adjacency_matrix)
        tops = kz.tops_vertices(adjacency_matrix, k)

        graphviz_text = gd.generate_dot_with_kernelization(adjacency_matrix, isolated, pendant, tops)
        f.write(graphviz_text)
        f.close()

        os.system('dot -Tpng -o../img/kernelized_graph.png ../dotfiles/kernelized_graph.dot')
        window["-IMAGE-"].update(filename="../img/kernelized_graph.png")


window.close()