import math

def elevation_angle(height, distance):
    x  = height/distance
    return math.degrees(math.atan2(height,distance))