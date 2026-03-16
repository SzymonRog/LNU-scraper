def estimate(x, t, v):
    return "Yes" if x <= float(t/60) * v else "No"