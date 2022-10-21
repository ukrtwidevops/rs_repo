def gps(s, x):
    if len(x) > 1:
        speed = []
        for i in range(0, len(x)-1):
            delta_dist = x[i+1] - x[i]
            speed.append(int((3600 * delta_dist)/s))
        return max(speed)
    else:
        return 0