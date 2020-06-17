# Laba2. Dispersion, expected_value and cocorelation

import sys
sys.path.append('../lab1')

import matplotlib.pyplot as plt
import random
import math
import numpy as np
import pandas as pd
import time

from lab1 import generate_signal, draw, DrawOption, N, n, w, A, x


Rxx_timer = []
Rxy_timer = []

def expected_value(signal):
  M = 0
  for i in range(N):
    M = M + signal[i]
  M = M / N
  return M


def dispersion(M, signal):
  D = 0
  for i in range(N):
    D = D + math.pow(signal[i] - M*signal[i], 2)
  D = D / (N - 1)
  return D

# Автокорелляция сигнала №1 на промежутке tt = -N..N
def autocorelation(signal, M):
  start_time = time.time()
  Rxx = []
  for tt in range(0, N):
    rx = 0
    for t in range(N):
      if t+tt > 0 and t+tt < N:
        rx += (signal[t] - M) * (signal[t+tt] - M)
    rx = rx / (N - 1)
    Rxx.append(rx)
  Rxx_timer.append(time.time() - start_time)
  return Rxx

# Взаимная корелляция на промежутке tt = 0..N/2
def bothcorelation(signal1, M1, signal2, M2):
  start_time = time.time()
  Rxy = []
  for tt in range(0, N):
    ry = 0
    for t in range(N):
      if t+tt > 0 and t+tt < N:
        ry += (signal1[t] - M1) * (signal2[t+tt] - M2)
    ry = ry / (N - 1)
    Rxy.append(ry)
  Rxy_timer.append(time.time() - start_time)
  return Rxy

def main_fn():
  signal1 = np.array([generate_signal(i) for i in range(N)])
  M1 = expected_value(signal1)
  D1 = dispersion(M1, signal1)
  # print('Mat №1: ', M1)
  # print('D №1: ', D1)

  signal2 = np.array([generate_signal(i) for i in range(N)])
  M2 = expected_value(signal2)
  D2 = dispersion(M2, signal2)
  # print('Mat №2: ', M2)
  # print('D №2: ', D2)

  for _ in range(0, 2000):
    Rxx = autocorelation(signal1, M1)
    Rxy = bothcorelation(signal1, M1, signal2, M2)
  
  print("Rxx: --- %s seconds ---" % sum(Rxx_timer))
  print("Rxy: --- %s seconds ---" % sum(Rxy_timer))

  print("Rxx average: --- %s seconds ---" % (sum(Rxx_timer) / 2000))
  print("Rxy average: --- %s seconds ---" % (sum(Rxy_timer) / 2000))

  options = [
    DrawOption("Signal 1", "plot"),
    DrawOption("Signal 2", "plot"),
    DrawOption("Rxx", "plot", range(0, N)),
    DrawOption("Rxy", "plot", range(0, N)),
  ]
  
  draw([signal1, signal2, Rxx, Rxy], options, "lab2.png")

if __name__ == '__main__':
  main_fn()