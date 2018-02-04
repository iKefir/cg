import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from pyhull.convex_hull import ConvexHull
from ipywidgets import interact
from geomlib import *


def draw_sorting_vis():
    lb = -1
    rb = 3
    step = 0.25

    plt.axis([lb, rb, -1, rb ** 2 + 1])

    dots = np.arange(lb - step, rb, 1)

    plt.plot([lb, rb], [0, 0], "black")
    plt.plot(dots, np.zeros(len(dots)), "bo")

    for d in dots:
        hp = HalfPlane(2 * d, -1, -d ** 2)
        hp.draw(left_b=lb, right_b=rb)
        plt.plot([d, d], [0, d ** 2], "gray")

    X = np.arange(lb - step, rb + 2 * step, step)
    Y = X ** 2
    plt.plot(X, Y, "r", linewidth = 3)

    plt.show()


def draw_dual_transform():
    xlb = 0
    xrb = 10
    ylb = 0
    yrb = 10

    A = np.array([-4, -1, -1, -0.25,   1, 0.5])
    B = np.array([1,   1,  1,     1,   1,   1])
    C = np.array([5,  -5,  0,    -3, -10, -10])
    CLR = np.array(["red", "yellow", "brown", "green", "blue", "grey"])
    HP = []

    X = A/B
    Y = C/B

    ch = ConvexHull(np.transpose([X, Y]))

    ax = plt.subplot(1, 2, 1)
    for a, b, c, clr in zip(A, B, C, CLR):
        HP.append(HalfPlane(a, b, c))
        HP[len(HP) - 1].draw(bclr=clr, left_b=xlb, right_b=xrb)

    ax.text(3, 2, "$\mathcal{LE}$")

    ax.axis([xlb, xrb, ylb, yrb])

    bx = plt.subplot(1, 2, 2)

    bx.text(-2, 2, "$\mathcal{UH}$")

    leftX = 500
    rightX = -500
    leftInd = 0
    rightInd = 0

    bottomHP = HalfPlane(0, -1, 0)

    P = []

    for v in ch.vertices:
        if X[v[0]] > X[v[1]]:
            P.append(HP[v[0]].intersect(HP[v[1]]))
            bx.plot(X[v], Y[v], color = "black", linewidth = 3)
            if X[v[0]] > rightX:
                rightX = X[v[0]]
                rightInd = v[0]
            if X[v[1]] < leftX:
                leftX = X[v[1]]
                leftInd = v[1]

    P.append(HP[leftInd].intersect(bottomHP))
    P.append(HP[rightInd].intersect(bottomHP))
    P.sort(key=lambda p: p.x)

    for i in range(len(P) - 1):
        ax.plot([P[i].x, P[i+1].x], [P[i].y, P[i+1].y], color = "black", linewidth = 3)

    for x, y, clr in zip(X, Y, CLR):
        bx.plot(x, y, color=clr, marker="o")

    plt.show()


def execute_draw(A, B, C, CLR):
    xlb = 0
    xrb = 10
    ylb = 0
    yrb = 10

    HP = []

    ax = plt.subplot(1, 3, 1)

    for a, b, c, clr in zip(A, B, C, CLR):
        HP.append(HalfPlane(a, b, c))
        HP[len(HP) - 1].draw(bclr=clr, left_b=xlb, right_b=xrb)

    move_point = Point(4, 2)
    ax.plot(move_point.x, move_point.y, "black", marker="o")
    ax.text(move_point.x, move_point.y + 0.2, "a")

    ax.axis([xlb, xrb, ylb, yrb])

    bx = plt.subplot(1, 3, 2)

    C = C + A*4 + B*2

    X = A / C
    Y = B / C

    ch = ConvexHull(np.transpose([X, Y]))

    xlb -= move_point.x
    xrb -= move_point.x
    ylb -= move_point.y
    yrb -= move_point.y

    for i in range(len(HP)):
        HP[i].move(4, 2)
        HP[i].draw(bclr=CLR[i], left_b=xlb, right_b=xrb)

    bx.plot(0, 0, "black", marker="o")
    bx.text(0, 0.2, "a")

    bx.axis([xlb, xrb, ylb, yrb])

    cx = plt.subplot(1, 3, 3)

    P = []

    MP = {}

    for v in ch.vertices:
        MP[v[0]] = v[1]
        cx.plot(X[v], Y[v], color = "black", linewidth = 3)

    ind = ch.vertices[0][0]

    for i in range(len(ch.vertices)):
        P.append(HP[ind].intersect(HP[MP[ind]]))
        ind = MP[ind]

    P.append(Point(P[0].x, P[0].y))

    for i in range(len(P) - 1):
        bx.plot([P[i].x, P[i+1].x], [P[i].y, P[i+1].y], color = "black", linewidth = 3)

    for p in P:
        p.x += 4
        p.y += 2

    for i in range(len(P) - 1):
        ax.plot([P[i].x, P[i+1].x], [P[i].y, P[i+1].y], color = "black", linewidth = 3)

    for x, y, clr in zip(X, Y, CLR):
        cx.plot(x, y, color=clr, marker="o")

    cx.plot(0, 0, "black", marker="o")

    plt.show()


def draw_second_dual_transform():
    A = np.array([-4, -1, -1, -0.25,   1, 0.5, 0.15])
    B = np.array([1,   1,  1,     1,   1,   1,   -1])
    C = np.array([5,  -5,  0,    -3, -10, -10,    0])
    CLR = np.array(["red", "yellow", "brown", "green", "blue", "grey", "violet"])

    execute_draw(A, B, C, CLR)


def draw_unbounded():
    A = np.array([-4, -1, -1, -0.25,   1, 0.5])
    B = np.array([1,   1,  1,     1,   1,   1])
    C = np.array([5,  -5,  0,    -3, -10, -10])
    CLR = np.array(["red", "yellow", "brown", "green", "blue", "grey"])

    execute_draw(A, B, C, CLR)


def draw_third_dual_transform():
    xlb = 0
    xrb = 10.1
    ylb = 0
    yrb = 10.1
    step = 2

    A = np.array([-4, -1, -1, -0.25,   1, 0.5, 0.15, 0])
    B = np.array([1,   1,  1,     1,   1,   1,   -1, 0])
    C = np.array([5,  -5,  0,    -3, -10, -10,    0, 0])
    CLR = np.array(["red", "yellow", "brown", "green", "blue", "grey", "violet", "black"])

    X = A / -1
    Y = B / -1
    Z = C / -1

    ch = ConvexHull(np.transpose([X, Y, Z]))

    fig = plt.figure()
    # ax = fig.add_subplot(121, projection='3d')
    #
    # ax.axes([xlb, xrb, ylb, yrb])
    #
    # XS = np.arange(xlb, xrb, step = 1)
    # YS = np.arange(ylb, yrb, step = 1)
    # XS, YS = np.meshgrid(XS, YS)
    #
    # for i in range(len(A)):
    #     ZS = A[i]*XS + B[i]*YS + C[i]
    #     ax.plot_surface(XS, YS, ZS, linewidth = 0, color=CLR[i], antialiased = False)

    bx = fig.add_subplot(111, projection='3d')

    bx.scatter(X, Y, Z, c=CLR, marker="o", alpha=1)

    triangles = []
    for v in ch.vertices:
        if v[0] == 7 or v[1] == 7 or v[2] == 7:
            triangles.append(v)

    bx.plot_trisurf(X, Y, Z, alpha=0.1, triangles=triangles)

    plt.show()


def visualise_moving_halfplanes():
    A = np.array([-4, -1, -1, -0.25,   1, 0.5, 0.15])
    B = np.array([1,   1,  1,     1,   1,   1,   -1])
    C = np.array([5,  -5,  0,    -3, -10, -10,    0])
    CLR = np.array(["red", "yellow", "brown", "green", "blue", "grey", "violet"])

    xlb = 0
    xrb = 10
    ylb = 0
    yrb = 10

    ax = plt.subplot(111)

    def draw_for_t(t=0):
        ax.clear()
        for a, b, c, clr in zip(A, B, C, CLR):
            HalfPlane(a, b, c - t).draw(bclr=clr, left_b=xlb, right_b=yrb)

        ax.axis([xlb, xrb, ylb, yrb])
        plt.show()

    interact(draw_for_t, t=(-10, 10))