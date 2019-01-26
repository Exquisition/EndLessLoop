import argparse
import pandas as pd
import numpy as np
from numpy import genfromtxt
import math



def find_v_max(radii, handling):
    v_max = []
    for i in range(len(radii)-1):
        if(radii[i] == -1):
            v_max.append(radii[i+1])
        else:
            if(radii[i+1] == -1):
                v_max.append(radii[i])
            else:
                v_max.append((min(radii[i], radii[i+1]) * handling/1000000)**(1/2))
    return v_max



def write_params(handling):
    for i in range(7):
        radii = genfromtxt('Hackaton2019/track_' + str(i + 1) + '.csv', delimiter=',')
        v_max_h = find_v_max(radii[1:], handling)
        r = pd.DataFrame({'radii': radii[1:]})
        r.to_excel('data/output.xlsx')
        v = pd.DataFrame({'v_max_h': v_max_h})
        v.to_excel('data/output.xlsx')
        v.to_csv('data/track_{}_h_{}_v'.format(i+1, handling), encoding='utf-8', index=False)
        v.to_csv('data/track_{}_h_{}_radii'.format(i+1, handling), encoding='utf-8', index=False)

def find_acc(v_max, a_max):
    acc = []
    for i in range(len(v_max)):
        num = min(5, len(v_max) - i - 1)
        v_next = 0
        for j in range(num):
            v_next += v_max[i+j]
        v_next = v_next/num
        v_next = min(v_max[i], v_next)
        a = (v_next**2 - (v_max[i])**2)/2
        a = min(a, a_max)
        acc.append(a)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parameters for car')
    parser.add_argument('--acc', type=int, default=0,
                        help='acceleration')
    parser.add_argument('--break', type=int, default=0,
                        help='breaking speed')
    parser.add_argument('--speed', type=int, default=0,
                        help='top speed')
    parser.add_argument('--gas', type=int, default=0,
                        help='gas capacity')
    parser.add_argument('--tire', type=int, default=0,
                        help='tire duration')
    parser.add_argument('--handling', type=int, default=12,
                        help='handling')
    args = parser.parse_args()
    write_params(args.handling)


