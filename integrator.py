from abc import ABC, abstractmethod

import numpy as np


class Integrator(ABC):
  """An abstract class for a numerical integrator.
  """
  def __init__(self):
    pass

  @abstractmethod
  def integrate(self, state, t, dt):
    pass


class Euler(Integrator):
  """Euler's method integrator.
  """
  def integrate(self, state, t, dt, dsdt=None):
    """Extrapolates value at `t+dt` using the gradient at `t`.
    """
    if dsdt is None:
      dsdt = state.dsdt(t)
    next_state = state + dt * dsdt
    return next_state


class RK4(Integrator):
  """4th order Runge-Kutta integrator.
  """
  def __init__(self):
    self.euler = Euler()

  def _evaluate(self, state, t, dt, dsdt):
    """Advances the state using Euler's method and computes the gradient at that state.
    """
    next_state = self.euler.integrate(state, t, dt, dsdt)
    return next_state.dsdt(t + dt)

  def integrate(self, state, t, dt):
    k1 = self._evaluate(state, t, 0, None)
    k2 = self._evaluate(state, t, dt/2, k1)
    k3 = self._evaluate(state, t, dt/2, k2)
    k4 = self._evaluate(state, t, dt, k3)
    m = (1 / 6) * (k1 + 2*k2 + 2*k3 + k4)
    next_state = state + m*dt
    return next_state
