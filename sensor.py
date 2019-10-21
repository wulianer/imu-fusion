from abc import ABC, abstractmethod

import numpy as np


class Accelerometer:
  """An accelerometer measures specific force.
  """
  def __init__(self):
    pass

  def measure(self):
    # f = R @ (a - g)

  def simulate(self):
    pass


class Gyroscope:
  """A gyroscope measures angular velocity.
  """
  def __int__(self):
    pass

  def measure(self):
    """Measures the angular velocity of the body frame wrt intertial frame
    expressed in body frame.
    """
    # assume navigation frame is stationary => w_en = 0
    # w_ib = R @ w_ie + w_nb


class Magnetometer:
  def __init__(self):
    pass


