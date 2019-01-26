import numpy as np
from numpy import genfromtxt
import math


handling_coeff = 15

tracks = []
max_speed = []
for i in range(8):
    track = genfromtxt('track_'+str(i+1)+'.csv', delimiter=',')
    tracks.append(track[1:])
    max_vel = []
    for j in range(1000):
        if track[j+1] >= 0:
            max_vel.append(math.sqrt(track[j+1]*handling_coeff/1000000))
        else:
            max_vel.append(-1)
    max_speed.append(np.array(max_vel))

print(len(tracks[0]))
print(max_speed[0])

