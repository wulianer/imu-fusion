# imu-fusion

The goal of this repo is to implement IMU sensor fusion in simulation and on real hardware using an Arduino.

## Todos

- [x] Implement 2 integrators: Euler's and 4th-order Runge-Kutta.
- [x] Implement various state classes.
- [ ] Create 3 sensor classes: accelerometer, gyroscope and magnetometer.
- [ ] Implement a Kalman Filter and an EKF.
- [ ] Create a linear state estimation problem and apply the Kalman filter to it.

## References

Here's a list of resources I consulted for this project:

- https://lpsa.swarthmore.edu/NumInt/NumIntFourth.html
- https://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/
- http://cs229.stanford.edu/section/more_on_gaussians.pdf
- https://github.com/trbabb/kalman
- https://arxiv.org/abs/1704.06053
