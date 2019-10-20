## Inertial Measurement Unit

An IMU usually consists of three types of sensors:

* gyroscope: measures the angular velocity in degrees/sec
* accelerometer: measures the linear acceleration in m/s^2
* magnetometer: measures the magnetic field strength in micro Tesla or Gauss.

If you integrate the gyroscope measurements, you can recover the orientation of the sensor. After subtracting the earth's gravity, you can double integrate the accelerometer measurements to obtain information about the sensor's position. Because you need to know the orientation of the sensor to subtract Earth's gravity, position and orientation estimation of the sensor are inherently linked. This process is known as dead reckoning.

Inertial sensors provide pose estimates at high sampling rates which are accurate on a short time scale but drift over longer time scales. They are therefore very suitable for being combined with sensors with a lower sampling rate but with information that does not drift over time (e.g. magnetometer, GPS data, etc.).

## References

- [Position and Orientation Estimation](https://arxiv.org/pdf/1704.06053.pdf)
