import matplotlib.pyplot as plt
import numpy as np
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

    X = np.array([-4, -1, -1, -0.25, 1, 0.5])
    Y = np.array([5, -5, 0, -3, -10, -10])
    clr = np.array(["red", "yellow", "brown", "green", "blue", "grey"])
    HP = []

    ax = plt.subplot(1, 2, 1)
    for x, y, c in zip(X, Y, clr):
        HP.append(HalfPlane(x, 1, y))
        HP[len(HP) - 1].draw(bclr=c, left_b=xlb, right_b=xrb)

    bottomHP = HalfPlane(0, -1, 0)
    p0 = bottomHP.intersect(HP[0])
    p1 = HP[0].intersect(HP[2])
    p2 = HP[2].intersect(HP[3])
    p3 = HP[3].intersect(HP[4])
    p4 = HP[4].intersect(bottomHP)
    ax.plot([p0.x, p1.x], [p0.y, p1.y], "black", linewidth=3)
    ax.plot([p1.x, p2.x], [p1.y, p2.y], "black", linewidth=3)
    ax.plot([p2.x, p3.x], [p2.y, p3.y], "black", linewidth=3)
    ax.plot([p3.x, p4.x], [p3.y, p4.y], "black", linewidth=3)

    p_point = Point(10/3, 10/3+5)
    ax.plot(p_point.x, p_point.y, "black", marker="o")
    ax.text(p_point.x + 0.2, p_point.y, "p")

    ax.axis([xlb, xrb, ylb, yrb])

    ax = plt.subplot(1, 2, 2)

    ax.plot([-4, -1], [5, 0], "black", linewidth=3)
    ax.plot([-1, -0.25], [0, -3], "black", linewidth=3)
    ax.plot([-0.25, 1], [-3, -10], "black", linewidth=3)

    p_line = Line(p_point.x, 1, p_point.y)
    p_line.draw(left_b=-4, right_b=1, linestyle="--", lwidth=1)
    ax.text(-2.5, 0, "p*")

    for x, y, c in zip(X, Y, clr):
        ax.plot(x, y, color=c, marker="o")

    plt.show()


def draw_second_dual_transform():
    xlb = 0
    xrb = 10
    ylb = 0
    yrb = 10

    X = np.array([-4, -1, -1, -0.25, 1, 0.5])
    Y = np.array([5, -5, 0, -3, -10, -10])
    clr = np.array(["red", "yellow", "brown", "green", "blue", "grey", "violet"])
    HP = []

    ax = plt.subplot(1, 3, 1)

    for x, y, c in zip(X, Y, clr):
        HP.append(HalfPlane(x, 1, y))
        HP[len(HP) - 1].draw(bclr=c, left_b=xlb, right_b=xrb)

    HP.append(HalfPlane(0.15, -1, 0))
    HP[len(HP) - 1].draw(bclr=clr[len(HP) - 1], left_b=xlb, right_b=xrb)

    p0 = HP[6].intersect(HP[0])
    p1 = HP[0].intersect(HP[2])
    p2 = HP[2].intersect(HP[3])
    p3 = HP[3].intersect(HP[4])
    p4 = HP[4].intersect(HP[6])
    ax.plot([p0.x, p1.x], [p0.y, p1.y], "black", linewidth=3)
    ax.plot([p1.x, p2.x], [p1.y, p2.y], "black", linewidth=3)
    ax.plot([p2.x, p3.x], [p2.y, p3.y], "black", linewidth=3)
    ax.plot([p3.x, p4.x], [p3.y, p4.y], "black", linewidth=3)
    ax.plot([p4.x, p0.x], [p4.y, p0.y], "black", linewidth=3)

    move_point = Point(4, 2)
    ax.plot(move_point.x, move_point.y, "black", marker="o")
    ax.text(move_point.x, move_point.y + 0.2, "a")

    p_point = Point(10 / 3, 10 / 3 + 5)
    ax.plot(p_point.x, p_point.y, "black", marker="o")
    ax.text(p_point.x + 0.2, p_point.y, "p")

    ax.axis([xlb, xrb, ylb, yrb])

    bx = plt.subplot(1, 3, 2)

    xlb -= move_point.x
    xrb -= move_point.x
    ylb -= move_point.y
    yrb -= move_point.y

    for i in range(len(HP)):
        HP[i].move(4, 2)
        HP[i].draw(bclr=clr[i], left_b=xlb, right_b=xrb)

    p0 = HP[6].intersect(HP[0])
    p1 = HP[0].intersect(HP[2])
    p2 = HP[2].intersect(HP[3])
    p3 = HP[3].intersect(HP[4])
    p4 = HP[4].intersect(HP[6])

    bx.plot([p0.x, p1.x], [p0.y, p1.y], "black", linewidth=3)
    bx.plot([p1.x, p2.x], [p1.y, p2.y], "black", linewidth=3)
    bx.plot([p2.x, p3.x], [p2.y, p3.y], "black", linewidth=3)
    bx.plot([p3.x, p4.x], [p3.y, p4.y], "black", linewidth=3)
    bx.plot([p4.x, p0.x], [p4.y, p0.y], "black", linewidth=3)

    p_point.x -= move_point.x
    p_point.y -= move_point.y
    bx.plot(p_point.x, p_point.y, "black", marker="o")
    bx.text(p_point.x + 0.2, p_point.y, "p")

    bx.plot(0, 0, "black", marker="o")
    bx.text(0, 0.2, "a")

    bx.axis([xlb, xrb, ylb, yrb])

    cx = plt.subplot(1, 3, 3)

    P = []

    xlb = 100
    xrb = -100

    for i in range(len(HP)):
        point = Point(HP[i].a / HP[i].c, HP[i].b / HP[i].c)
        P.append(point)
        if point.x < xlb:
            xlb = point.x
        if point.x > xrb:
            xrb = point.x

    cx.plot([P[6].x, P[0].x], [P[6].y, P[0].y], "black", linewidth=3)
    cx.plot([P[0].x, P[2].x], [P[0].y, P[2].y], "black", linewidth=3)
    cx.plot([P[2].x, P[3].x], [P[2].y, P[3].y], "black", linewidth=3)
    cx.plot([P[3].x, P[4].x], [P[3].y, P[4].y], "black", linewidth=3)
    cx.plot([P[4].x, P[6].x], [P[4].y, P[6].y], "black", linewidth=3)

    p_line = Line(-p_point.x, -p_point.y, -1)
    p_line.draw(left_b=xlb, right_b=xrb, linestyle="--", lwidth=1)
    cx.text(0, -0.12, "p*")

    for i in range(len(P)):
        cx.plot(P[i].x, P[i].y, color=clr[i], marker="o")

    cx.plot(0, 0, "black", marker="o")

    plt.show()