from geomlib import *
from random import shuffle


def get_common_part_borders(hp, index):
    new_hp = hp[index]
    left_down_border = Point(-inf, -inf)
    right_up_border = Point(inf, inf)
    for i in range(index):
        point = new_hp.intersect(hp[i])
        if point is None:
            continue
        if new_hp.b == 0:
            ru_point = Point(point.x, point.y + 1)
        else:
            ru_point = new_hp.get_point_for_x(point.x + 1)

        if ru_point in hp[i]:
            if left_down_border < point:
                left_down_border = point
        else:
            if right_up_border > point:
                right_up_border = point

    if left_down_border > right_up_border:
        return None
    return (left_down_border, right_up_border)


def get_intersection_point(hp):
    shuffle(hp)

    hp_len = len(hp)
    if hp_len == 1:
        return hp[0].get_point_for_x(0)

    answer_point = hp[0].intersect(hp[1])
    if answer_point is None:
        answer_point = hp[0].get_point_for_x(0)
        if answer_point not in hp[1]:
            return None

    for i in range(2, hp_len):
        if answer_point not in hp[i]:
            borders = get_common_part_borders(hp, i)
            if borders is None:
                return None
            answer_point = borders[0]
            if answer_point == Point(-inf, -inf):
                answer_point = borders[1]
                if answer_point == Point(inf, inf):
                    answer_point = hp[i].get_point_for_x(0)

    return answer_point