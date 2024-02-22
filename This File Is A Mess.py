import numpy as np
import math
import matplotlib.pyplot as plt

class radioactivedecay:
    def __init__(self, N, lam):
        self.t = 0.0
        self.N = N
        self.lam = lam
        self.halfLife = math.log(2.0)/self.lam
        self.dt = 0.1*self.halfLife

    def calculate(self, dt=None):
        _dt = self.dt
        if dt is not None:
            _dt = dt
        self.N -= self.lam*self.N*_dt
        self.t += _dt

decay = radioactivedecay(1e6, math.log(2.0)/2)
N = [1e6]
t = [0.0]
num = int(decay.halflife*5/decay.dt)
for i in range(1, num):
    decay.calculate()
    N.append(decay.N)
    t.append(decay.t)
plt.semilogy(t, N)
plt.show()
