# ROS 2 Robot Modeling and Simulation

A hands-on repository containing custom ROS 2 nodes, interface packages, robot description files (URDF/Xacro), transform configurations (TF2), and Gazebo simulation setups.

## 📦 Packages Included

- **my_cpp_pkg**: C++ implementation of publishers, subscribers, custom clients, and nodes.
- **my_py_pkg**: Python implementation of publisher/subscriber nodes, custom action servers, parameter management, and controllers.
- **my_robot_interfaces**: Custom interface definitions for messages (.msg), services (.srv), and actions (.action).

## 🚀 Getting Started

### Build Instructions

```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
```
