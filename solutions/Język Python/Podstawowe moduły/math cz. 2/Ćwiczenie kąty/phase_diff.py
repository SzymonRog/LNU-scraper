import math

def phase_diff(phase1, phase2):
    sin_r = math.sin(phase2 - phase1)
    cos_r = math.cos(phase2 - phase1)
    return math.degrees(math.atan2(sin_r,cos_r))