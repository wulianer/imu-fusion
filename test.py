import numpy as np

from state import KinematicState
from integrator import Euler, RK4


if __name__ == "__main__":
  t = 0
  dt = 1
  pos = np.zeros(3)
  vel = np.zeros(3)
  acc = np.array([1, 4, 10])

  euler = Euler()
  rk4 = RK4()
  
  state = KinematicState(pos, vel, acc)
  print("Euler's method...")
  for i in range(10):
    state = euler.integrate(state, t, dt)
  print(i+1, state.pos)

  state = KinematicState(pos, vel, acc)
  print("RK4...")
  for i in range(10):
    state = rk4.integrate(state, t, dt)
  print(i+1, state.pos)

  actual = 0.5 * acc * 10**2
  print("True position at t=10: {}".format(actual))
