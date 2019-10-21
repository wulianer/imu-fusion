import numpy as np

from state import KinematicState
from integrator import Euler, RK4


if __name__ == "__main__":
  t = 0
  dt = 1

  euler = Euler()
  rk4 = RK4()
  
  state = KinematicState(0, 0, 10)
  print("Euler's method...")
  for i in range(10):
    state = euler.integrate(state, t, dt)
  print(i+1, state.pos, state.vel)

  state = KinematicState(0, 0, 10)
  print("RK4...")
  for i in range(10):
    state = rk4.integrate(state, t, dt)
  print(i+1, state.pos, state.vel)

  actual = 0.5 * 10 * 10**2
  print("True position at t=10: {}".format(actual))
