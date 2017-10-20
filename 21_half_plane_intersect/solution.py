from geomlib import *


# event in l_C1
def first_left_func(le_C1_next, le_C2, re_C2, event):
    left_ans = []
    right_ans = []
    if le_C1_next is None:
        return left_ans, right_ans
    if (le_C2 is None or event in le_C2) and (re_C2 is None or event in re_C2):
        left_ans.append(le_C1_next)
    if re_C2 is not None and le_C1_next.intersect_from_point(event, re_C2) is not None:
        if not (event in re_C2):
            left_ans.append(le_C1_next)
            right_ans.append(re_C2)
    if le_C2 is not None and le_C1_next.intersect_from_point(event, le_C2) is not None:
        if event in le_C2:
            left_ans.append(le_C2)
        else:
            left_ans.append(le_C1_next)
    return left_ans, right_ans


# event in r_C1
def first_right_func(re_C1_next, le_C2, re_C2, event):
    left_ans = []
    right_ans = []
    if re_C1_next is None:
        return left_ans, right_ans
    if (le_C2 is None or event in le_C2) and (re_C2 is None or event in re_C2):
        right_ans.append(re_C1_next)
    if le_C2 is not None and re_C1_next.intersect_from_point(event, le_C2) is not None:
        if not (event in le_C2):
            right_ans.append(re_C1_next)
            left_ans.append(le_C2)
    if re_C2 is not None and re_C1_next.intersect_from_point(event, re_C2) is not None:
        if event in re_C2:
            right_ans.append(re_C2)
        else:
            right_ans.append(re_C1_next)
    return left_ans, right_ans


# event in l_C2
def second_left_func(le_C1, re_C1, le_C2_next, event):
    left_ans = []
    right_ans = []
    if le_C2_next is None:
        return left_ans, right_ans
    if (le_C1 is None or event in le_C1) and (re_C1 is None or event in re_C1):
        left_ans.append(le_C2_next)
    if re_C1 is not None and le_C2_next.intersect_from_point(event, re_C1) is not None:
        if not (event in re_C1):
            left_ans.append(le_C2_next)
            right_ans.append(re_C1)
    if le_C1 is not None and le_C2_next.intersect_from_point(event, le_C1) is not None:
        if event in le_C1:
            left_ans.append(le_C1)
        else:
            left_ans.append(le_C2_next)
    return left_ans, right_ans


# event in r_C2
def second_right_func(le_C1, re_C1, re_C2_next, event):
    left_ans = []
    right_ans = []
    if re_C2_next is None:
        return left_ans, right_ans
    if (le_C1 is None or event in le_C1) and (re_C1 is None or event in re_C1):
        right_ans.append(re_C2_next)
    if le_C1 is not None and re_C2_next.intersect_from_point(event, le_C1) is not None:
        if not (event in le_C1):
            right_ans.append(re_C2_next)
            left_ans.append(le_C1)
    if re_C1 is not None and re_C2_next.intersect_from_point(event, re_C1) is not None:
        if event in re_C1:
            right_ans.append(re_C1)
        else:
            right_ans.append(re_C2_next)
    return left_ans, right_ans