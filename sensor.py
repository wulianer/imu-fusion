from abc import ABC, abstractmethod

import numpy as np

from walle.core import Pose


class Sensor(ABC):
  """A sensor maps an underlying hidden state to a noisy measurement.
  """
  def __init__(self, pose=Pose()):
    """Initialies the sensor.

    Args:
      pose (Pose): The pose of the sensor wrt the local coordinate
        frame.
    """
    self.pose = pose

  @abstractmethod
  def measure(self, state):
    """Returns the true value of the given state.

    Args:
      state (State): the underlying state of the system.
    """
    pass

  @abstractmethod
  def corrupt(self, state):
    """Generates stochastic noise according to the characteristic of the sensor.

    Args:
      state (State): the underlying state of the system.
    """
    pass

  def simulate(self, state):
    """Returns a stochastic measurement of the given state. 

    Args:
      state (State): the underlying state of the system.
    """
    return self.measure(state) + self.corrupt(state)


class WhiteNoiseSensor(Sensor):
  """A noisy sensor with additive Gaussian noise.
  """
  def __init__(self, cov, *args):
    """Initializes the noisy sensor.

    Args:
      cov (ndarray): the noise covariance matrix of shape (, ).
    """
    super().__init__(args)
    self.cov = cov

  def corrupt(self, state):
    return np.random.multivariate_normal(np.zeros(3), self.cov)


class Accelerometer:
  """An accelerometer measures the specific force f.
  """
  pass


class Gyroscope:
  """A gyroscope measures the angular velocity w.
  """
  pass


class Magnetometer:
  pass
