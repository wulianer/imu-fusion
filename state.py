from abc import ABC, abstractmethod

import numpy as np


class State(ABC):
  """A state describes the underlying configuration of a system.
  """
  def __init__(self, *args):
    pass

  @abstractmethod
  def dsdt(self, t):
    """Describes how the state variables change over a very small time delta.

    In other words, computes the gradient of the state variables wrt time.

    Args:
      t (float): The current timestep.

    Returns:
      dsdt (object): a state containing the gradient of each state variable
        with respect to time.
    """
    pass

  @abstractmethod
  def __add__(self, other):
    """Defines how a state delta (dsdt) is added to the current state.
    """
    pass

  @abstractmethod
  def __mul__(self, other):
    """Defines how a state is multiplied by a scalar value.
    """
    pass


class KinematicState(State):
  """A simple 3D kinematic state with constant acceleration.
  """
  def __init__(self, pos, vel, acc):
    self.pos = np.asarray(pos)
    self.vel = np.asarray(vel)
    self.acc = np.asarray(acc)

  def __repr__(self):
    s = "[p: {:.2f}, v: {:.2f}, a: {:2f}]"
    return s.format(self.pos, self.vel, self.acc)

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

  def dsdt(self, t):
    # we assume constant acceleration
    # thus the value of the current timestep
    # is ignored
    return self.__class__(self.vel, self.acc, np.zeros(3))
