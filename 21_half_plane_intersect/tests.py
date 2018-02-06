from geomlib import *
from solution import first_left_func, first_right_func, second_left_func, second_right_func
import numpy as np
import matplotlib.pyplot as plt


# FULL TEST
class test_obj:
    def __init__(self, number, input, answer, left_b = -15, right_b = 15):
        self.number = number
        self.input = input
        self.answer = answer
        self.left_b = left_b
        self.right_b = right_b


def test(func, to):
    res = func(to.input)
    if res == to.answer:
        print("Test",to.number,": OK")
    else:
        print("Test",to.number,": BAD")
        print("\tExpected:", to.answer)
        print("\tGot     :", res)
        for i in range(len(to.input)):
            to.input[i].draw(left_b = to.left_b, right_b = to.right_b)
        plt.show()


t_1 = [
    HalfPlane(1, -1, 2),
    HalfPlane(-1, -1, 2),
    HalfPlane(0, -1, -1),
    HalfPlane(0, -1, 3),
    HalfPlane(0, -1, 4)
]

e_1 = ([HalfPlane(-1, -1, 2)], [HalfPlane(1, -1, 2), HalfPlane(0, -1, 4)])

t_2 = [
    HalfPlane(-1, 1, 2),
    HalfPlane(-1, -1, 2),
    HalfPlane(1, 1, -5),
    HalfPlane(1, -1, -5)
]

e_2 = ([HalfPlane(-1, 1, 2), HalfPlane(-1, -1, 2)], [HalfPlane(1, 1, -5), HalfPlane(1, -1, -5)])

t_3 = [
    HalfPlane(0, 1, -1),
    HalfPlane(-1, 1, 2),
    HalfPlane(-1, -1, 2),
    HalfPlane(1, 1, -5),
    HalfPlane(1, -1, -5)
]

e_3 = ([HalfPlane(0, 1, -1), HalfPlane(-1, 1, 2), HalfPlane(-1, -1, 2)], [HalfPlane(1, 1, -5), HalfPlane(1, -1, -5)])

t_4 = [
    HalfPlane(0.25, 1, -2),
    HalfPlane(-1, 1, 2),
    HalfPlane(-1, -1, 2),
    HalfPlane(1, 1, -5),
    HalfPlane(1, -1, -5)
]

e_4 = ([HalfPlane(-1, 1, 2), HalfPlane(-1, -1, 2)], [HalfPlane(0.25, 1, -2), HalfPlane(1, 1, -5), HalfPlane(1, -1, -5)])

t_5 = [
    HalfPlane(1, -1, 2),
    HalfPlane(0, -1, 0),
    HalfPlane(-1, 0, 0)
]

e_5 = ([HalfPlane(-1, 0, 0)], [HalfPlane(1, -1, 2)])

t_6 = [
    HalfPlane(1, 1, 2),
    HalfPlane(0, -1, 0),
    HalfPlane(-1, 0, 0)
]

e_6 = ([], [])

t_7 = [
    HalfPlane(1, 1, -2),
    HalfPlane(0, -1, 0),
    HalfPlane(-1, 0, 0)
]

e_7 = ([HalfPlane(-1, 0, 0)], [HalfPlane(1, 1, -2), HalfPlane(0, -1, 0)])

t_8 = [
    HalfPlane(0, -1, 0),
    HalfPlane(0, 1, 0),
    HalfPlane(1, 0, 0),
    HalfPlane(-1, 0, 0)
]

e_8 = ([HalfPlane(0, 1, 0), HalfPlane(-1, 0, 0)], [HalfPlane(1, 0, 0), HalfPlane(0, -1, 0)])

t_9 = [
    HalfPlane(1, -1, -2),
    HalfPlane(1, 1, -2),
    HalfPlane(-1, -1, 5),
    HalfPlane(-1, 1, 5)
]

e_9 = ([], [])

to_1 = test_obj(1, t_1, e_1, -5, 5)
to_2 = test_obj(2, t_2, e_2, 0, 5)
to_3 = test_obj(3, t_3, e_3, 0, 5)
to_4 = test_obj(4, t_4, e_4, 0, 5)
to_5 = test_obj(5, t_5, e_5, -2, 4)
to_6 = test_obj(6, t_6, e_6, -5, 5)
to_7 = test_obj(7, t_7, e_7, -2, 4)
to_8 = test_obj(8, t_8, e_8, -2, 4)
to_9 = test_obj(9, t_9, e_9, 0, 6)

def full_test(func):
    plt.ioff()
    test(func, to_1)
    test(func, to_2)
    test(func, to_3)
    test(func, to_4)
    test(func, to_5)
    test(func, to_6)
    test(func, to_7)
    test(func, to_8)
    test(func, to_9)


def test_point(func, to):
    answer = func(to.input)
    ans_is_none = to.answer == ([], [])
    if answer is None:
        if ans_is_none:
            print("Test",to.number,": OK")
            return
        else:
            print("Test",to.number,": BAD")
            print("\tYour answer is None, but there is an intersection")
            for i in range(len(to.input)):
                to.input[i].draw(left_b=to.left_b, right_b=to.right_b)
            plt.show()
            return

    if ans_is_none:
        print("Test",to.number,": BAD")
        print("\tYour answer is",answer,"but there is no intersection")
        left_b = answer.x if answer.x < to.left_b else to.left_b
        right_b = answer.x if answer.x > to.right_b else to.right_b
        for j in range(len(to.input)):
            to.input[j].draw(left_b=left_b, right_b=right_b)
        answer.draw()
        plt.show()
        return

    for i in range(len(to.input)):
        if answer not in to.input[i]:
            print("Test",to.number,": BAD")
            print("\tYour answer is not in intersection")
            left_b = answer.x if answer.x < to.left_b else to.left_b
            right_b = answer.x if answer.x > to.right_b else to.right_b
            for j in range(len(to.input)):
                to.input[j].draw(left_b=left_b, right_b=right_b)
            answer.draw()
            plt.show()
            return

    print("Test",to.number,": OK")


def full_test_point(func):
    plt.ioff()
    test_point(func, to_1)
    test_point(func, to_2)
    test_point(func, to_3)
    test_point(func, to_4)
    test_point(func, to_5)
    test_point(func, to_6)
    test_point(func, to_7)
    test_point(func, to_8)
    test_point(func, to_9)


# FUNCTION TESTS


def get_random_hp(direction):
    while True:
        random_ints = np.random.randint(-100, 100, size=3)
        hp = HalfPlane(random_ints[0], random_ints[1], random_ints[2])
        if direction ^ hp.orientation_downright():
            return hp


def get_random_point_on_edge(hp):
    random_x = np.random.randint(-1000, 1000)
    res_p = hp.get_point_for_x(random_x)
    return res_p


def generate_test_case(function_number):
    if function_number == 0:
        hp1 = get_random_hp(False)
        hp2 = get_random_hp(False)
        hp3 = get_random_hp(True)
        point = get_random_point_on_edge(hp1)
    elif function_number == 1:
        hp1 = get_random_hp(True)
        hp2 = get_random_hp(False)
        hp3 = get_random_hp(True)
        point = get_random_point_on_edge(hp1)
    elif function_number == 2:
        hp1 = get_random_hp(False)
        hp2 = get_random_hp(True)
        hp3 = get_random_hp(False)
        point = get_random_point_on_edge(hp3)
    else:
        hp1 = get_random_hp(False)
        hp2 = get_random_hp(True)
        hp3 = get_random_hp(True)
        point = get_random_point_on_edge(hp3)
    return hp1, hp2, hp3, point


def test_func(f_num, f, correct_f):
    for i in range(1000):
        tc = generate_test_case(f_num)
        ans = f(tc[0], tc[1], tc[2], tc[3])
        correct_ans = correct_f(tc[0], tc[1], tc[2], tc[3])
        if ans != correct_ans:
            print("Test", i+1, ": BAD")
            break
        if (i+1)%100 == 0:
            print("Test", i+1, ": OK")


def help_func_test(f1, f2, f3, f4):
    print("Testing first_left_func:")
    test_func(0, f1, first_left_func)
    print("Testing first_right_func:")
    test_func(1, f2, first_right_func)
    print("Testing second_left_func:")
    test_func(2, f3, second_left_func)
    print("Testing second_right_func:")
    test_func(3, f4, second_right_func)