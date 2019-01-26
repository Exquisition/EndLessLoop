import numpy as np
from numpy import genfromtxt
import math


# Acceleration, Breaking, Top Speed, Gas Capacity, Tire Durability, Handling, Cost
tiers = np.array([[10, -10, 10,  500,  500,  9, 0],
                  [15, -15, 20,  750,  750, 12, 2],
                  [20, -20, 30, 1000, 1000, 15, 3],
                  [25, -25, 40, 1250, 1250, 18, 4],
                  [30, -30, 50, 1500, 1500, 21, 5]])

# Calculate maximum velocity for each track at each tier
for cur_tier in range(5):
    print("Tier", cur_tier+1)
    tracks = []
    max_speed = []
    for i in range(8):
        track = genfromtxt('track_'+str(i+1)+'.csv', delimiter=',')
        tracks.append(track[1:])
        max_vel_temp = []
        max_vel = []

        for j in range(1000):
            if track[j+1] >= 0:
                max_vel_temp.append(math.sqrt(track[j+1]*tiers[cur_tier, 5]/1000000))
            else:
                max_vel_temp.append(10000)

        for k in range(1000):
            if k == 0:
                max_vel.append(min(max_vel_temp[k], max_vel_temp[k+1]))
            elif k == 999:
                max_vel.append(min(max_vel_temp[k-1], max_vel_temp[k]))
            else:
                max_vel.append(min(max_vel_temp[k-1], max_vel_temp[k], max_vel_temp[k+1]))

        max_speed.append(np.array(max_vel))

    print(len(tracks[0]))
    print(max_speed[0])

    acceleration = []
    stop_required = False
    cur_gas = tiers[cur_tier, 3]
    cur_wear = tiers[cur_tier, 4]
    for i in range(1000):
        # max_break <= acc <= max_acc
        acc = 0.1
        acceleration.append(acc)

        cur_gas -= 0.1*acc**2
        cur_wear -= 0.1*acc**2
        if cur_gas <= 0 or cur_wear <= 0:
            stop_required = True
        pass



