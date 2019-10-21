# imu-fusion

The goal of this repo is to get familiar with filters in the context of state estimation (e.g. sensor fusion). I'm going to be implementing the following filters:

* Kalman Filter
* Extended Kalman Filter
* Extended Kalman Filter (with autodiff)
* Unscented Kalman Filter
* Histogram Filter
* Particle Filter

## Simulation

- [ ] Create a simulation class for three sensors: accelerometer, gyroscope and magnetometer.
- [ ] Create simulation data by simulating the sensors using kinematics.
    - [ ] Simulated data will need an implementation of [Runge-Kutta 4](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods). 
- [ ] Corrupt the above "ground-truth" with noise.

## Arduino
