import numpy as np
from numpy import genfromtxt
import math


# Acceleration, Breaking, Top Speed, Gas Capacity, Tire Durability, Handling
tiers = np.array([[10, -10, 10,  500,  500,  9],
                  [15, -15, 20,  750,  750, 12],
                  [20, -20, 30, 1000, 1000, 15],
                  [25, -25, 40, 1250, 1250, 18],
                  [30, -30, 50, 1500, 1500, 21]])
tier = 4


tracks = []
max_speed = []
for i in range(8):
    track = genfromtxt('track_'+str(i+1)+'.csv', delimiter=',')
    tracks.append(track[1:])
    max_vel = []
    for j in range(1000):
        if track[j+1] >= 0:
            max_vel.append(math.sqrt(track[j+1]*tiers[tier, 5]/1000000))
        else:
            max_vel.append(-1)
    max_speed.append(np.array(max_vel))

print(len(tracks[0]))
print(max_speed[0])
