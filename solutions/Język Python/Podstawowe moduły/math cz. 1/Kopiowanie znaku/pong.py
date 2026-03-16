import math


def paddle_velocity(base_speed, paddle_y, ball_y):
    if paddle_y == ball_y:
        return 0
    else:
        if ball_y- paddle_y  > 0:
            return math.copysign(base_speed,1)
        else:
            return math.copysign(base_speed,-1)