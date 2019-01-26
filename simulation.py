import argparse
import pandas as pd
import numpy as np
from numpy import genfromtxt
import math

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parameters for car')
    parser.add_argument('--acc', type=int,
                        help='acceleration')
    parser.add_argument('--break', type=int,
                        help='breaking speed')
    parser.add_argument('--speed', type=int,
                        help='top speed')
    parser.add_argument('--gas', type=int,
                        help='gas capacity')
    parser.add_argument('--tire', type=int,
                        help='tire duration')
    parser.add_argument('--handling', type=int,
                        help='handling')
    args = parser.parse_args()


def find_v_max(radii, handling):
    v_max = []
    for i in range(len(radii)):
        if(radii[i] == -1):
            v_max.append(-1)
        else:
            max = (radii[i] * handling/1000000)^1/2
            v_max.append(max)



def write_params():
    radii = []
    track_num = 1
    for i in range(7):
        v_max_h = find_v_max()
        radii_ = genfromtxt('/Hackaton2019/track_' + str(i + 1) + '.csv', delimiter=',')
        info = pd.DataFrame({'radii': radii[1:] ,'v_max_h': [],
                       'b': [3, 5, 6, 2, 4, 6, 7, 8, 7, 8, 9]})
