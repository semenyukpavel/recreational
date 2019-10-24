import matplotlib.pyplot as plt
import random

from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'k.')

vertices = [[0.0, 0.0], [2.0, 4.0], [4.0, 0.0]]

points = []


def gen_points(n, pts):
    for i in range(n):
        vertex = random.choice(vertices)
        if len(points) == 0:
            start_x = random.uniform(0.0, 2.0)
            start_y = random.uniform(0.0, 2.0)
            point = [start_x, start_y]
        else:
            point = pts[-1]

        nx = point[0] + (vertex[0] - point[0]) / 2
        ny = point[1] + (vertex[1] - point[1]) / 2

        pts.append([nx, ny])

    return pts


def init():
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 4.5)
    return ln,


def update(frame):
    xdata.append(frame[0])
    ydata.append(frame[1])
    ln.set_data(xdata, ydata)
    return ln,


if __name__ == '__main__':
    ani = FuncAnimation(fig, update, frames=gen_points(100, points), init_func=init, blit=True)
    plt.show()
