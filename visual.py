import random

import matplotlib.pyplot as plt
from matplotlib.widgets import Button


def generate_color(exception_colors: list[tuple[float, float, float]]):
    def get_color():
        r = random.uniform(0, 0.6)
        g = random.uniform(0, 0.6)
        b = random.uniform(0, 0.6)
        return r, g, b

    color = get_color()
    while color in exception_colors:
        color = get_color()
    return color


def view(x_range, x_coords, labels, function):
    colors_in_use = []
    y_fun_coords = []
    x_fun_coords = []
    btn_pos = [.01, .01]
    btn_size = [.06, .04]
    buttons = []
    scatters = []

    def toggle_points(event, index):
        for _i in range(len(scatters)):
            if _i != index:
                scatters[_i].set_visible(False)
            else:
                scatters[_i].set_visible(True)
        plt.draw()

    fig, ax = plt.subplots()

    for i in range(x_range[0], x_range[1]):
        x_fun_coords.append(i)
        y_fun_coords.append(function(i))
    ax.plot(x_fun_coords, y_fun_coords)

    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    for i in range(len(x_coords)):
        color = generate_color(colors_in_use)
        colors_in_use.append(color)
        scatters.append(ax.scatter(
            x_coords[i],
            [function(x_coord) for x_coord in x_coords[i]],
            color=color,
            label=labels[i]
        ))
        for x_coord in x_coords[i]:
            ax.text(x_coord, function(x_coord), f'({labels[i]}, {x_coord})', ha='right')

        ax_btn = plt.axes((btn_pos[0], btn_pos[1], btn_size[0], btn_size[1]))
        btn_pos[0] += btn_size[0] + 0.01
        button = Button(ax_btn, labels[i])
        button.on_clicked(func=lambda event, index=i: toggle_points(event, index))
        buttons.append(button)

    plt.show()
