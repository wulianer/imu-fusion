from abc import ABC, abstractmethod

import numpy as np


class State(ABC):
  """A state describes the underlying configuration of a system.
  """
  def __init__(self, *args):
    pass

  @abstractmethod
  def dsdt(self):
    """Describes how the state variables change over a very small time delta.
    """
    pass

  @abstractmethod
  def __add__(self, other):
    """Defines how a state delta (dsdt) is added to the current state.
    """
    pass


class TestRK4(State):
  def __init__(self):
    pass

  def __add__(self, other):
    pass

  def dsdt(self):
    pass


class KinematicState(State):
  """A simple 2D kinematic state.
  """
  def __init__(self, pos=None, vel=None, acc=None):
    self.pos = pos if pos is not None else np.zeros(2)
    self.vel = vel if vel is not None else np.zeros(2)
    self.acc = acc if acc is not None else np.zeros(2)

  def __add__(self, other):
    if isinstance(other, KinematicState):
      return self.__class__(
        self.pos + other.pos,
        self.vel + other.vel,
        self.acc + other.acc,
      )
    else:
      raise NotImplemented

  def dsdt(self):
    """Newton's second law of motion.
    """
    return self.__class__(
      self.vel,
      self.acc,
      None,  # assumes constant acceleration
    ) 


def rk4_step(s_init, t_init, step_size):
  """Advances a state governed by differential equations using 4th order Runge-Kutta.
  """
  pass
