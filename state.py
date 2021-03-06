from abc import ABC, abstractmethod

import numpy as np


class State(ABC):
  """A state describes the underlying configuration of a system.
  """
  def __init__(self, *args):
    pass

  @abstractmethod
  def grad(self, t):
    """Describes how state variables change over a very small time delta.

    Args:
      t (float): The current timestep.

    Returns:
      grad (object): the gradient of each state variable
        with respect to time, evaluated at the given
        timestep `t`.
    """
    pass

  @abstractmethod
  def __add__(self, other):
    pass

  @abstractmethod
  def __mul__(self, other):
    pass


class KinematicState(State):
  """A simple kinematic state with constant acceleration.
  """
  def __init__(self, pos, vel, acc):
    self.pos = np.asarray(pos)
    self.vel = np.asarray(vel)
    self.acc = np.asarray(acc)

  def __add__(self, other):
    if isinstance(other, KinematicState):
      return self.__class__(
        self.pos + other.pos,
        self.vel + other.vel,
        self.acc + other.acc,
      )
    else:
      raise NotImplemented

  def __mul__(self, other):
    if isinstance(other, (int, float)):
      return self.__class__(
        other * self.pos,
        other * self.vel,
        other * self.acc,
      )
    else:
      raise NotImplemented

  def __rmul__(self, other):
    return self * other

  def __truediv__(self, other):
    if isinstance(other, (int, float)):
      return (1 / other) * self
    else:
      raise NotImplemented

  def grad(self, t):
    # we assume constant acceleration
    # thus the value of the current timestep
    # is ignored
    return self.__class__(self.vel, self.acc, np.zeros(3))
